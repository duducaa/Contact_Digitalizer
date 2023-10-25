from paddleocr import PaddleOCR
import os
import cv2 as cv
import re
from digitalizer import Digitalizer

main_path = 'Digitalizer/tests/detection_data'
images_paths = [os.path.join(main_path, file) for file in os.listdir(main_path)]
digitalizer = Digitalizer(images_paths, use_angle_cls=True, lang='pt')
digitalizer.detect_text('Phone')

# for image, result in zip(digitalizer.images, digitalizer.results):
#     for line in result[0]:
        # word = line[1][0]
        # rect = [list(map(int, i)) for i in line[0]]
        
        # area_1 = abs((rect[1][0] - rect[3][0]) * (rect[1][1] - rect[3][1]))
        # area_2 = abs((rect[0][0] - rect[2][0]) * (rect[0][1] - rect[2][1]))
        
        # if area_1 > area_2:
        #     cv.rectangle(image, rect[1], rect[3], (255, 0, 0), 3)
        # else:
        #     cv.rectangle(image, rect[0], rect[2], (255, 0, 0), 3)
    
    # cv.imshow('Display', image)
    # cv.waitKey()
    # cv.destroyAllWindows()
    
print(digitalizer.results['Phone'])    