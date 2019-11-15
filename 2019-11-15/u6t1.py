# coding: utf-8
from u6 import Person


class Student(Person):
    """docstring for Student"""
    def __init__(self, name='', age=20, sex='man', major='Computer'):
        super(Student, self).__init__(name, age, sex)
        self.setMajor(major)

    def setMajor(self, major):
        if not type(major) == str:
            raise Exception('major must be a string.')
        self.__major = major

    def show(self):
        super(Student, self).show()
        print(self.__major)


if __name__ == '__main__':
    xiaoming = Student('Xiao ming', 19, 'man', 'English')
    xiaoming.show()
