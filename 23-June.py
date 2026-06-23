#1
class Ticket:
    def __init__(self, movie, seats_available, seats_requested):
        self.movie = movie
        self.seats_available = seats_available
        self.seats_requested = seats_requested
        self.confirmed_seats = min(seats_available, seats_requested)

        if seats_requested <= seats_available:
            self.message = "Full request confirmed"
        else:
            self.message = "Only partial seats confirmed"

    def display(self):
        print("Movie:", self.movie)
        print("Seats Requested:", self.seats_requested)
        print("Seats Confirmed:", self.confirmed_seats)
        print("Status:", self.message)
        print()


t1 = Ticket("Avengers", 50, 20)
t2 = Ticket("Batman", 10, 15)
t3 = Ticket("Superman", 30, 30)

t1.display()
t2.display()
t3.display()

#2
class Employee:
    def __init__(self, name, department="General", bonus=0):
        self.name = name
        self.department = department
        self.bonus = bonus

    def annual_summary(self):
        total_pay = 30000 + self.bonus
        print("Name:", self.name)
        print("Department:", self.department)
        print("Bonus:", self.bonus)
        print("Total Pay:", total_pay)
        print()


e1 = Employee("Mohit", "IT", 5000)
e2 = Employee("Yaksh", "HR")
e3 = Employee("Akshat")

e1.annual_summary()
e2.annual_summary()
e3.annual_summary()

#3

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
items = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 10),
    ("Keyboard", 1000, 5)
]

products = []

for name, price, quantity in items:
    products.append(Product(name, price, quantity))

grand_total = 0

for p in products:
    value = p.total_value()
    grand_total += value
    print("Product:", p.name)
    print("Price:", p.price)
    print("Quantity:", p.quantity)
    print("Total Value:", value)
    print()

print("Total Inventory Value:", grand_total)