'''
TextCaptchaBreaker. Created on Nov 11, 2010

@author: Sajid Anwar
'''

import WolframAlphaService
import re

numbers =   {
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
                
                'twenty': 20, 'thirty': 30, 'forty': 40,
                'fifty': 50, 'sixty': 60, 'seventy': 70, 
                'eighty': 80, 'ninety': 90, 'hundred': 100,
                
                'thousand': 1000, 'million': 1000000
            }

def solve(question):
    
    tokens = re.sub(r'[^\w\d\s]+', '', question).lower().split(' ')
    
    # Enter as digits:
    #    'Enter the number fifteen thousand six hundred and eighty six in digits:' - 15686
    #    'What is sixty four thousand six hundred and sixty one as digits?' - 64661
    if 'number' in tokens or 'digits' in tokens or 'as' in tokens:
        
        for i in range(len(tokens)):
            
            # Go through each token and remove the ones that are not digits or 'and'.
            if is_num(tokens[i]):
                continue
            elif tokens[i] in numbers:
                continue
            elif tokens[i] == 'and':
                continue
            else:
                tokens[i] = ''
                
        tokens = remove_empty(tokens)
        
        # Let WolframAlpha solve.
        return str(WolframAlphaService.words_to_number(' '.join(tokens)))
    
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
