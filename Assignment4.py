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

#task2
#Write a file and append data in existing file and again read the file for showing appended data
def write_file(filename):
    write1 = input("Enter the content:")
    with open(filename, 'w') as file:
        file.write(write1 + "\n")
    print("data enter successfully")

def append_data(filename):
    append1 = input("Enter your data:")
    with open(filename, 'a') as file:
        file.write(append1 + "\n")
    print("data append successfully")

def readfile(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())
filename = "Output.txt"
write_file(filename)
append_data(filename)
readfile(filename)