#!/usr/bin/env python3

from random import choice


class Investment(object):
    def __init__(self, type, max_percent=1, budget=0, invested=0,):
        self.type = type
        self.budget= budget
        self.invested= invested
        self.max_percent= max_percent

    def info(self):
        print(self.type, self.max_percent, self.invested)


class GradeRank(object):
    def __init__(self, grade=0, oper='>='):
        self.grade = grade
        self.oper = oper


class Person(object):
    def __init__(self, name, investments, total_budget=0, grade_rank=GradeRank()):
        self.name = name.title()
        self.investments = investments
        self.total_budget = total_budget
        self.grade_rank = grade_rank

    def info(self):
        print(self.name)
        for i in self.investments:
            i.info()
        print(self.grade_rank)

    def investment_types(self):
        investments = []
        for i in self.investments:
            investments.append(i.type)
        return investments

    # def maxed_out(self, )


class Loan(object):
    def __init__(self, amount, type, grade):
        self.amount = amount
        self.type = type
        self.grade = grade
        self.amount_lent = 0

    def info(self):
        print(self.type)
        print(self.grade)
        print(self.amount_lent)

    def lend_in(self):
        self.amount_lent += 2000

    def fufilled(self):
        return True if self.amount <= self.amount_lent else False


def grader(payment_grade, person_grade_rank):
    operators = {
        '>': lambda x, y: x > y,
        '>=': lambda x, y: x >= y
    }
    return operators[person_grade_rank.oper](payment_grade,
                                             person_grade_rank.grade)


def pick_lender(loan, people):
    eligble_people = []
    for person in people:
        if loan.type not in person.investment_types():
            continue
        else:
            if grader(loan.grade, person.grade_rank):
                eligble_people.append(person)

    if eligble_people == []:
        return False
    else:
        return choice(eligble_people)


def main():
    people = []
    eligble_people = []
    loans = []

    loans.append(Loan(100000, 'cars', 4))
    loans.append(Loan(100000, 'boats', 4))
    loans.append(Loan(100000, 'bikes', 1))
    loans.append(Loan(100000, 'beer', 5))

    people.append(Person('John', [Investment('cars', .5), Investment('beer')], 500000, GradeRank(3,'>')))
    people.append(Person('frank', [Investment('cars'), Investment('bikes')], 10000, GradeRank(4,'>=')))
    people.append(Person('bob', [Investment('bikes')], 10000, GradeRank()))
    people.append(Person('Boby', [Investment('cars')], 20000, GradeRank()))


    for loan in loans:
        lender = pick_lender(loan, people)
        if lender:
            print("{} is going to invest in {}".format(lender.name, loan.type))
    """
        while loan.fufilled() is False:
                        loan.lend_in()
        print("loan for {} was {}".format(loan.type, loan_result))
    """


if __name__ == '__main__':
    main()
