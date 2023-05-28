# class Car:
#
#     def __int__(self, color, make, year):
#         self.color = color
#         self.make = make
#         self.year = year
#
# class Car:
#    # Constructor
#    def __init__(self, name, year_built, model):
#        self.name = name
#        self.year_built = year_built
#        self.model = model
#
#    def __repr__(self):
#         return f'Car({self.name},{self.year_built},{self.model})'

# class Prey:
#     def flees(self):
#         print('This animal flees')
# class Predator:
#     def hunts(self):
#         print('This animal hunts')
# class Rabbit(Prey):
#     pass

# from Practice import Employee
#
# emp1 = Employee('Santhosh', 12345, 'SE')
#
# emp1.get_name()
# emp1.get_emp_id()
# emp1.get_position()
# emp1.set_name('Bharathi')
# emp1.get_name()

# from Practice import Student, Course
#
# s1 = Student('Santhosh', 90)
# s2 = Student('Bharathi', 95)
# s3 = Student('Tharun', 80)
# s4 = Student('Krithika', 70)
# s5 = Student('Karthick', 70)
# s6 = Student('Sharath', 60)
#
# course = Course('Programming', 5)
#
# course.add_student(s1)
# course.add_student(s2)
# course.add_student(s3)
# course.add_student(s4)
# course.add_student(s5)
# course.add_student(s6)
#
# Student.__init__(s1, 'Santhosh', 90)
# print(s1.grade)
# print(course.get_avg_grade())
# print(course.students[0].name)

# collectionss = {'Name': 'SS',
#                'Age': 23,
#                'Summa': 'Therila'}

class Item:

    all = []

    def __init__(self, name, price):
        self.__name = name
        self.price = price

    #Makes the name attribute a read only field and cannot be changed
    @property
    def name(self):
        return self.__name

    #Allows user to set a value even if property decorator is present
    @name.setter
    def name(self, value):
        if len(value) >= 10:
            raise Exception('Name is too long')
        else:
            self.__name = value

Item1 = Item('IPhone 14 Pro', 130000)
Item1.name = 'Iphone 15 pro'
print(Item1.name)







