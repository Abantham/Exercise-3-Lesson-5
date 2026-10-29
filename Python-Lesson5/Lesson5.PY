def greet() :

    print("Hello,World")

greet()



def personalized_greeting(Adrian):
    print(f"Hello, Adrian! Hope you are having a great day.")

personalized_greeting("Adrian")


def square(number):
    return number **2


result = square(5)

print(result)




def rectangle_area(length, width):  
    return length * width

result = rectangle_area(5, 10)

print(result)




def apply_operation(func, number):
 return func(number)

def double(number):
   return number * 2 

def square(number):
   return number ** 2


result1 = apply_operation(double, 7)
print (result1)

result2 = apply_operation(square, 3)
print(result2)   