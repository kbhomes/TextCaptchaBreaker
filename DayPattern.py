'''
TextCaptchaBreaker. Created on Nov 11, 2010

@author: Sajid Anwar
'''

import re

days =  ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def solve(question):
    
    tokens = re.sub(r'[^\w\d\s]', '', question).lower().split(' ')
    
    # Weekend:
    #    'Which day from Sunday, Thursday, Tuesday or Monday is part of the weekend?' - sunday
    #    'Which day from Friday, Saturday, Tuesday, Wednesday or Monday is part of the weekend?' - saturday
    if 'weekend' in tokens:
        
        for i in range(len(tokens)):
            
            # Go through each token and return that which is a weekend day.
            if tokens[i] == 'saturday' or tokens[i] == 'sunday':
                return tokens[i]
            
        return None
        
    # Which day is today:
    #    'What day is today, if yesterday was Wednesday?' - thursday
    #    'Tomorrow is Tuesday. If this is true, what day is today?' - monday
    elif 'today' in tokens:
        
        offset = None
        day = None
        
        for i in range(len(tokens)):
            
            # Go through each token and find whether we are looking for 
            # after yesterday or before tomorrow and save that day.
            if tokens[i] == 'yesterday':
                offset = 1  # Add 1 to yesterday to get today.
            elif tokens[i] == 'tomorrow':
                offset = -1 # Subtract 1 from tomorrow to get today.
            elif tokens[i] in days:
                day = tokens[i]
                
        if day is None or offset is None:
            return None
        
        return days[(days.index(day) + offset) % 7]
    
    else:
        return None
