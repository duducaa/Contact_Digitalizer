from paddleocr import PaddleOCR
import os
from digitalizer import Digitalizer
import cv2 as cv

main_path = 'Digitalizer/detection_data'
images_paths = [os.path.join(main_path, file) for file in os.listdir(main_path)]
digitalizer = Digitalizer(images_paths, use_angle_cls=True, lang='pt')
results = digitalizer.detect_text(images_paths, 'Phone')

for image, result in results:
    for index, line in enumerate(result[0]):
        word = line[1][0]
        rect = [list(map(int, i)) for i in line[0]]
        
        area_1 = abs((rect[1][0] - rect[3][0]) * (rect[1][1] - rect[3][1]))
        area_2 = abs((rect[0][0] - rect[2][0]) * (rect[0][1] - rect[2][1]))

        if area_1 > area_2:
            point_i, point = rect[1], rect[3]
        else:
            point_i, point = rect[0], rect[2]

        point_min = [min(point_i[0], point[0]), min(point_i[1], point[1])]
        point_max = [max(point_i[0], point[0]), max(point_i[1], point[1])]

        cv.rectangle(image, point_min, point_max, (255, 0, 0), 3)
        cropped_image = image[point_min[1]:point_max[1], point_min[0]:point_max[0]]

        cv.imshow(f'Cropped {index}', cropped_image)
    
    cv.imshow('Display', image)
    cv.waitKey()
    cv.destroyAllWindows()
    
# print(digitalizer.results['Phone'])    