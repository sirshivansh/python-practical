def count_lines_words_characters(filename):
    lines = 0
    words = 0
    characters = 0

    with open(filename, 'r') as file:
        for line in file:
            lines += 1
            words += len(line.split())
            characters += len(line.replace(" ",""))
        return lines, words, characters
    
filename = r'C:\Users\sirsh\OneDrive\Desktop\PYTHON-PRACTICALS-SEM4\xyz.txt'
lines, words, characters = count_lines_words_characters(filename)

print(f"Number of lines : {lines}")
print(f"Number of Words : {words}")
print(f"Number of Characters : {characters}")