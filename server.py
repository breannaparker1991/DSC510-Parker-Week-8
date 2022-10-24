import json

gba_file = open('Gettysburg.txt', 'r')
gba_dict = {}

def add_word():
  for word in gba_file:
    if word in gba_dict:
      gba_dict[word] +=1
    else:
      gba_dict[word] = 1
  print(gba_dict)

add_word()

def main(): 
  for line in gba_file:
    pass


# with open('Gettysburg.txt') as f:
#   data = json.load(f)

# for word in data:
#   print(word)