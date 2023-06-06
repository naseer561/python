# 1. Iterate over a list and print each element.

# fruits = ["apple", "banana", "cherry"]   # list is the datatype for the items fruits

# for fruit in fruits:                     # fruit is the variable which will iterate over the list of items given in the above variable fruits
#     print(fruit)                         # eg: for fruit(apple) in fruits will go in the sequence it will print in the output, similarly for banana and cherry.
    
    
# 2.Iterate over a string and count the number of vowels.

# word = "Hello,World !"                # String is the datatype for the given variable word

# vowels = "aeiou"                
# count = 0                       

# for char in word:               
#     if char.lower() in vowels:  
#         count += 1                  # count=1   # count = 3  

# print("Number of vowels:", count)  #once all the elements are calculated in sequence it will print the count in the output.
 
# Example 3: Iterate over a range of numbers and calculate their sum.

# start = 1                                  
# end = 10
# sum = 0

# for num in range(start, end+1):   # Start =1 ,End =10+1  range(1, 11)  from left it is inclusive and from right it is exclusive.
#     sum += num                     # sum=0, num is the variable sum+=num(1-10 is the range)it will iterate until the end of the range and calculates the sum.
#                                     # 1 sum= 1  sum = 3   sum=10
# print("Sum of numbers from", start, "to", end, "is", sum)  #once it completes will print the given statement in the output.

# # Example 4: Iterate over a dictionary and print key-value pairs.
# student_scores = {"John": 85, "Emma": 92, "Ryan": 78,"naseer":91}   # Dictionary is the datatype for the given variable student_scores
#fvnqhlcgshlvealylvcgergffytpktgiveqcctsicslyqlenycn
# count=0
# names=[]
# namestr=""
# for x,y in student_scores.items():   # items(), keys(), values()           #name,score are the variables in dictionary items and each element will iterate in sequence.
#     if y > 90:
#         names.append(x)
#         count+=1

#                             #eg: John scored 85 similarly for emma and Ryan.
# print("student's  count who scored more than 90:",count)
# print("studnet names who scored more than 90:", names)
# print(namestr)

# # 5.Iterate over a string and reverse its order.

# text = "Hello, World!"                         # text variable is stored by value string "Hello World!"
# reversed_text = "".join(reversed(text))                            #reversed_text="" is a funtion to reverse() the given string 

# # for char in text:                              # char is the variable in text(Hello , World!) the reversed function will itrate for each element and reverse the text.
# #     reversed_text = char + reversed_text       # reversed_text=H, reversed_text=eh,reversed_text= !dlroW ,olleH
# print("original text:", text)  
# print("Reversed text:", reversed_text)         #once all the elements are reversed in sequence it will print this statement in the output.
# print("Reversed text:", text[::-1])

# Example 1: Iterate over dictionary keys and print them.

# student_scores = {"John": 85, "Emma": 92, "Ryan": 78}



# for name in student_scores:
#     print(student_scores[name])


# Example 2: Iterate over dictionary values and calculate their average.

# student_scores = {"John": 85, "Emma": 92, "Ryan": 78}
# total_score = 0
# num_students = len(student_scores)                         # num_students=3

# for score in student_scores.values():                       # 85 in 
#     total_score += score                                    # total_score=0+85,I2:85+92=177, I3: 177+78=255

# average_score = total_score / num_students            # 255/3= 85
# print("Average score:", average_score)               


# # Example 3: Iterate over dictionary items and display key-value pairs.

# student_scores = {"John": 85, "Emma": 92, "Ryan": 78}

# for name, score in student_scores.items():     #  for name,score in [(john,84),(Emma,92),(Ryan,78)]
#     print(name, "scored", score)                 # john scored 85


# Example 4: Count the number of occurrences of each character in a string using a dictionary.

# text = "Hello, World!"
# char_counts = {}

# for char in text:
#     if char in char_counts:
#         char_counts[char] += 1
#     else:
#         char_counts[char] = 1

# for char, count in char_counts.items():
    # print(char, ":", count)



