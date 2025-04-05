s = "Shivansh Mishra"
s1 = "Roll Number 2 SE B COMPS"

print ( s +" "+ s1) #Concatenation
print("Roll 02 "*3) #repetition
print(s[1]) #Indexing
print(s[0:5]) #Slicing

print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.title())
print(s.find("e")) #returns occurance of first occurance, or -1 if not found
print(s.count("i"))
print(s.startswith("Sh"))
print(s.endswith("ra"))
print(len(s))

str= "Shivansh02"
print(str.isalnum()) #returns true if all characters are alphaneumeric
print(str.isdigit()) #returns true if all characters are digits
print(str.isalpha()) #returns true is all characters are alphaneumeric
print(str.isspace()) #returns true if all characters are whitespaces

string= " banana "
print(string.strip())
print(string.replace("a","o"))

words = "apple, banana, cherry"
print(words.split(" "))
words = ['apple', 'mango', 'cherry']
print(",".join(words))
