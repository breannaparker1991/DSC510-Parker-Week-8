#DSC 510
#Week 9
#Gettysburg 9.1
#Author Breanna Parker
#10/24/22

from fileinput import close
import string
import operator

gba_dict = dict()

def add_word(words,gba_dict):
  for word in words:
    gba_dict[word] = gba_dict.get(word,0) + 1

def process_lines(line, gba_dict):
  # for line in gba_dict:
    line = line.rstrip()
    line = line.translate(line.maketrans('','', string.punctuation))
    line = line.lower()
    words = line.split()
    add_word(words,gba_dict)
  

def pretty_print(gba_dict):
    for word in sorted(gba_dict, key = gba_dict.get, reverse=True):
      print (word, gba_dict[word])

def process_file(gba_dict):
  fname = input("enter the file name:")
  try:
    with open (fname, 'w') as f:
      fname.write(gba_dict)
  except:
    print("File cannot be opened:")
    exit()


def main():
  try:
    with open("Gettysburg.txt", 'r') as gba_file:
      for line in gba_file:
        process_lines(line, gba_dict)
      pretty_print(gba_dict)
  except:
    print("File cannot be opened")
    exit()
  process_file(gba_dict)
if __name__ == '__main__':
  main()
  
  
main()