# Example 5: Filter and create a new dictionary based on certain conditions.

# student_scores = {"John": 85, "Emma": 92, "Ryan": 78, "Emily": 90}

# passing_scores = {}

# for name, score in student_scores.items():   # name=Emily , score=90
#     if score >= 80:                          # True
#         passing_scores[name] = score         # {'John':85,'Emma':92,'Emily':90 }


# for name,score in passing_scores.items():
#     print(name, ': ', score)
# # print("Passing scores:", passing_scores)     #"Passing scores: {'John':85,'Emma':92,'Emily':90 }

# 1.
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)

# # 2. For Loop with a Dictionary:
#     # Iterating over a dictionary
# student_grades = {"John": 85, "Emily": 92, "Ryan": 78}
# for name, grade in student_grades.items():
#     print(f"{name}: {grade}")
#     # print(f" {name}: {grade}")


# 3.For Loop with Enumerate:
# # Enumerating a list
# fruits = ["apple", "banana", "orange"]
# for index, fruit in enumerate(fruits):
#     if index !=0:                                   #0!=0 False
#         print(f"Index: {index}, Fruit: {fruit}")    #


# 4.Nested For Loop:
# Nested for loop
# colors = ["red", "green", "blue"]
# sizes = ["small", "medium", "large"]
# for color in colors:                             #for  "red" in ["red", "green", "blue"]
#     for size in sizes:
#         continue                                 # for "small" in  ["small", "medium", "large"]    
#         print(f"Color: {color}, Size: {size}")
#     print("hi")

# 5.For Loop with Break and Continue:
# Using break and continue in a loop
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num == 3:
#         break   # exit from for  inner loop
#     if num == 5:
#         continue  # go to for loop  inner again
#     print(num)


# # 1.Calculating Average Grades:
# # Calculating the average grade of students
# student_grades = {"John": [85, 90, 92], "Emily": [92, 88, 95], "Ryan": [78, 80, 82]}
# for name, grades in student_grades.items():      # for "Emly", [92, 88, 95] in student_grades.items()
#     total = sum(grades)                            # total=sum([85,90,92])=275
#     average = total / len(grades)                  # average= 275/3= 91
#     print(f"{name}: Average grade = {average} and total score={total}")   # John: average grade= 89
#     print(name,": Average grade =",average," and toatl score=",total)



# # 2.Filtering Even Numbers:
# # Filtering even numbers from a list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

# 3.Counting Letter Frequency:
# Counting the frequency of each letter in a string
# text = "Hello, World!"                        #
# letter_frequency = {}                     
# for char in text:                                                  # for "," in "Hello, World!"
#     if char.isalpha():                                                 # if  ",".isalpha()= False:
#         char = char.lower()                                               #  char="l"
#         letter_frequency[char] = letter_frequency.get(char, 0) + 1        #  letter_frequence["l"]= 2 = {h:1,e:1,l:2}
#                                                                            #{h:1,e:1,l:1}

# print(letter_frequency)


# Example 4: Count the number of occurrences of each character in a string using a dictionary.#

# text= ["Hello, World!", " naseer"]
# text = "Hello, World!"
# char_counts = {}

# for char in text:
#     if char in char_counts:
#         char_counts[char] += 1
#     else:
#         char_counts[char] = 1

# for char, count in char_counts.items():
    # print(char, ":", count)



# # 4.Matrix Transposition:
# # Transposing a matrix using nested for loops
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# for row in transposed_matrix:
#     print(row)


# # Example matrix
# matrix = [  [1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]  ]                # matrix[0][1] =2    matrix[1][2]=6   matrix[2][1]=8  matrix[0][2]=3
# # matrix = [  [1, 2, 3],  [4, 5, 6],   [7, 8, 9]  ]   matrix[0]=[1, 2, 3]               , matrix[1]=[4, 5, 6]  , matrix[2]=[7, 8, 9]
#                                                       # a=[1, 2, 3]#  matrix[0][0]=1              , matrix[1][0]=4      , matrix[2][0]=7  
# # Get the dimensions of the matrix                                    matrix[r][c]
# rows = len(matrix)                                  # rows= 3
# cols = len(matrix[0])                               # cols= 3 

