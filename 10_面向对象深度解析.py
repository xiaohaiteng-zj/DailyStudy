#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 18:02
# @Author  : 小海腾
# 学习链接   : https://www.runoob.com/python3/python3-class.html


class People(object):
    name = ''
    age = 0
    _tc = ''

    def __init__(self, name, age, tc):
        self.name = name
        self.age = age
        self._tc = tc

    def description(self):
        return '我是{name}，今年{age}岁，擅长{tc}'.format(name=self.name, age=self.age, tc=self._tc)

    def add(self, x):
        y = x + 2
        return y


class Student(People):
    school = ''

    def __init__(self, name, age, tc, school):
        super(Student, self).__init__(name, age, tc)
        self.school = school

    def description(self):
        return '我是{name}，毕业于{school}，今年{age}岁，擅长{tc}'.format(name=self.name,school=self.school, age=self.age, tc=self._tc)

    def add_a(self, x, a):
        y = super(Student, self).add(x)
        b = y + a
        return b


a = People('张佳', 25, 'python')
re = a.description()
print(re)
print(a.add(6))
b = People('小海腾', 25, 'java')
re2 = b.description()
print(re2)
print(b.add(6))
c = Student('李四', 18, 'c++', '华东师范大学')
re3 = c.description()
print(re3)
print(c.add_a(3, 5))
