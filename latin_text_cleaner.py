'''
latin_text_cleaner.py
reads text in from one or more text files, removes the punctuation and header/footer info, and
writes the output to a file
bancks holmes
'''
import string
import numpy as np
from cltk.lemmatize.latin.backoff import BackoffLatinLemmatizer
import os

#first, build list of filenames
filenames = []
for filename in os.listdir('ovid'):
    filenames.append(str(filename))
print(filenames)
#then, concatenate them into one text file https://stackoverflow.com/questions/13613336/python-concatenate-text-files
with open('corpora/all.txt', 'w') as outfile:
    for fname in filenames:
        with open('ovid/' + fname, 'r') as infile:
            for line in infile:
                outfile.write(line)
print('outfile written')

lemmatizer = BackoffLatinLemmatizer()
ltr_str = ''

file = open('ovid/sample_text.txt', 'r')
for line in file:
    ltr_str += str(line)
file.close()

np_str = np.asarray(ltr_str)   

for symbol in string.punctuation:
    np_str = np.char.replace(np_str, symbol, '')

np_str = np.char.lower(np_str)
tokens = np_str.tolist().split()
lemmatized = lemmatizer.lemmatize(tokens)
#print(filenames)