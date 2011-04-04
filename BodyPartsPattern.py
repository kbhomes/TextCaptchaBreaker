'''
Created on Nov 11, 2010

@author: Sajid Anwar
'''

import re

parts = ['hair', 'ankle', 'thumb', 'toe', 'eye', 'chin', 'head', 'chest', 'face', 'stomach',
         'hand', 'heart', 'arm', 'ear', 'nose', 'foot', 'knee', 'leg', 'elbow', 'finger', 'tongue',
         'tooth', 'brain']

def solve(question):
    
    tokens = re.sub(r'[^\w\d\s]', '', question).lower().split(' ')
    found = []
    
    # Body parts:
    #    'Cat, apple, finger, elephant or hospital: the body part is?' - finger
    #    'The list chin, cat, head, toe, T-shirt and hair contains how many body parts?' - four
    #    'Ant, snake and eye: how many body parts in the list?' - one
    #    'Cat, apple, finger, elephant or hospital: the body part is?' - finger
    if 'body' in tokens and ('part' in tokens or 'parts'):
        
        for i in range(len(tokens)):
            
            # Go through each token and save those that are body parts.
            if tokens[i] in parts:
                found.append(tokens[i])               
    else:
        return None
    
    if len(found) == 1:
        if 'parts' in tokens:
            return '1'
        else:
            return found[0]
    elif len(found) > 1:
        return str(len(found))
    else:
        return None
        
