'''
Created on Nov 11, 2010

@author: Sajid Anwar
'''
import hashlib

def hash(data):
    return hashlib.md5(data).hexdigest()
