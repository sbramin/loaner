#!/usr/bin/env python3

from random import choice


class TypeRatio(object):
    def __init__(self, type, ratio=100):
        self.type = type
        self.ratio = ratio

    def info(self):
        print(self.type, self.ratio)


class GradeRank(object):
    def __init__(self, grade, oper):
        self.grade = grade
        self.oper = oper


class Person(object):
    def __init__(self, name, types, grade_rank):
        self.name = name
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


def compare_grades():
    operators= {
        '>': lambda: x, y: True if x > y else False,
        '<': lambda: x, y: True if x < y else False,
        '>=': lambda: x, y: True if x >= y else False,
        '<=': lambda: x, y: True if x <= y else False
    }
    return operators


def main():
    grader = compare_grades()
    print()

    people = []
    eligble_people = []

    payin = Payment(1000, 'cars', 2)

    people.append(Person('John', [TypeRatio('cars', 50), TypeRatio('beer', 50)], GradeRank(3,'>')))
    people.append(Person('frank', [TypeRatio('cars'), TypeRatio('bikes')], GradeRank(2,'>')))
    people.append(Person('bob', [TypeRatio('bikes')], GradeRank(2,'>')))

    for person in people:
        if payin.type in person.my_types():
            if grader[person.grade_rank.oper](payin.grade, person.grade_rank.grade):
                eligble_people.append(person)

    print(eligble_people)

if __name__ == '__main__':
    main()
