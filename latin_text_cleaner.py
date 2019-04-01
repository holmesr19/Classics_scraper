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

#then, concatenate them into one text file https://stackoverflow.com/questions/13613336/python-concatenate-text-files
with open('corpora/all.txt', 'w') as outfile:
    for fname in filenames:
        with open('ovid/' + fname, 'r') as infile:
            for line in infile:
                outfile.write(line)


lemmatizer = BackoffLatinLemmatizer()
ltr_str = ''

file = open('corpora/all.txt', 'r')
for line in file:
    ltr_str += str(line)
file.close()

np_str = np.asarray(ltr_str)   

for symbol in string.punctuation:
    np_str = np.char.replace(np_str, symbol, '')

np_str = np.char.lower(np_str)
tokens = np_str.tolist().split()
lemmatized = lemmatizer.lemmatize(tokens)
with open ('corpora/all_lemmatized.txt', 'w') as lemmata:
    for parsed in lemmatized:
        lemmata.write(parsed[1] + ' ')
#print('all lemmata written successfully :)')

#make list of heroides filnames
her_filnames = []
for filename in filenames:
    if filename[5:8] == 'met':
        her_filnames.append(str(filename))

#add their text to corpora/her.txt
with open('corpora/met.txt', 'w') as outfile:
    for fname in her_filnames:
        with open('ovid/' + fname, 'r') as infile:
            for line in infile:
                outfile.write(line)

#lemmatize (and clean) the fool out that mf (this should be a function)
her_str = ''

her_file = open('corpora/met.txt', 'r')
for line in her_file:
    her_str += str(line)
her_file.close()

her_np_str = np.asarray(her_str)   

for symbol in string.punctuation:
    her_np_str = np.char.replace(her_np_str, symbol, '')

her_np_str = np.char.lower(her_np_str)
her_tokens = her_np_str.tolist().split()
her_lemmatized = lemmatizer.lemmatize(her_tokens)
with open ('corpora/met_lemmatized.txt', 'w') as lemmata:
    for parsed in her_lemmatized:
        lemmata.write(parsed[1] + ' ')
print("heroides lemmata written successfully :')")
#write the lemmatized output to corpora/her_lemmatized.txt