'''
TextCaptchaBreaker. Created on Nov 12, 2010

@author: Sajid Anwar
'''

import Browser
import re
import urllib

def words_to_number(words):
    
    try:
        browser = Browser.Browser()
        response = browser.open('http://www.wolframalpha.com/input/?i=' + urllib.quote_plus(words)).read()
        
        return re.search(r"javascript:showmathpop\('(\d+)'\)", response).group(1)
    except Exception as ex:
        return -1
    
