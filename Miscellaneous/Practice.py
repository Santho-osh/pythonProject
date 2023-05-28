# x = 'Santhosh'
# print(type(x))


# def hello():
#     print('Hello')
#
#
# print(type(hello))

# class Employee:
#
#     def __init__(self, name, emp_id, position):
#         self.name = name
#         self.emp_id = emp_id
#         self.position = position
#
#     def get_name(self):
#         print(self.name)
#
#     def get_emp_id(self):
#         print(self.emp_id)
#
#     def get_position(self):
#         print(self.position)
#
#     def set_name(self, name):
#         self.name = name

# class Student:
#
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def get_grade(self):
#         return self.grade
#
# class Course:
#
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#     def get_avg_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def details(self):
#         print(f'I am {self.name} and I am {self.age} years old')
#
# class Dog(Animal):
#     def speak(self):
#         print('Bark')
#
# class Cat(Animal):
#
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#
#     def speak(self):
#         print('Meow')
#
#     def colordetails(self):
#         print(f'I am {self.color} color')
#
# class Fish(Animal):
#     def ability(self):
#         print('I can live in Water')
#
# dog1 = Dog('Tommy', 2)
# dog1.speak()
# dog1.details()
#
# cat1 = Cat('Dumma', 5, 'Brown')
# cat1.colordetails()
# cat1.details()

# class Students:
#
#     student_list = []
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Students.student_list.append(self.name)
#
#     @classmethod
#     def all_students(cls):
#         return cls.student_list
#
#     @staticmethod
#     def sums(lists: []):
#         ans = 0
#         for i in lists:
#             ans += i
#         return ans
#
#
#
#
#
# s1 = Students('Santhosh', 24)
# s2 = Students('Bharathi', 23)
#
# print(Students.all_students())
#
# orulist = [1,2,3,4,5,55,6]
#
# print(Students.sums(orulist))
#
# print(s1.sums(orulist))

# class Summa:
#     def __init__(self):
#         print(f'{self} is created')
#
#     def testing(self, name):
#         print(f'{self} got a name {name}')
#
# obj_of_summa = Summa()
# obj_of_summa.testing('Santhosh')

import csv
class Products:

    pay_rate = 0.8 #20% discount
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        #Validation for data type
        assert price > 0
        assert quantity > 0

        #Assigning to self
        self.name = name
        self.price = price
        self.quantity = quantity
        Products.all.append(self)

    def total_amount(self):
        return self.price * self.quantity

    @classmethod
    def read_from_csv(cls):
        name = price = quantity = ''
        with open('Products.csv', 'r') as p:
            reader = csv.DictReader(p)
            product = list(reader)



        for i in product:
            name = i.get('Product')
            price = i.get('Price')
            quantity = i.get('Quantity')
            return name, price, quantity, product
            # Products(name=i.get('Product'),
            #          price=float(i.get('Price')),
            #          quantity=i.get('Quantity'),
            #          )

        # for i in product:
        #     print(i)

        # for items in product:
        #     Print(items.get('Product'))
        #     Products(
        #         name = items.get('Product'),
        #         price = float(items.get('Price')),
        #         quantity = items.get('Quantity')
        #     )

    def discounted_price(self):
        self.price = self.price * Products.pay_rate
        return self.price

    def __repr__(self):
        return f'Products("{self.name}", {self.price}, {self.quantity})'


class Phone(Products):

    def __init__(self, name, price, quantity, broken):
        super().__init__(name, price, quantity)
        self.broken = broken



# item1 = Products('Laptop', 50000, 2)
# print(item1.discounted_price())
# Products.read_from_csv()
# print(Products.all)
print(Products.read_from_csv())
phone1 = Phone('Apple', 70000, 1, 'Yes')
print(phone1.broken)





































































































































