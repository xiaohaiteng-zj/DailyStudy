#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 13:35
# @Author  : 小海腾
# 学习链接   : https://www.cnblogs.com/anzhangjun/p/9780463.html


import abc


class Animal(metaclass=abc.ABCMeta):
    """
    1、抽象基类只能被继承，不能实例化，实例化会报错
    2、抽象基类主要定义了基本类和最基本的抽象方法，为子类定义共有的api，不需要具体实现
    3、抽象基类可以不实现具体的方法（当然也可以实现，只不过子类如果想调用抽象基类中定义的方法需要使用super()）而是将其留给派生类实现
    """

    @abc.abstractmethod   # 加完这个方法子类必须有这个方法，否则报错
    def run(self):
        pass

    @abc.abstractmethod   # 加完这个方法子类必须有这个方法，否则报错
    def eat(self):
        pass


class People(Animal):
    
    def run(self):
        print("People is walking")
        
    def eat(self):
        print("people is eating")


class Dog(Animal):

    def run(self):
        print("Dog is zouing")

    def eat(self):
        print("dog is eating")


if __name__ == '__main__':
    p = People()
    p.eat()