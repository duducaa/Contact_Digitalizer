from paddleocr import PaddleOCR
import re
import cv2 as cv

class Digitalizer(PaddleOCR):
    def __init__(self, paths, **kwargs):
        super().__init__(**kwargs)
        self.patterns = {'Instagram': '', 'Facebook': '', 'Email': '', 'Phone': ''}
        self.contacts = {'Instagram': [], 'Facebook': [], 'Email': [], 'Phone': []}
    
    def read_image_batch(self, paths):
        return [cv.imread(path) for path in paths]

    def match_pattern(self, word, specific_pattern=''):
        if specific_pattern != '':
            sp_pattern = self.patterns[specific_pattern]
            return re.match(sp_pattern, word), specific_pattern
        else:
            for font, pattern in self.patterns.items():
                if re.match(pattern, word):
                    return True, font
        
        return False, ''
    
    def detect_text(self, paths, specific_pattern=''):
        results = []
        for image in self.read_image_batch(paths):
            result = self.ocr(image, cls=True)
            for line in result[0]:
                word = line[1][0]
                matches, font = self.match_pattern(word, specific_pattern)
                if not matches: continue
                self.contacts[font].append(word)
            results.append([image, result])

        return results