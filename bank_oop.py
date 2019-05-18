class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def __str__(self):
        return "The current interest rate is {}% and balance is ${}".format(self.interest_rate, self.balance)
        
    def deposit(self, amount):
        self.amount = float(amount)
        self.balance += self.amount
        print("New balance is ${}".format(self.balance))
    
    def withdraw(self, amount):
        self.amount = float(amount)
        self.balance -= self.amount
        print("New balance is ${}".format(self.balance))

    def gain_interest(self):
        self.balance = (1 + self.interest_rate/100)*self.balance
        print("New balance is ${:.2f}".format(self.balance))


test = BankAccount(15, 2.5)
print(test)
test.deposit(5)
test.withdraw(5)
test.gain_interest()
# print(test)



























# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = int(age)
#         # this is passed into the constructor or instantiator
    
#     def introduce(self):
#         print("Hello my name is {} and I am {} years old".format(self.name, self.age))
    
# james = Person('James', '12')
# print(james.age)
# print(james.introduce())

# # class Recipe:
# #     def __init__(self, title, description, mins, veg):
# #         self.title = title
# #         self.description = description
# #         self.mins = int(mins)
# #         self.veg = veg

    
