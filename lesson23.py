# N1
# class Calc:
#     def __init__(self, arg1, arg2):
#         self.arg1 = arg1
#         self.arg2 = arg2

#     def gumar(self):
#         return self.arg1 + self.arg2

#     def hanum(self):
#         return self.arg1 - self.arg2
    
#     def bazmapatkum(self):
#         return self.arg1 * self.arg2

#     def bajanum(self):
#         try:
#             return self.arg1 / self.arg2
#         except ZeroDivisionError:
#             return "0"
# while True:
#     try:
#         x = float(input("Enter number 1st --->"))
#         y = float(input("Enter number 2dt --->"))
#         a = Calc(x, y)
#         print(a.gumar())
#         break
#     except ValueError:
#         print("Enter onli number!!")
#         continue

# N3
# class Change:
#     def __init__(self, usd):
#         self.usd = usd
    
#     def dram(self):
#         return self.usd * 490
#     def ru(self):
#         return self.usd * 40
#     def eur(self):
#         return self.usd * 0.25

# pox = Change(100)
# print(pox.dram())
# print(pox.ru())
# print(pox.eur())
        




# class Staff:
#     def __init__ (self, pPosition, pName, pPay):
#         self._position = pPosition
#         self.name = pName
#         self.pay = pPay
#         print('Creating Staff object')

#     @property
#     def position(self):
#         print("Getter Method")
#         return self._position
#     @position.setter
#     def position(self, value):
#         if value == 'Manager' or value == 'Basic':
#             self._position = value
#         else:
#             print('Position is invalid. No changes made.')
#     def __str__(self):
#         return "Position = %s, Name = %s, Pay = %d"%(self._position, self.name, self.pay)
#     def calculatePay(self):
#         prompt = '\nEnter number of hours worked for %s: ' %(self.name)
#         hours = input(prompt)
#         prompt = 'Enter the hourly rate for %s: '%(self.name)
#         hourlyRate = input(prompt)
#         self.pay = int(hours)*int(hourlyRate)
#         return self.pay

# officeStaff1 = Staff('Basic', 'Yvonne', 0)
# print(officeStaff1.name)
# print(officeStaff1.position)

# #изменение переменной position
# officeStaff1.position = 'Manager'
# #повторный вывод position
# print(officeStaff1.position)

# # Использование метода calculatePay() для вычисления зарплаты:
# print(officeStaff1.calculatePay())
# print(officeStaff1.pay)

# # Вывод строкового представления officeStaff1:
# print(officeStaff1)


# officeStaff1 = Staff('Basic', 'Yvonne', 0)
# print(officeStaff1._position)

# officeStaff1.position = 'Manager'
# print(officeStaff1._position)

# officeStaff1.position = 'CEO'
# print(officeStaff1._position)
# print(officeStaff1._position)





# 9.5. КОРРЕКТИРОВКА ИМЕН 

# class A:
#     def __init__(self):
#         self.__x = 5
#         self._y = 6

# varA = A()
# print(varA._y)

# # произойдет ошибка.--- varA.__x
# print(varA.__x)
# # получить доступ к переменной --- varA._A__x
# print(varA._A__x)


# # 9.6. ЧТО ТАКОЕ SELF

# class ProgStaff:
#     companyName = 'ProgrammingLab'
#     def __init__(self, pSalary):
#         self.salary = pSalary
    
#     def printInfo(self):
#         print("Company name is", ProgStaff.companyName)
#         print("Salary is", self.salary)
# peter = ProgStaff(2500)
# john = ProgStaff(2000)
# peter.printInfo()
# john.printInfo()

# print('-----------------------')
# ProgStaff.companyName = 'ProgrammingSchool'
# print(peter.companyName)
# print(john.companyName)

# print('-----------------------')
# peter.salary = 2700
# print(peter.salary)
# print(john. salary)

# print('-----------------------')
# john.printInfo()
# # Оба метода выдают одинаковый результат
# ProgStaff.printInfo(john)


# 9.7. МЕТОДЫ КЛАССА И СТАТИЧЕСКИЕ МЕТОДЫ
# Методы класса и статические методы используются не так часто. В большинстве случаев для класса Python
# вполне хватает методов экземпляров.
# class MethodDemo:
#     a = 1
#     @classmethod
#     def classM(cls):
#         print("Class Method. cls.a = ", cls.a)
#     @staticmethod
#     def staticM():
#         print("Static method")

# # чтобы вызвать classM() в приведенном примере, можно использовать следующее выражение:
# MethodDemo.classM()
# # Также можно создать объект MethodDemo и использовать его для вызова метода, как показано ниже:
# print('-----------------------')
# md1 = MethodDemo()
# MethodDemo.a = 10
# md1.classM()

# # Чтобы вызвать статический метод, можно указать либо имя класса, либо имя экземпляра.
# print('-----------------------')
# md1.staticM()
# # или
# print('-----------------------')
# MethodDemo.staticM()


# class SomeClass:
#     def __init__(self):
#         print('This is SomeClass')
#     def someMethod(self, a):
#         print('The value of a is', a)
#         self.b = 5
#     class SomeOtherClass:
#         def __init__(self):
#             print('This is SomeOtherClass')


# sc = SomeClass()
# sc.someMethod(100)
# sc.SomeOtherClass()

















