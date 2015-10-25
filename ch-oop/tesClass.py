__author__ = 'haven'


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s,%s' % (self.name, self.score))


bart = Student('bart', 33)

bart.print_score()
