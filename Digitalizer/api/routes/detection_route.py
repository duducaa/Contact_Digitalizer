import sys, os
root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import request, Blueprint
import json
import base64
import numpy as np
from digitalizer import Digitalizer

app_detection = Blueprint('detection', __name__)

@app_detection.route('/detection', methods=['POST'])
def make_detect():
    if request.method == 'POST':
        detection_json = request.get_json()
        data = detection_json[0]

        try:
            decoded = base64.b64decode(data['image'])
            image_data = json.loads(decoded)
            image = np.array(image_data).astype(np.uint8)

            digitalizer = Digitalizer(use_angle_cls=True, lang='pt')
            results = digitalizer.detect_text(image)
            print('lololololololololo')

            return json.dumps({'Message': 'Contacts Founded!!!', 'contacts': results}), 200
        except Exception as err:
            return json.dumps({'Error': f'{err}'}), 501
    else:
        return 'Wrong Request Methods. Only POST Allowed!!!', 405