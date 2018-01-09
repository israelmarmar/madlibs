import re

regex = re.compile(r"\[(\w+)\]")

ch='y'

while ch=='y':

  file = open("madtemp.txt", "r")
  stri=file.readlines()
  stri=" ".join(stri)

  for lexical in regex.findall(stri):
    word=raw_input("Digit a "+lexical+": ")
    stri=stri.replace("["+ lexical+"]",word,1)
  print stri
  ch=raw_input("Continue? y/n: ")

file.close()
