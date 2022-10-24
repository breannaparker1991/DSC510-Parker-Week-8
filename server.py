#DSC 510
#Week 9
#Gettysburg 9.1
#Author Breanna Parker
#10/24/22


import string

gba_dict = dict()

def add_word(words,gba_dict):
  for words in gba_dict:
    if words in gba_dict:
      gba_dict[words] +=1
    else:
      gba_dict[words] = 1
  print(gba_dict)

def process_lines():
  for line in gba_dict:
    line = line.rstrip()
    line = line.translate(line.maketrans('','', gba_dict.punctuation))
    line = line.lower()
    words = line.split()
    add_word(words,gba_dict)

def pretty_print(gba_dict):
  lst = list()
  for key,val in list(gba_dict.items()):
    lst.append((val,key))
    lst.sort(reverse = True)
    for key,val in lst[:10]:
      print(key,val)

def main(gba_dict):
  try:
    gba_file = open("Gettysburg.txt", 'r')
  except:
    print("File cannot be opened")
    exit()
  for line in gba_file:
    process_lines(line, gba_dict)
    pretty_print(gba_dict)
  
if __name__ == '__main__':
  main()
  