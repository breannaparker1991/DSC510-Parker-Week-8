#DSC 510
#Week 9
#Gettysburg 9.1
#Author Breanna Parker
#10/24/22

import string


gba_dict = dict()

def add_word(words,gba_dict):
  for word in words:
    gba_dict[word] = gba_dict.get(word,0) + 1

def process_lines(line, gba_dict):
    line = line.rstrip()
    line = line.translate(line.maketrans('','', string.punctuation))
    line = line.lower()
    words = line.split()
    add_word(words,gba_dict)
  

def pretty_print(gba_dict):
    lst = []
    for key, val in gba_dict.items():
      lst.append((val,key))
    lst.sort(reverse=True)
    print('{:11s}{:11s}'.format("Word","Count"))
    print(''*21)
    for val, key in lst:
      print('{:12s} {:<3d}'.format(key,val))
    # previous code worked but didn't look as pretty, keep for refernce
    # for word in sorted(gba_dict, key = gba_dict.get, reverse=True):         
    #   print (word, gba_dict[word])
    

def process_file(gba_dict):
  fname = input("enter the file name:")
  try:
    # new_file = open(fname)
    with open (fname, 'w') as f:
      print(gba_dict)
  except:
    print("File cannot be opened:")
    exit()


def main():
  try:
    with open("Gettysburg.txt", 'r') as gba_file:
      for line in gba_file:
        process_lines(line, gba_dict)
      print("Length of Dictionary", len(gba_dict))
      pretty_print(gba_dict)
  except:
    print("File cannot be opened")
    exit()
  # process_file(gba_dict)


if __name__ == '__main__':
  main()
  
  