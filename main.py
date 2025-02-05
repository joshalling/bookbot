with open("./books/frankenstein.txt") as f:
  file_contents = f.read()
  
words = file_contents.split()
character_count = {}
for letter in file_contents:
  letter = letter.lower()
  if letter in character_count:
    character_count[letter] += 1
  else:
    character_count[letter] = 1

print(character_count)