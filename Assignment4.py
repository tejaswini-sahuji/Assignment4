#file reading and error handling
#task1
#reading sample file and print data if file is exist otherwise gives error
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File content:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Main execution
read_file('sample.txt')

'''
describe above def function
Tries to open a file in read ('r') mode.
If the file exists, it prints each line after stripping leading/trailing whitespace (line.strip()).
If the file does not exist, it catches the FileNotFoundError and shows a user-friendly error message.
'''

#task2
#Write a file and append data in existing file and again read the file for showing appended data
def write_file(filename):
    write1 = input("Enter the content:")
    with open(filename, 'w') as file:
        file.write(write1 + "\n")
    print("data enter successfully")

'''
 What it does:
Takes input from the user.
Opens the file in write mode ('w') — this overwrites the file.
Writes the input content with a newline.
Confirms the success message.
'''

def append_data(filename):
    append1 = input("Enter your data:")
    with open(filename, 'a') as file:
        file.write(append1 + "\n")
    print("data append successfully")
'''
Takes input from the user.
Opens the file in append mode ('a') — this adds data at the end.
Writes the input followed by a newline.
Confirms that data was appended.
'''

def readfile(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())
'''
Opens the file in read mode.
Prints each line after removing leading/trailing whitespace using strip().
'''

filename = "Output.txt"    
write_file(filename)       # Step 1: Write initial content from user input 
append_data(filename)      # Step 2: Append new content from user input
readfile(filename)         # Step 3: Display full content of the file



