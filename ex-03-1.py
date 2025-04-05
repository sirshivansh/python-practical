#Python program to Append Data to existing File and then display the entire file

file_name = r'C:\Users\sirsh\OneDrive\Desktop\PYTHON-PRACTICALS-SEM4\xyz.txt'
#appending Data to the file
with open(file_name, 'a') as file:
    file.write('\nThis is New Data Appended to the file.')

#reading and displaying entire file
with open(file_name, 'r') as file:
    content = file.read()
    print(content)