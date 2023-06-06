# fruits = ["apple", "banana", "cherry","mango"]
# for x in fruits:
#     print("inside loop")
#     print(x)
#     if x == "cherry":
#         break
#         print(x)
        

#     print(x)
#     print(x)



# print("outside of loop")

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     print(x)
#     #continue #go to for loop
    
#   print(x) 

#   str()
#   int()
#   print()
#   list()
#   dict()
#   float()
#   bool()
#   input()
#   range()



# for x in range(6):
#   if x == 3: 
#     break
#   print(x)
# else:
#   print("Finally finished!")

# print("outside loop")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:               #red                                         #big                                   # tasty
#   for y in fruits:          #apple     banana      cherry                #apple       banana      cherry        #apple          banana          cherry
#     print(x, y)             #red apple red banana  red cherry            #big apple   big banana  big cherry    #tasty apple    tasty banana    tasty cherry





# for x in [0, 1, 2]:
#     pass

# print("naseer") 

# myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# for x in myMixedTypeList:
#     print(type(x), x)
# import random
# number = random.randint(1,10)  #4
# print(number)
# isGuessRight = False

# while isGuessRight != True:
#     guess = input("Guess a number between 1 and 10: ")  #4
#     if int(guess) == number:
#         print("You guessed {}. That is correct! You win!".format(guess))
#         isGuessRight = True
#     else:
#         print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
#     print("while loop")


# def sumf(a,b):
#   print("Hello from a function")
#   c=a+b
#   return c


# x=10
# y=20

# total=sumf(x,y)


# print(total)

# x=x*10
# y=y*10

# total=sumf(x,y)

# print(total)


# my_function()


# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function("Emil", "Tobias", "Linus")
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")




# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1) # 3+(3)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(3)


# # Calculate the Area of a Circle:
# radius = float(input("Enter the radius of the circle: "))
# area = 3.14159 * radius * radius
# print("The area of the circle is:", area)

# #Convert Celsius to Fahrenheit:
# # (0°C × 9/5) + 32 = 32°F

# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print("Temperature in Fahrenheit:", fahrenheit)


# Check if a Number is Even or Odd:
# num % 2 == 0 is even
# num % 2 == 1 is odd

# # if True:
# #     print("only if statment is true")
# #     print("this line is also belongs to if")
# # else:
# #     print("print only if statment is false")
# #     print("this line is belongs to else")

# number = int(input("Enter a number: "))
# if number % 2 == 1:
#     print("The number is odd.")
# else:
#     print("The number is even.")


# # Find the Maximum of Two Numbers:
# num1=int(input("enter a number1:"))
# num2=int(input("Enter number2:"))
# if num1>num2:
#     print(" {} is maximum".format(num1))
# elif num1<num2:
#     print(" {} is maximum ".format(num2))
# else:
#     print(" {} is equal {}".format(num1,num2))
# def maxfun(a,b):
#     if a>b:
#         return a
#     elif a<b:
#         return b
  


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# maximum = maxfun(num1, num2)
# print("The maximum number is:", maximum)

# num1=num1*10
# num2=num2+5
# maximum = maxfun(num1, num2)
# print("The maximum number is:", maximum)

# fruits=["apple","banna","cherry","orange"]
# fruits[0]
# fruits[0:2]
# fruits[1:4]
# fruits[1:]
# fruits[:2]
# fruits[:]
# fruits[::-1]

# strng="naseer"
# strng[0]

# strng[:]


# print(strng)
# print(strng[:])
# string = input("Enter a string: ")

# reversed_string = string[::-1]
# print("Reversed string:", reversed_string)


# 22 =2+2=4
# number = int(input("Enter a number: ")) #22
# sum_of_digits = 0
# while number > 0:
#     digit = number % 10                            # digit=2%10=2
#     sum_of_digits += digit                          # sum_of_digits= sum_of_digits+digit   2+2=4                 # 
#     number //= 10                                   # number= 2//10=0
# print("The sum of digits is:", sum_of_digits)


# x = 10
# if x > 0:
#     print("x is positive.")
#     print("x is positive.")
# elif x >5:
#     print("this is elif statment")
# else:
#     print("x is not positive.")

# print("End of the code.")

# x = 10
# if x > 0:
#     print("x is positive.")
#     if x > 5:
#         print("x is greater than 5.")
#     elif x == 5:
#         print("x is equal to 5.")
#     else:
#         print("x is less than 5.")
    
#     print("out if statment code")
# else:
#     print("x is not positive.")
# print("End of the code.")



# def my_function(fname,fname1,fname3):
#     print(fname + " mohammed")

# my_function("naseer","rahim","zuber") #naseer mohammed
# # my_function("Rahim")  #Rahim mohammed
# # my_function("zuber")  #zuber mohammed


# def my_function(*kids):             # kids=("Rahima","rahim")
#   for i in kids:                    # for i in ("Rahima","rahim"), i=NULL 
#     print( i + " mohammed")            #1 Rahima mohammed #2 Rahim mohmmed
                                    


# a= int(input("enter age number:")) # 29
# if a>30:                           #False
#   my_function("naseer","zuber")
# elif a <30 and a >25:               # True              
#   my_function("Rahima","Rahim")        #go to line 254
# else:
#   my_function("anwar")



def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

# my_function("Naseer", "Rahim",  "anwar")
my_function(child1 = "Naseer", child2 = "Rahim", child3 = "anwar")


