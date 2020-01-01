# import the necessary libraries 
import nltk 
import re
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords 
from collections import Counter
import pickle as pckl
import glob
import sys
# python3 -mpickle count.pckl 

# Case folding
def text_lowercase(text): 
	return text.lower() 

# Remove special characters 
def remove_nonalphanum(text): 
	result = re.sub(r'[^\d\w\s\n\t]+', '', text) 
	return result 

# Remove stopwords
def remove_stopwords(text): 
	stop_words = set(stopwords.words("english")) 
	word_tokens = word_tokenize(text) 
	filtered_text = [word for word in word_tokens if word not in stop_words] 
	return ' '.join(filtered_text)
  
text = ''
for filename in glob.glob('corpus/*.txt'):
	with open(filename, 'r') as f:
		text += '\n'.join(f.readlines())

text = text_lowercase(text)
text = remove_nonalphanum(text)
text = remove_stopwords(text)

col = Counter(text.split())

print (len(col))

with open('count.pckl', 'wb') as f:
	pckl.dump(col, f)



