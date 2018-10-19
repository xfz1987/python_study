#!/usr/bin/env python
#coding=utf-8

# 面向对象
'''
Student(要继承的父类，如果没有要继承的，就继承object)
__init__(self) 构造函数，第一个参数永远是 self
私有属性：在属性名称前加__，既然不可以写，那么就跟不就不能从外部直接访问
'''
class Student(object):
  def __init__(self, name, score):
    self.__name = name
    self.__score = score

  def print_score(self):
    print('%s: %d' % (self.__name, self.__score))

  def getName(self):
    print(self.__name)

  def setName(self, name):
    self.__name = name

tom = Student('Tome', 60)
jake = Student('jake', 90)
tom.print_score()
jake.print_score()
# tom.name = 'mkie'
# tom.print_score()
tom.getName()
tom.setName('SB')
tom.getName()

# 继承和堕胎
'''
'''
class Animal(object):
  def run(self):
    print('Animal is running')

class Dog(Animal):
  # 方法重写
  def run(self):
    print('dog is running')
  def eat(self):
    print('dog is eating')

class Cat(Animal):
  def run(self):
    print('cat is running')
  def pa(self):
    print('cat is paing')

animal = Animal()
animal.run()

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.pa()
cat.run()