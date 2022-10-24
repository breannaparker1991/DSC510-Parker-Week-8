
import json

# gba_file = open('Gettysburg.txt')



with open('Gettysburg.txt', 'r') as file:
  data = file.read().splitlines()
gba_dict = dict()

def add_word():
  for word in data:
    if word in gba_dict:
      gba_dict[word] +=1
    else:
      gba_dict[word] = 1
  print(gba_dict)

def process_lines():
  for line in data:
    line = line.rstrip()
    line = line.translate(line.maketrans('','', data.punctuation))
    line = line.lower()
    words = line.split()
    add_word(data)
  print(process_lines)

process_lines()

def main(gba_dict):
  for key in gba_dict:
    print(key, gba_dict[key])
  
  
# def add_word():
#   with open("Gettysburg.txt") as f:
#     for line in f:
#       (key,val) = line.split()
#       gba_dict[int(key)] = val
#   print(gba_dict)


# def add_word():
#   for line in data:
#     word = line.split()
#     for w in word:
#       if word not in gba_dict:
#         gba_dict[word] = 1
#       else:
#         gba_dict[word] += 1
#   print(gba_dict)
  

# add_word()


# def process_line():
#   add_word()
#   for d in gba_dict:
#     d[] = d.replace

# def main(): 
#   for line in gba_file:
#     pass

  
# with open('Gettysburg.txt') as f:
#   data = json.load(f)

# for word in data:
#   print(word)