# # Create a new matrix for the transpose                          1,2,3   4,5,6,  7,8,9
# transpose = [[0 for _ in range(rows)] for _ in range(cols)]  # [[1,0,0],[2,0,0],[3,0,0]]

# # Perform matrix transposition
# for i in range(rows):                                #  for 0 in 0,1,2:                i=0
#     for j in range(cols):                            #           for 1 in 0,1,2:       j=2
#         transpose[j][i] = matrix[i][j]               #                   transpose[2][0]= matrix[0][2] =3

# # Print the original matrix
# print("Original matrix:")
# for row in matrix:   # [  [1, 2, 3],  [4, 5, 6],   [7, 8, 9]  ] 
#     print(row)

# # Print the transposed matrix
# print("Transposed matrix:")
# for row in transpose:
#     print(row)





# Certainly! Here are five programs that involve lists, dictionaries, for loops, and if statements:

# 1. Filtering Even Numbers:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:                       
#         even_numbers.append(num)             #[2,4,6,8,10]
# print(even_numbers)

# # Creating a dictionary
# student = {'name': 'John', 'age': 20, 'major': 'Computer Science'}

# # Accessing dictionary values
# print(student['name'])  # Output: John

# # Modifying dictionary values
# student['age'] = 21
# print(student)  # Output: {'name': 'John', 'age': ,21 'major': 'Computer Science'}

# # Adding a new key-value pair
# student['gpa'] = 3.8
# print(student)  # Output: {'name': 'John', 'age': 21, 'major': 'Computer Science', 'gpa': 3.8}

# # Removing a key-value pair
# del student['major']
# print(student)  # Output: {'name': 'John', 'age': 21, 'gpa': 3.8}


# 2. Counting Letter Frequency:
#    ```python
# text = "Hello, World!"
# letter_frequency = {}
# for char in text:                                # for ',' in "Hello, World!"
#     if char.isalpha():                             #  if ','.isalpha(): False 
#         char = char.lower()                             # char='o'
#         if char in letter_frequency:                    # if 'l' in {'h':1,'e':1,'l':1}: True 
#             letter_frequency[char] += 1                      # a+=1  a=a+1   letter_frequency['l']=  2  {'h':1,'e':1,'l':2}
#         else:
#             letter_frequency[char] = 1                  #letter_frequencey['l]=1  {'h':1,'e':1,'l':2,'o':1}
# print(letter_frequency)

#    ```

# 3. Calculating Average Grades:
# student_grades = {"John": [85, 90, 92], "Emily": [92, 88, 95], "Ryan": [78, 80, 82]}
# for name, grades in student_grades.items():                                 #for "Emily", [92, 88, 95] in student_grades.items():   
#     total = sum(grades)                                                     # total=sum([92, 88, 95])=267
#     average = total / len(grades)                                           #average=267/3=91.6
#     if average >= 90:                                                       # if 91 >=90:
#         print(f"{name} has an average grade of {average}. Excellent!")
#     elif average >= 80:                                                         # elif 80 >= 80: True
#         print(f"{name} has an average grade of {average}. Good job!")           # print
#     else:
#         print(f"{name} has an average grade of {average}. Keep up the effort!") 


# 4. Finding Maximum Number:
#    ```python
# numbers = [5, 8, 3, 9, 2, 11, 6]
# max_number = numbers[0]                          # max_number= 5
# for num in numbers:                              # for 11 in [5, 8, 3, 9, 2, 11, 6]
#     if num > max_number:                            # if 6  > 11: F
#         max_number = num                                #max_number=11
        
# print(f"The maximum number is: {max_number}")

#    ```

