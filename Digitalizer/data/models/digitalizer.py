from paddleocr import PaddleOCR
import re
import cv2 as cv

class Digitalizer(PaddleOCR):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.patterns = {
            'Instagram': r'^@', 
            #'Facebook': '',
            'Site': r'\b(www\.)?w+\.\w{3}(\.\w{2})?\b',
            'Email': r'\b\w+@\w+(\.\w{2, 3}){1, 2}', 
            'Phone': r'\(?\d{2,3}\)?[-.\s]?9?[-.\s]?\d{4}[-.\s]?\d{4}|\b0800?\s?\d{3}\s?\d{4}\b|\b9?[-.\s]?\d{4}[-.\s]?\d{4}\b'}

    def match_patterns(self, word, score, contacts):
        for font, pattern in self.patterns.items():
            if pattern == '': continue
            matches = re.findall(pattern, word)
            for match in matches:
                contacts[font].append([match, score])
            if len(matches) > 0: break
    
    def detect_text(self, image):
        result = self.ocr(image, cls=True)
        contacts = {key: [] for key in self.patterns.keys()}
        for line in result[0]:
            word = line[1][0]
            score = line[1][1]
            self.match_patterns(word, score, contacts)

        return contacts