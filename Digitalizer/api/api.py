import sys, os
sys.path.append(os.path.join(os.getcwd(), "api/routes"))
sys.path.append(os.path.join(os.getcwd(), "data/models"))

from flask import Flask
from flask_cors import CORS

from routes.detection_route import app_detection

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(app_detection)

if __name__ == '__main__':
    app.run(debug=True)