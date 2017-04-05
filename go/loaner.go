package main

import "fmt"

type investment struct {
	Category   string
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
	Investments []investment
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
	el := make([]lender, 0)
	fmt.Println(el)
}

func main() {
	lenders := make([]lender, 0)
	loans := make([]loan, 0)

	lenders = append(lenders, lender{Name: "Joe", Budget: 10000, Grade: grade{Rating: 4, Operator: ">"}, Investments: []investment{investment{Category: "cars"}, investment{Category: "boats", MaxPercent: .5}}})
	lenders = append(lenders, lender{Name: "Bob", Budget: 20000, Grade: grade{Rating: 5, Operator: ">="}, Investments: []investment{investment{Category: "beer"}, investment{Category: "boats", MaxPercent: .5}}})

	loans = append(loans, loan{Amount: 100000, Category: "beer", Rating: 4})

	fmt.Println(lenders)
	fmt.Println(loans)
}
