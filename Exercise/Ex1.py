import datetime
now = datetime.datetime.now()
name = input("Name:")
year = now.year
age = 100 - int(input("Age:"))

print("Name:" + name + "\n Year: " + str(year + age))