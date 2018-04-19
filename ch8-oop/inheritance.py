#! /usr/bin/python3
#-*-coding:UTF-8-*-

class Animal(object):
	def run(self):
		print('animal is running...')

	def __run(self):
		print('i am a private method.')

	def jump(self):
		print('animal is jumpping...')

class Dog(Animal):
	def eat(self):
		print('dog is eating...')

	def run(self):
		print('dog is running...')

class Cat(Animal):
	pass

dog = Dog()
cat = Cat()
dog.jump()
dog.run()
dog.eat()
#dog.__run()
cat.run()
print(isinstance(dog, Animal))