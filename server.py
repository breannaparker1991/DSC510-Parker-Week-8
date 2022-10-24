import json

def process_line(line,word_count_dict):
  pass

def add_word(word, word_count_dict):
  for word in data:
    if word in gba_dict:
      gba_dict[word] +=1
    else:
      gba_dict[word] = 1
      
      
def pretty_print(word_count_dict):
  print('{:11}{:11}'.format('Word', "Count"))
        
def main():
  word_count_dict = {}
  try:
    with open("Gettysburg.txt", 'r') as file:
      #####
  except FileNotFoundError as e:
    print(e)
  else:
    pretty_print(word_count_dict)

if __name__ == "__main__":
  main()