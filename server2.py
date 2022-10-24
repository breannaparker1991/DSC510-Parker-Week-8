


# gba_file = open('Gettysburg.txt')

  
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

def process_line(line,word_count_dict):
  import string
  for line in word_count_dict:
    line = line.rstrip()
    line = line.translate(line.maketrans('','', word_count_dict.punctuation))
    line = line.lower()
    words = line.split()
    add_word(words,word_count_dict)

def add_word(word, word_count_dict):
  for word in word_count_dict:
    if word in word_count_dict:
      word_count_dict[word] +=1
    else:
      word_count_dict[word] = 1
      
        lst = list()
  for key,val in list(gba_dict.items()):
    lst.append((val,key))
    lst.sort(reverse = True)
    for key,val in lst[:10]:
      print(key,val)
      
      
def pretty_print(word_count_dict):
  word_count_dict = dict(reversed(sorted(word_count_dict.items(), key=lambda item: item[1])))
  print("total words:", sum(word_count_dict.values()))
  print('-' * 30)
  for word,count in word_count_dict.items():
    print('{:<26}{:>}'.format('Word', "Count"))
        
def main():
  word_count_dict = {}
  gba_file = open("Gettysburg.txt", "r")
  for line in gba_file:
    process_line(line,word_count_dict)

    pretty_print(word_count_dict)

if __name__ == "__main__":
  main()
  
main()