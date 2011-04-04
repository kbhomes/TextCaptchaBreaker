'''
Created on Nov 11, 2010

@author: Sajid Anwar
'''

import re

numbers =   {
                'zero': 0,      'one': 1,   'eleven': 11, 
                'ten': 10,      'two': 2,   'twelve': 12, 
                'twenty': 20,   'three': 3, 'thirteen': 13, 
                'thirty': 30,   'four': 4,  'fourteen': 14, 
                'forty': 40,    'five': 5,  'fifteen': 15, 
                'fifty': 50,    'six': 6,   'sixteen': 16, 
                'sixty': 60,    'seven': 7, 'seventeen': 17, 
                'seventy': 70,  'eight': 8, 'eighteen': 18, 
                'eighty': 80,   'nine': 9,  'nineteen': 19, 
                'ninety': 90, 
            }

def solve(question):
    
    tokens = re.sub(r'[\?,]', '', question).lower().split(' ')
    operator = 1
    index = -1
    
    # Addition:
    #    'What is 10 plus 1?' - 11
    #    '1 + 3 is what?' - 4
    if 'plus' in tokens or '+' in tokens or 'add' in tokens:
        
        # Find the location of the operator.
        index = tokens.index('plus') if 'plus' in tokens else \
                tokens.index('+') if '+' in tokens else \
                tokens.index('add') if 'add' in tokens else \
                None
                
        if index is None:
            return None
        
        operator = 1
    
    # Subtraction:
    #    'What is ten - 3?' - 7
    #    '8 minus 4 is what?' - 4
    elif 'minus' in tokens or '-' in tokens or 'subtract' in tokens:
        
        # Find the location of the operator.
        index = tokens.index('minus') if 'minus' in tokens else \
                tokens.index('-') if '-' in tokens else \
                tokens.index('subtract') if 'subtract' in tokens else \
                None
                
        if index is None:
            return None
        
        operator = -1
        
    else:
        return None
        
    # Get the tokens before and after the operator (should be numbers).
    before = tokens[index - 1]
    before = int(before) if is_num(before) else numbers[before] if before in numbers else None
    after = tokens[index + 1]
    after = int(after) if is_num(after) else numbers[after] if after in numbers else None
    
    if before is None or after is None:
        return None
    
    # Return the total.
    return str(before + operator * after)
        
def is_num(str_value):
    
    try:
        int(str_value)
    except:
        return False
    
    return True
