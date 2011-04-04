'''
Created on Nov 11, 2010

@author: Sajid Anwar
'''

import re

single_numbers =   {
                'zero': 0,  'ten': 10,     
                'one': 1,   'eleven': 11, 
                'two': 2,   'twelve': 12, 
                'three': 3, 'thirteen': 13, 
                'four': 4,  'fourteen': 14, 
                'five': 5,  'fifteen': 15, 
                'six': 6,   'sixteen': 16, 
                'seven': 7, 'seventeen': 17, 
                'eight': 8, 'eighteen': 18, 
                'nine': 9,  'nineteen': 19,
                'hundred': 100
            }
split_numbers = {
                    'twenty': 20, 'thirty': 30, 'forty': 40,
                    'fifty': 50, 'sixty': 60, 'seventy': 70, 
                    'eighty': 80, 'ninety': 90
                }
ordinals =  {
                '1st': 1, 'first': 1,
                '2nd': 2, 'second': 2,
                '3rd': 3, 'third': 3,
                '4th': 4, 'fourth': 4,
                '5th': 5, 'fifth': 5,
                '6th': 6, 'sixth': 6,
                '7th': 7, 'seventh': 7,
                '8th': 8, 'eighth': 8,
                '9th': 9, 'ninth': 9,
                '10th': 10, 'tenth': 10
            }

def solve(question):
    
    tokens = remove_empty(re.sub(r'[^\w\d\s]', ' # ', question).lower().split(' '))
    found = []
    which = -1
    
    # Which number:
    #    'What is the 2nd number in the list nineteen, 23 and twenty nine?' - 23
    if 'number' in tokens or \
       'largest' in tokens or 'biggest' in tokens or 'highest' in tokens or \
       'smallest' in tokens or 'lowest' in tokens:
        
        for i in range(len(tokens)):
            
            # Go through each token and save those that are numbers and those that are ordinal.
            if tokens[i] in ordinals:
                which = ordinals[tokens[i]]
            elif is_num(tokens[i]):
                found.append(int(tokens[i]))
            elif tokens[i] in single_numbers:
                if single_numbers[tokens[i]] == 100 and i != 0 and tokens[i - 1] in single_numbers:
                    found.append(single_numbers[tokens[i-1]] * 100)
                else:
                    found.append(single_numbers[tokens[i]])
            elif tokens[i] in split_numbers:
                if i + 1 != len(tokens) and tokens[i + 1] in single_numbers:
                    found.append(split_numbers[tokens[i]] + single_numbers[tokens[i + 1]])
                    tokens[i + 1] = None
                else:
                    found.append(split_numbers[tokens[i]])
                
        if which == -1:
            if 'largest' in tokens or 'biggest' in tokens or 'highest' in tokens:
                return str(max(found))
            elif 'smallest' in tokens or 'lowest' in tokens:
                return str(min(found))
            else:
                return None
        else:
            return str(found[which - 1])
    
    else:
        return None
    
def is_num(str_value):
    
    try:
        int(str_value)
    except:
        return False
    
    return True

def remove_empty(list):
    
    while '' in list:
        list.remove('')
        
    return list
