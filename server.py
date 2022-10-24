import json

def process_line(line,word_count_dict):
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
      
      
def pretty_print(word_count_dict):
  for key,value in word_count_dict():
    print('{:11}{:11}'.format('Word', "Count"))
        
def main():
  word_count_dict = {}
  gba_file = open("Gettysburg.txt")
  for line in gba_file:
    process_line(line,word_count_dict)

    pretty_print(word_count_dict)

if __name__ == "__main__":
  main()
  
main()