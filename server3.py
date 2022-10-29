#DSC 510
#Week 9
#Gettysburg 9.1
#Author Breanna Parker
#10/24/22

import string

def add_word(word,gba_dict):
  if word in gba_dict:
    gba_dict[word] +=1
  else:
    gba_dict[word] = 1
    

def process_lines(line, gba_dict):
    line = line.strip()
    words = line.split()
    for word in words:
      if word != '--':
        word = word.lower()
        word = word.strip()
        word = word.strip(string.punctuation)
        add_word(word,gba_dict)
  

def pretty_print(gba_dict):
    lst = []
    for key, val in gba_dict.items():
      lst.append((val,key))
    lst.sort(reverse=True)
    print('{:11s}{:11s}'.format("Word","Count"))
    print(''*21)
    for val, key in lst:
      print('{:12s} {:<3d}'.format(key,val))

def process_file(gba_dict):
  fname = input("enter the file name:")
  try:
    with open (fname, 'w') as f:
      fname.write(gba_dict)
  except:
    print("File cannot be opened:")
    exit()


def main():
  gba_dict = dict()
  try:
    gba_file = open("Gettysburg.txt", 'r')
  except FileNotFoundError as e:
    print(e)
    exit()
  for line in gba_file:
    process_lines(line, gba_dict)
  print("Length of Dictionary", len(gba_dict))
  pretty_print(gba_dict)


if __name__ == '__main__':
  main()
  