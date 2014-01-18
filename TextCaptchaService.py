'''
TextCaptchaBreaker. Created on Nov 11, 2010

@author: Sajid Anwar
'''

import Browser
import xml.dom.minidom

class TextCaptchaService:
    '''
    Methods to request a new textCAPTCHA.
    '''

    def __init__(self, apikey):
        
        # Initialize a new Browser for our service.
        self._browser = Browser.Browser()
        self._apikey = apikey
        
    def captcha(self):
        
        # Download a CAPTCHA and its answer(s).
        response = self._browser.open('http://textcaptcha.com/api/' + self._apikey, set_referer=False).read()
        question = ''
        answers = []
        
        # Check if everything's alright.
        if len(response) == 0:
            return None
        
        # Parse the XML.
        document = xml.dom.minidom.parseString(response)
        
        # Get the question.
        question = document.getElementsByTagName('question')[0].firstChild.data
        
        # Get the answers.
        nodes = document.getElementsByTagName('answer')
        
        if len(nodes) == 0:
            raise RuntimeError('Unable to parse answer(s) from textCAPTCHA')
        
        for i in range(len(nodes)):
            answers.append(nodes[i].firstChild.data)
            
        return (question, answers)
