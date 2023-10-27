
# YOUR CODE HERE - write code to open letter.txt in read mode 'r'

f = 

# YOUR CODE HERE - write code to read the contents of letter.txt using f.readlines() in the variable lines

lines = 

# For loop to remove the \n from the lines read
cleaned_lines = []
for line in lines:
    cleaned_lines.append(line.rstrip('\n'))

print(cleaned_lines)

# YOUR CODE HERE - write code to close the file using f.close()
