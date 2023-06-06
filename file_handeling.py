# file_handeling.py
# f= open('example.txt', 'r')

# f.close()

# # Reading lines from a file and printing them
# with open('example.txt', 'r') as file:
#     for line in file:
#         # print("naseer")
#         print(line.strip())

# # Writing lines to a file
# lines = ['This is line 1', 'This is line 2', 'This is line 3']
# with open('output.txt', 'w') as file:
#     for line in lines:
#         file.write(line + '\n')

# Counting the number of words in a file
with open('example.txt', 'r') as file:
    word_count = 0
    for line in file:                          # for "This file is for testing purposes." in file:
        words = line.split()                  #  words=["This", "file", "is", 'for', "testing", "purposes."]
        word_count += len(words)              # word_count= word_count + len(words)= 4 + 6=10
print(f"Total words: {word_count}")



# Copying content from one file to another
# with open('example.txt', 'r') as source_file, open('example_copy.txt', 'w') as destination_file:
#     for line in source_file:
#         destination_file.write(line)
#         destination_file.write("naseer\n")

# s= open('example.txt', 'r')
# d=open('example_copy.txt', 'w')

# for line in s:
#     d.write(line)
#     d.write("Rahima \n")

# s.close()
# d.close()
# import csv

# # Reading from a CSV file and writing selected rows to another CSV file
# with open('example5.csv', 'r') as input_file, open('example5_copy.csv', 'w', newline='') as output_file:
#     reader = csv.reader(input_file)
#     writer = csv.writer(output_file)
#     for row in reader:
#         if row[0] == 'Error':
#             writer.writerow(row)
