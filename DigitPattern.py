'''
Created on Nov 11, 2010

@author: Sajid Anwar
'''

import re

ordinals =  {
                '1st': 1, 'first': 1,
                '2nd': 2, 'second': 2,
                '3rd': 3, 'third': 3,
                '4th': 4, 'fourth': 4,
                '5th': 5, 'fifth': 5,
                '6th': 6, 'sixth': 6,
                '7th': 7, 'seventh': 7,
                '8th': 8, 'eight': 8,
                '9th': 9, 'ninth': 9,
                '10th': 10, 'tenth': 10
            }

def solve(question):
    
    tokens = re.sub(r'[^\w\d\s]', '', question).lower().split(' ')
    number = None
    which = -1
    
    # Digit:
    #    'What is the 6th digit in 7911863?' - pink
    if 'digit' in tokens:
        
        for i in range(len(tokens)):
            
            # Go through each token and save those that are numbers or ordinals.
            if is_num(tokens[i]):
                number = tokens[i]
            elif tokens[i] in ordinals:
                which = ordinals[tokens[i]]
                
        return number[which - 1]
       
    else:
        return None
    
def is_num(str_value):
    
    try:
        int(str_value)
    except:
        return False
    
    return True
