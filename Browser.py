'''
TextCaptchaBreaker. Created on Jun 13, 2010

@author: Sajid Anwar
'''
import urllib2

class Browser:
    
    def __init__(self):
        
        self.cookies = urllib2.HTTPCookieProcessor()
        self.opener = urllib2.build_opener(self.cookies)
        self.useragent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1'
        self.referer = None
    
    def open(self, url, data=None, set_referer=True, timeout=None):
        
        self.opener.addheaders = [
            ('User-Agent', self.useragent)
        ]
        
        if self.referer:
            self.opener.addheaders.append(('Referer', self.referer))
        
        
        resp = self.opener.open(url, data, timeout)
        
        if set_referer:
            self.referer = resp.geturl()
            
        return resp
        
