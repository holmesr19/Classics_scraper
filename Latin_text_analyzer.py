'''
Author: bancks holmes
File: Latin_text_analyzer.py
Purpose: This program integrates the parsing engine from whitaker's words 
with a text analysis component similar to one like that employed by voyant
tools. A parsing engine assists the operation of the text analyzer in a 
language such as latin because it is so much more dependent on declension
and conjugation than a non-inflected language like english.
'''

class latin_text_analyzer(object)

    def __init__():
        words = []
        author = '%author%'
        
    def initial_letters(words):
        initial_letters = []
        for word in words:
            initial_letters.append(word[0]) 
        return initial_letters