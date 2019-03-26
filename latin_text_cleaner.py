'''
latin_text_cleaner.py
reads text in from one or more text files, removes the punctuation and header/footer info, and
writes the output to a file
bancks holmes
'''
import string
import numpy

file = open('ovid/sample_text.txt', 'rb')
ltr_str = ''
for line in file:
    ltr_str += str(line)

out = ltr_str.translate(str.maketrans("",""), string.punctuation) #import numpy to use for this

file.close()

print(out)