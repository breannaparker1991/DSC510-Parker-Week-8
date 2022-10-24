import json

gba_file = open('Gettysburg.txt', 'r')
gba_dict = {}

def add_word():
  for word in gba_file:
    gba_dict.append(word)
  print(gba_dict)

add_word()

def main(): 
  for line in gba_file:
    pass


# with open('Gettysburg.txt') as f:
#   data = json.load(f)

# for word in data:
#   print(word)