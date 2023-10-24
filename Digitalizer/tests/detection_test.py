from paddleocr import PaddleOCR
import os
import cv2 as cv
import re

class Digitalizer(PaddleOCR):
    def __init__(self, main_path, **kwargs):
        super().__init__(**kwargs)
        self.images_path = [os.path.join(main_path, file) for file in os.listdir(main_path)]
        self.results = []
        
    def detect_text(self):
        for path in self.images_path:
            image = cv.imread(path)
            result = self.ocr(image, cls=True)
            self.results.append(result)

main_path = 'Digitalizer/tests/detection_data'
ocr = Digitalizer(main_path, use_angle_cls=True, lang='pt')
for index, path in enumerate(ocr.images_path):
    image = cv.imread(path)
    
    results = ocr.ocr(image, cls=True)
    for line in results[0]:
        word = line[1][0]
        rect = [list(map(int, i)) for i in line[0]]
        
        area_1 = abs((rect[1][0] - rect[3][0]) * (rect[1][1] - rect[3][1]))
        area_2 = abs((rect[0][0] - rect[2][0]) * (rect[0][1] - rect[2][1]))
        
        if area_1 > area_2:
            cv.rectangle(image, rect[1], rect[3], (255, 0, 0), 3)
        else:
            cv.rectangle(image, rect[0], rect[2], (255, 0, 0), 3)
    
    cv.imshow('Display', image)
    cv.waitKey()
    cv.destroyAllWindows()
    