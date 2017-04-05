#!/usr/bin/env python3

from random import choice


class TypeRatio(object):
    def __init__(self, type, ratio=100):
        self.type = type
        self.ratio = ratio

    def info(self):
        print(self.type, self.ratio)


class GradeRank(object):
    def __init__(self, grade=0, oper='>='):
        self.grade = grade
        self.oper = oper


class Person(object):
    def __init__(self, name, types, grade_rank):
        self.name = name.title()
        self.types = types
        self.grade_rank = grade_rank

    def info(self):
        print(self.name)
        for tr in self.types:
            tr.info()
        print(self.grade)
        print()

    def my_types(self):
        types = []
        for tr in self.types:
            types.append(tr.type)
        return types


class Payment(object):
    def __init__(self, amount, type, grade):
        self.amount = amount
        self.type = type
        self.grade = grade

    def info(self):
        print(self.name)
        print(self.types)
        print(self.grade)


def grader(payment_grade, person_grade_rank):
    operators= {
        '>': lambda x, y: True if x > y else False,
        '>=': lambda x, y: True if x >= y else False
    }
    return operators[person_grade_rank.oper](payment_grade, person_grade_rank.grade)


def main():
    people = []
    eligble_people = []

    payin = Payment(1000, 'cars', 4)

    people.append(Person('John', [TypeRatio('cars', 50), TypeRatio('beer', 50)], GradeRank(3,'>')))
    people.append(Person('frank', [TypeRatio('cars'), TypeRatio('bikes')], GradeRank(4,'>=')))
    people.append(Person('bob', [TypeRatio('bikes')], GradeRank()))
    people.append(Person('Boby', [TypeRatio('cars')], GradeRank()))

    for person in people:
        if payin.type not in person.my_types():
            continue
        else:
            if grader(payin.grade, person.grade_rank):
                eligble_people.append(person)

    if eligble_people:
        print("{} is going to buy some {}".format(choice(eligble_people).name, payin.type))
    else:
        print("no one fits the bill")

if __name__ == '__main__':
    main()
