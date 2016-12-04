import random
from urllib.request import urlopen
import sys
import os

WORD_URL = 'http://learncodethehardway.org/words.txt'
WORDS = []
PHRASES = {
"class %%%(%%%):": "Make a class named %%% that is-a %%%",
"class %%%(object):\n\tdef __init__(self, ***)": "class %%% has-a __init__ that takes self and *** paramters.",
"class %%%(object):\n\tdef ***(self, @@@)":"class %%% has-a function named *** that takes self and @@@ parameters",
"*** = %%%()": "Set *** to an instance of class %%%.",
"***.***(@@@)": "From *** get the *** function, and call it with parameters self and @@@",
"***.*** = '***'": "From *** get the *** attribute and set it to '***'."}

#check if user wants to drill phrases first
if(len(sys.argv) == 2 and sys.argv[1] == "english"):
  PHRASE_FIRST = True
else:
  PHRASE_FIRST = False
  
#load up the words from the website
for word in urlopen(WORD_URL).readlines():
  #print(word)  ##had to do some debugging here from python 2 to 3:http://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal#6273618
  temp = word.decode('UTF-8')
  #print(temp)
  WORDS.append(temp.strip()) #what is strip()?
  
def convert(snippet, phrase):
  class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
  other_names = random.sample(WORDS, snippet.count("***"))
  results = []
  param_names = []
  
  for i in range(0, snippet.count("@@@")):
    param_count = random.randint(1,3)
    param_names.append(', '.join(random.sample(WORDS, param_count)))
  
  for sentence in snippet, phrase:
    result = sentence[:]
    
    #fake class names
    for word in class_names:
      result = result.replace("%%%", word, 1)
    
    #fake other names:
    for word in other_names:
      result = result.replace("***", word, 1)
      
    #fake parameter lists
    for word in param_names:
      result = result.replace("@@@", word, 1)
    
    results.append(result)
  
  return results

try:
  while True:
    snippets = list(PHRASES.keys()) #had to do some debugging here from python 2 to 3: http://blog.labix.org/2008/06/27/watch-out-for-listdictkeys-in-python-3
    print(snippets)
    random.shuffle(snippets)
    
    for snippet in snippets:
      phrase = PHRASES[snippet]
      question, answer = convert(snippet, phrase)
      if PHRASE_FIRST:
        question, answer = answer, question
      print(question)
      
      input("> ")
      #os.system('cls') #Don't want to give away the answer when you've done a similar question above.
      print("ANSWER: \n%s\n" % answer)
except EOFError:
  print("\nBye")