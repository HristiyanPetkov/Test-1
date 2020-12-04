# Exercise 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

def is_equal(a, b, c):
    a = a % 10
    b = b % 10
    c = c % 10
    
    ab = (a*b)
    
    ab = ab % 10
    
    if c == ab:
        return True
    else:
        return False
print(num1, num2, num3, '->', is_equal(num1, num2, num3))

print()

# Exercise 2

speed = int(input("Enter the max speed: "))
distance = int(input("Enter distance: "))

time1 = distance / speed
speed = speed + 15
time2 = distance / speed

time2 = time1 - time2
time2 = 60 * time2

print(speed, distance, '->', round(time2), 'minutes')
