import json

with open('Gettysburg.txt') as f:
  data = json.load(f)

for word in data:
  print(word)