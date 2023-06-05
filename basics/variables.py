x = 5
y = "John"
print(x)
print(y,"\n")

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x,"\n")

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z,"\n\n")
x = 5
y = "John"
print(type(x))
print(type(y),"\n\n")

x, y, z = "Orange", "Banana", "Cherry"
print(x," ",y," ",z,"\n")
x = y = z = "Orange"
print(x)
print(y)
print(z,"\n")

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

""" Python Stings
"""
print("Hello World is assigned to a varialbe")


a = " Hello, World! "
print('Length of \'Hello World\' is ' ,len(a),"\n\n")
print("It is easy to automatically pull characters from a string such as 'Hello, World'")
for x in a:
    print(x)
    
print("\n")

print("You can easily check to see if there is text in a string with 'text in string'\n")
print("It implies an if\n")
print("It is", "Hello" in a," that Hello is in a")
print("It is", "hello" in a," that hello is in a\n")

print("Slicking Strings")
print("The syntax is [x:y] which means get the of the text starting at x up to but not including y")
print("a[2:5] of Hello, World")
print(a[2:5],"\n\n")
print("Get characters from beggining up to 5 with a[:5]")
print(a[:5],"\n")
print("You can also make a string upper/lower with <var>.lower etc")
print(a.lower()," ",a.upper(),"\n")
print("If you want to remove white spaces from begin or end use <var>(strip())")
print("A with white spaces:",a,":A without white spaces:"+ a.strip()+":\n")
