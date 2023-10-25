from paddleocr import PaddleOCR
import re
import cv2 as cv

class Digitalizer(PaddleOCR):
    def __init__(self, paths, **kwargs):
        super().__init__(**kwargs)
        self.images = [cv.imread(path) for path in paths]
        self.patterns = {'Instagram': '', 'Facebook': '', 'Email': '', 'Phone': ''}
        self.results = {'Instagram': [], 'Facebook': [], 'Email': [], 'Phone': []}
    
    def match_pattern(self, word, specific_pattern=''):
        if specific_pattern != '':
            sp_pattern = self.patterns[specific_pattern]
            return re.match(sp_pattern, word), specific_pattern
        else:
            for font, pattern in self.patterns.items():
                if re.match(pattern, word):
                    return True, font
        
        return False, ''
    
    def detect_text(self, specific_pattern=''):
        for image in self.images:
            result = self.ocr(image, cls=True)
            for line in result[0]:
                word = line[1][0]
                matches, font = self.match_pattern(word, specific_pattern)
                if not matches: continue
                self.results[font].append(word)