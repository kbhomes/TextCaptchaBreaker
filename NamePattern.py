'''
Created on Nov 11, 2010

@author: Sajid Anwar
'''

import re

omit = ['What', 'If', 'The']

def solve(question):
    
    question = re.sub(r"'s", '', question)
    question = re.sub(r'[^\w\d\s]', '', question)
    tokens = question.split(' ')
    name = None
    
    # Name:
    #    'What is Susan's name?' - Susan
    #    'If a person is called George, what is their name?' - George
    if 'name' in tokens:
        
        for i in range(len(tokens)):
            
            # Go through each token and save those that have a capital letter that we won't omit.
            if tokens[i] not in omit and re.search(r'^[A-Z]', tokens[i]):
                name = tokens[i].lower()

    return name
