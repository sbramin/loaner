package main

import "fmt"

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

func pickLender(lo loan, les []lender) {
	//el := make([]lender, 0)
}

func main() {
	lenders := make(map[string]lender)
	loans := make([]loan, 0)

	lenders["Joe"] = lender{Name: "Joe", Budget: 10000, Grade: grade{Rating: 4, Operator: ">"}, Investments: map[string]investment{"cars": investment{}, "beer": investment{MaxPercent: 0.5}}}
	lenders["Frank"] = lender{Name: "Frank", Budget: 20000, Grade: grade{Rating: 2, Operator: ">="}, Investments: map[string]investment{"cars": investment{}, "beer": investment{MaxPercent: 0.5}}}
	lenders["Jane"] = lender{Name: "Jane", Budget: 10000, Grade: grade{Rating: 4, Operator: ">"}, Investments: map[string]investment{"cars": investment{}, "goats": investment{}}}

	loans = append(loans, loan{Amount: 100000, Category: "beer", Rating: 4})
	loans = append(loans, loan{Amount: 100000, Category: "burgers", Rating: 4})
	loans = append(loans, loan{Amount: 100000, Category: "cars", Rating: 2})

	fmt.Println(lenders)
	//fmt.Println(loans)
}
