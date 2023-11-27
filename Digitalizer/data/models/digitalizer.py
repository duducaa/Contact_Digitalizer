from paddleocr import PaddleOCR
import re
import cv2 as cv
import requests

class Digitalizer(PaddleOCR):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.patterns = {
            'Email': r'\w+@\w+\.\w{3}\.\w{2}', 
            'Instagram': r'@[\w\.]+',
            'Site': r'www\.\w+\.\w{3}\.\w{2}(/\w+)?|\w+\.\w{3}\.\w{2}(/\w+)?',
            'Phone': r'\(?\d{2,3}\)?[-.\s]?9?[-.\s]?\d{4}[-.\s]?\d{4}|\b0800?\s?\d{3}\s?\d{4}\b|\b9?[-.\s]?\d{4}[-.\s]?\d{4}\b'}
        
        self.verify_functions = {
            'Instagram': self.verify_instagram,
            'Site': self.verify_site,
            'Email': self.verify_email,
            'Phone': self.verify_phone
        }

    def match_patterns(self, word, score, contacts):
        for font, pattern in self.patterns.items():
            if pattern == '': continue
            matches = re.findall(pattern, word)
            for match in matches:
                contacts[font].append([match, score])
    
    def detect_text(self, image):
        result = self.ocr(image, cls=True)
        contacts = {key: [] for key in self.patterns.keys()}
        for line in result[0]:
            word = line[1][0]
            print(word)
            score = line[1][1]
            self.match_patterns(word, score, contacts)

        return contacts
    
    def verify_instagram(self, account):
        pass
    
    def verify_site(self, site):
        response = requests.get(f"https://{site}")
        print(response.status_code)
        return response.status_code == 200
    
    def verify_email(self, email):
        pass
    
    def verify_phone(self, phone):
        pass