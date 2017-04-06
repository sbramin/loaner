package main

import (
	"fmt"
	"math/rand"
)

type investment struct {
	Invested   int64
	MaxPercent float64
}

type grade struct {
	Rating   int64
	Operator string
}

type loan struct {
	Amount         int64
	Category       string
	Rating         int64
	AmountInvested int64
}

type lender struct {
	Name        string
	Budget      int64
	Investments map[string]investment
	Grade       grade
}

func grader(l loan, g grade) bool {
	switch g.Operator {
	case ">":
		if l.Rating > g.Rating {
			return true
		}
	case ">=":
		if l.Rating >= g.Rating {
			return true
		}
	}
	return false
}

func pickLender(lo loan, les map[string]lender) (lender, error) {
	el := make([]lender, 0)
	for _, l := range les {
		if l.Budget == 0 {
			continue
		}
		if lenderCat, ok := l.Investments[lo.Category]; !ok {
			continue
		} else {
			if lenderCat.Invested >= int64(lenderCat.MaxPercent*float64(l.Budget)) {
				continue
			}
			if grader(lo, l.Grade) {
				el = append(el, l)
			}
		}
	}
	if len(el) == 0 {
		return lender{}, fmt.Errorf("no eligble lenders for a %s loan", lo.Category)
	} else {
		n := rand.Int() % len(el)
		return el[n], nil
	}
}

func (le *lender) Invest(lo loan) error {
	if le.Budget == 0 {
		return fmt.Errorf("Out of cash!")
	} else {
		le.Budget -= 2000
		invested := le.Investments[lo.Category].Invested
		invested += 2000
		fmt.Printf("%s bought £20 of %s \n", le.Name, lo.Category)
	}
	return nil
}

func (lo *loan) Buy() error {
	if lo.AmountInvested == lo.Amount {
		return fmt.Errorf("Loan already satisfied")
	} else {
		lo.AmountInvested += 2000
	}
	return nil
}

func main() {
	lenders := make(map[string]lender)
	loans := make([]loan, 0)

	lenders["Joe"] = lender{Name: "Joe", Budget: 10000, Grade: grade{Rating: 3, Operator: ">"}, Investments: map[string]investment{"cars": investment{}, "beer": investment{MaxPercent: 0.5}}}
	lenders["Frank"] = lender{Name: "Frank", Budget: 20000, Grade: grade{Rating: 2, Operator: ">="}, Investments: map[string]investment{"cars": investment{}, "beer": investment{MaxPercent: 0.5}}}
	lenders["Jane"] = lender{Name: "Jane", Budget: 10000, Grade: grade{Rating: 4, Operator: ">"}, Investments: map[string]investment{"cars": investment{}, "goats": investment{}}}
	lenders["Mary"] = lender{Name: "Mary", Budget: 10000, Grade: grade{Rating: 3, Operator: ">"}, Investments: map[string]investment{"homes": investment{}, "beer": investment{}}}

	loans = append(loans, loan{Amount: 10000, Category: "beer", Rating: 4})
	//loans = append(loans, loan{Amount: 100000, Category: "burgers", Rating: 3})
	//loans = append(loans, loan{Amount: 100000, Category: "cars", Rating: 2})

	for _, l := range loans {
		for l.Amount > l.AmountInvested {
			lender, err := pickLender(l, lenders)
			if err != nil {
				break
			} else {
				lender.Invest(l)
				l.Buy()
			}
		}

		fmt.Println()

	}

}
