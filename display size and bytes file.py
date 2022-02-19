file = open("myfile.txt", "r")

number_of_lines = 0
number_of_words = 0
number_of_characters = 0

for line in file:
  line = line.strip("\n")


  words = line.split()
  number_of_lines += 1
  number_of_words += len(words)
  number_of_characters += len(line)
  file_size_in_bytes = number_of_characters + len(line)+2

file.close()

print("lines:", number_of_lines)
print("words:", number_of_words)
print("characters:", number_of_characters)
print(file_size_in_bytes)