'''
TextCaptchaBreaker. Created on Nov 11, 2010

@author: Sajid Anwar
'''

import TextCaptchaService
import ColorPattern
import NamePattern
import BodyPartsPattern
import DigitPattern
import AddSubtractPattern
import WhichNumberPattern
import WordsToNumberPattern
import DayPattern
import Md5
import sys

if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        print('TextCAPTCHA API key required.')
        print('')
        print('Usage: python TextCaptchaBreaker.py <API_KEY> <iterations>')
        sys.exit()
    
    apikey = sys.argv[1]
    service = TextCaptchaService.TextCaptchaService(apikey)
    total = 10
    solved = 0
    
    if len(sys.argv) == 3:
        try:
            total = int(sys.argv[2])
        except:
            pass
    else:
        print('Did not specify number of iterations, defaulting to %d' % total)
        print('')
    
    for i in range(total):
        
        question, hashes = service.captcha()
        answer = None
        answerer = None
        
        try:
            if answer is None:
                answer = ColorPattern.solve(question)
            if answer is None:
                answer = NamePattern.solve(question)
            if answer is None:
                answer = BodyPartsPattern.solve(question)
            if answer is None:
                answer = DigitPattern.solve(question)
            if answer is None:
                answer = AddSubtractPattern.solve(question)
            if answer is None:
                answer = WhichNumberPattern.solve(question)
            if answer is None:
                answer = WordsToNumberPattern.solve(question)
            if answer is None:
                answer = DayPattern.solve(question)
            
            if answer is not None and Md5.hash(answer) in hashes:
                print('%d - Solved! %s - "%s"' % (i, answer, question))
                solved += 1
            else:
                print('%d - Failed! "%s" - %s' % (i, question, hashes))
        except:
            print('%d - Exception: %s' % (i, question))
            
    print('Solved %d of %d' % (solved, total))
    