# 5. Grouping Names by First Letter:
#    ```python
# names = ["Alice", "Bob", "Charlie", "Alex", "David", "Dad", "Bhai"]
# name_groups = {}                
# for name in names:                                 # for "Bhai" in ["Alice", "Bob", "Charlie", "Alex", "David", "Dad", "Bhai"]
#     first_letter = name[0]                                  #first_letter="B"
#     if first_letter in name_groups:                         # if "B" in {"A":["Alice","Alex"],"B":["Bob","Bhai"],"C":["Charlie"],"D":["David","Dad"]}:  T
#         name_groups[first_letter].append(name)                    #["Bob"].append("Bhai")  == ["Bob", "Bhai"]
#     else:                                                   #Else:
#         name_groups[first_letter] = [name]                       # name_groupe["D"]= ["David"]
# print(name_groups)                                      #{"A":["Alice","Alex"],"B":["Bob","Bhai"],"C":["Charlie"],"D":["David","Dad"]}

# print(name_groups["B"])

#    ```

# These examples demonstrate the combined usage of lists, dictionaries, for loops, and if statements to perform various operations like filtering elements, counting frequencies, calculating averages, finding maximum values, and grouping names. Feel free to modify and customize these programs according to your needs and explore further possibilities with these fundamental programming constructs.




# Certainly! Here are five examples that involve functions, lists, and dictionaries in Python:

# Example 1: Calculating the average of a list of numbers using a function.
# ```python
def calculate_average(numbers):
    total = sum(numbers)                      #  total=sum([10, 20, 30, 40, 50])= 150
    average = total / len(numbers)             # average= 150/5 = 30
    return average                             # retrun 30

num_list = [10, 20, 30, 40, 50]
avg = calculate_average(num_list)     #   avg = calculate_average([10, 20, 30, 40, 50])= 30
print("Average:", avg)                      # print("Average:", 30)


# ```

# Example 2: Counting the frequency of words in a sentence using a dictionary and a function.
# ```python
# def count_word_frequency(sentence):   
#     word_frequency = {}                               
#     words = sentence.split()                            #words="I love programming and programming loves me".split()

#     for word in words:                                 #  for "loves" in ['I', 'love', 'programming', 'and', 'programming', 'loves', 'me']:
#         if word in word_frequency:                            #if "loves" in {"I":1,"Love":1,"programming":2,"and":1."loves":1}:      
#             word_frequency[word] += 1                               #word_frequency["programming"] = 1+ 1 =2    {"I":1,"Love":1,"programming":2,"and":1}
#         else:                                                  #else:
#             word_frequency[word] = 1                                #  word_frequency["loves"]=1    {"I":1,"Love":1,"programming":2,"and":1."loves":1,"me":1}

#     return word_frequency

# text = "I love programming and programming loves me"
# frequency_dict = count_word_frequency(text)  
# print("Word frequency:", frequency_dict)
# ```

# Example 3: Sorting a list of dictionaries based on a specific key using a function.
# ```python
# def sort_by_key(data_list, key):
#     sorted_list = sorted(data_list, key=lambda x: x[key]) # sorted_lis= sorted(data_list, score=lambda x:85)
#     return sorted_list
# x={"name": "John", "age": 20, "score": 85}
#  a=  x["score"]
# students = [
#     {"name": "John", "age": 20, "score": 85},
#     {"name": "Emma", "age": 22, "score": 92},
#     {"name": "Ryan", "age": 21, "score": 78}
# ]

# sorted_students = sort_by_key(students, "score")
# print("Sorted students:", sorted_students)
# ```

# Example 4: Removing duplicates from a list using a function.
# ```python
# def remove_duplicates(input_list):
#     unique_list = list(set(input_list))        # unique_list= [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     return unique_list

# numbers = [1, 2, 3, 2, 4, 5, 1, 3, 6, 7, 4, 8, 9]
# unique_numbers = remove_duplicates(numbers)       #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("Unique numbers:", unique_numbers)
# ```

# Example 5: Checking if a number is prime using a function and a dictionary.
# ```python
# def is_prime(number):                            #   
#     if number < 2:                               #  if 17 <2: False   
#         return False

#     for i in range(2, int(number ** 0.5) + 1):   # for 4 in range(2, 5):  2,3,4
#         if number % i == 0:                         #  if 17%4 == 0 : False
#             return False

