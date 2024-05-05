
# Program 1: Check if a number is positive or negative. 
# python
# num = float(input("Enter a number: ")) # 1                          #-1                                  #0

# if num > 0:                             # 1.0>0= True              #-1 >0= False                        #0 >0= False
#     print("The number is positive.")    # The number is positive.
# elif num < 0:                                                                                           # 0 <0 = False
#     print("The number is negative.")                               # This number is neagative
# else:
#     print("The number is zero.")                                                                        # The number is zero


# # 2.Determine if a year is a leap year.
# year = int(input("Enter a year: "))                        #here year is the variable and the input string is converted into int 2024

# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): # False and (True)
#     print("It is a leap year.")                            #  so it will print as leap year
# else:                                                      # the if condition is false it will print else stmt as not a leap year.
#     print("It is not a leap year.")    


# # Program 3: Check if a number is even or odd.
# python
# num = int(input("Enter a number: "))   #2               #1

# if num % 2 == 0:                        # True          #1%2=1==0- False
#     print("The number is even.")  
# else:
#     print("The number is odd.")         


# Program 4: Determine the largest of three numbers.
# python
# num1 = float(input("Enter the first number: "))             # 10.5                  10.0               10.0                 10.0
# num2 = float(input("Enter the second number: "))            # 10.1                  10.5               10.1                10.0
# num3 = float(input("Enter the third number: "))             # 10.0                  10.1               10.5                10.0

# if num1 > num2 and num1 > num3:                           # True                   False                                  True
#     print("The first number is the largest.",num1)               #print
# elif num2 > num1 and num2 > num3:                                                 #True
#     print("The second number is the largest.",num2)
# elif num1==num2 and num2== num3:                                 # a==b b== c c==a
#     print("All three numbers are equal")                                     # print
# else:
#     print("The third number is the largest.", num3)                                                     #print



# # Program 5: Check if a character is a vowel or consonant.
# # python
# char = input("Enter a character: ")                 #I

# if char.lower() in 'aeiou':                         # A in 'aeiou'   = False        
#     print("The character is a vowel.")
# else:
#     print("The character is a consonant.")          #The character




# # Example 1: Determine the grade based on a percentage score range.
# # python
# percentage = float(input("Enter the percentage score: "))  # 70

# if percentage >= 90:
#     grade = "A"
# else:
#     if percentage >= 80:
#         grade = "B"
#     else:
#         if percentage >= 70:
#             grade = "C"
#         else:
#             if percentage >= 60:
#                 grade = "D"
#             else:
#                 grade = "F"
#             print("1")
#             print("4")
#         print("2")
#         print("5")
#     print("3")
#     print("6")

# print("The grade is:", grade)



# #Example 2: Categorize a number into different ranges.
# #python
# num = int(input("Enter a number: ")) # here num is the variable and the input string is converted into int and give your input integer

# if num >= 0: # here num is the variable and is >=0                            #51 >= 0   101 >=0   -1 >= 0
#     if num <= 50:    #and <=50 then go to line 16 and print Low Category      #51 <= 50  101<=50
#         category = "Low"
#     else: # the above range doesnt meet then go to line 9
#         if num <= 100: # here num is the variable and is >=51 and <=100 then go to line 16 and print Medium Category   101<=100
#             category = "Medium"
#         else:
#             category = "High"  # here if the value and is >=101 then go to line 16 and print High Category
#         print("1")
# else:
#     category = "Negative" # here if the value and is -1 or below then go to line 16 and print Negative Category

# print("The number belongs to the", category, "category.") #print function prints the category


# Example 3: Classify a character based on its type.
# # python
# char = input("Enter a character: ")                # R                                 #r  #1   @ #1a

# if char.isalpha():                                  # "1".isalpah()= False                   
#     if char.islower():                              # "r".islower()= True
#         category = "Lowercase Letter"
#     else:
#         category = "Uppercase Letter"               # catergory="uppercase letter"
#     print("1")
# else:
#     if char.isdigit():                              #"1".isdigit()=True
#         category = "Digit"
#     elif char.isalnum():
#         category = "alpha-numeric"
#     else:
#         category = "Special Character"
#     print("2")
# print("The character is a", category)


# # Example 4: Determine the type of triangle based on side lengths using multiple conditions.
# # python
# side1 = float(input("Enter the length of side 1: "))            #10   10            5
# side2 = float(input("Enter the length of side 2: "))            #10    20           4
# side3 = float(input("Enter the length of side 3: "))            #10    10          3

# if side1 == side2 == side3:                         # side1== side2 and side2==side3 and side3== side1
#     triangle_type = "Equilateral Triangle"
# elif side1 == side2 or side1 == side3 or side2 == side3:      # False or False or False
#     triangle_type = "Isosceles Triangle"
# else:
#     if side1**2 == side2**2 + side3**2 or side2**2 == side1**2 + side3**2 or side3**2 == side1**2 + side2**2:  #False or False or True
#         triangle_type = "Right-angled Triangle"
#     else:
#         triangle_type = "Scalene Triangle"

# print("The triangle is a", triangle_type)


# Example 5: Classify a number into positive, negative, or zero, and then further categorize positive numbers.
# # # python
# num = float(input("Enter a number: "))                              #10.0

# if num > 0:
#     if num < 10:
#         category = "Single Digit Positive Number"
#     else:
#         if num < 100:
#             category = "Two-digit Positive Number"
#         else:
#             category = "Positive Number"
#         print("1")
#     print("2")        
# elif num < 0:
#     category = "Negative Number"
# else:
#     category = "Zero"

# print("The number belongs to the", category, "category.")

# import os

# def new_user(): 
#     confirm = "N" 
#     while confirm != "Y": 
#         username = input("Enter the name of the user to add: ") 
#         print("Use the username '" + username + "'? (Y/N)") 
#         confirm = input().upper()
#     os.system("sudo adduser " + username)

