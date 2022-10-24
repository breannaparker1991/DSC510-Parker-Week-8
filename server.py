import json

gba_file = open('Gettysburg.txt')
gba_dict = dict()
# def add_word():
#   with open("Gettysburg.txt") as f:
#     for line in f:
#       (key,val) = line.split()
#       gba_dict[int(key)] = val
#   print(gba_dict)


def add_word():
  for line in gba_file:
    word = line.split()
    for w in word:
      if word not in gba_dict:
        gba_dict[word] = 1
      else:
        gba_dict[word] += 1
  print(gba_dict)
  
add_word()

# def add_word():
#   for word in gba_file:
#     if word in gba_dict:
#       gba_dict[word] +=1
#     else:
#       gba_dict[word] = 1
#   print(gba_dict)


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