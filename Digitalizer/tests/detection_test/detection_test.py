import cv2 as cv
import requests
import json
import base64
import os

main_path = 'tests/detection_test/detection_data'
images_paths = [os.path.join(main_path, file) for file in os.listdir(main_path)]

BASE_URL = 'http://127.0.0.1:5000/'
headers = {'Content-type': 'application/json; charset=utf-8'}

for path in images_paths:
    image = cv.imread(path)
    json_image = json.dumps(image.tolist())
    encoded = base64.b64encode(json_image.encode())
    data = json.dumps([{'image': encoded.decode('utf8')}])

    response = requests.post(BASE_URL + 'detection', data=data, headers=headers)

    contacts = response.json()['contacts']
    for key, value in contacts.items():
        print('========================\n')
        print(f'        {key}           \n')
        for v in value:
            print(v)
        print('\n========================')

    cv.imshow('Display', image)
    cv.waitKey()