#     return True

# num = 17
# result = is_prime(num) # =  True

# prime_dict = {num: result}
# print("Prime dictionary:", prime_dict)

# ```


# Example 6:Finds the minimum value in a list of numbers.
# def min_value(numbers):
#   """Finds the minimum value in a list of numbers."""
#   min_value = numbers[0]                  # min_value=2
#   for number in numbers:                   # for 1 in [2, 1, 3, 4, 5]:
#     if number < min_value:                      # if 1 < 2 :
#       min_value = number                            #min_value=1
#   return min_value

# numbers = [2, 1, 3, 4, 5]

# min_value = min_value(numbers)
# print(min_value)


# def max_value(numbers):
#   """Finds the minimum value in a list of numbers."""
#   max_value = numbers[0]                  # min_value=2
#   for number in numbers:                   # for 1 in [2, 1, 3, 4, 5]:
#     if number > max_value:                      # if 1 < 2 :
#       max_value = number                            #min_value=1
#   return max_value

# numbers = [2, 1, 3, 4, 5]

# max_value = max_value(numbers)
# print(max_value)


# Example 7:Finds all occurrences of a value in a list
# def find_all_occurrences(list, value):                    #  find_all_occurrences([1, 2, 3, 1, 2], 1)
#   """Finds all occurrences of a value in a list."""
#   occurrences = []
#   for index, item in enumerate(list):                     # for index, item in enumerate([1, 2, 3, 1, 2])
#     if item == value:                                          # if 1 == 1 :
#       occurrences.append(index)                                         # occurrences.append(3)  =  [0,3]
#   return occurrences

# list = [1, 2, 3, 1, 2]
# value = 1
# occurrences = find_all_occurrences(list, value)
# print(occurrences)



# 1. Matrix Multiplication:
#    ```python
# matrix1 = [[1, 2, 3], 
#            [4, 5, 6], 
#            [7, 8, 9]]
# matrix2 = [[10, 11, 12], 
#            [13, 14, 15], 
#            [16, 17, 18]]
# result = [[0, 0, 0], 
#           [0, 0, 0], 
#           [0, 0, 0]]

# # result = [[84, 90, 96], 
# #           [40, 0, 0], 
# #           [0, 0, 0]]
# for i in range(len(matrix1)):                               #for 1 in range(3): i=1
#     for j in range(len(matrix2[0])):                           #for  0 in range(3): j =2
#         for k in range(len(matrix2)):                              # for 0 in range(3): k =2
#             result[i][j] += matrix1[i][k] * matrix2[k][j]              #result[1][0]=result[1][0]+ matrix1[1][0] * matrix2[0][0]= 0+4*10=40
#     print("hi")
# print(result)

#    ```

# 2. Prime Number Checker:
#    ```python
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# num = 17
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

#    ```

# 3. Binary Search Algorithm:
#    ```python
#    def binary_search(arr, target):
#        low = 0
#        high = len(arr) - 1

#        while low <= high:
#            mid = (low + high) // 2
#            if arr[mid] == target:
#                return mid
#            elif arr[mid] < target:
#                low = mid + 1
#            else:
#                high = mid - 1

#        return -1

#    numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
#    target = 16
#    index = binary_search(numbers, target)
#    if index != -1:
#        print(f"{target} found at index {index}.")
#    else:
#        print(f"{target} not found in the list.")
#    ```

# 4. Recursive Factorial Calculation:
#    ```python
#    def factorial(n):
#        if n == 0 or n == 1:
#            return 1
#        else:
#            return n * factorial(n - 1)

#    num = 5
#    result = factorial(num)
#    print(f"The factorial of {num} is: {result}")
#    ```

# 5. Fibonacci Sequence with Memoization:
#    ```python
#    def fibonacci(n, memo={}):
#        if n in memo:
#            return memo[n]
#        elif n <= 2:
#            return 1
#        else:
#            result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
#            memo[n] = result
#            return result

#    num = 10
#    result = fibonacci(num)
#    print(f"The Fibonacci number at index {num} is: {result}")
#    ```
