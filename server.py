import http.server
import socketserver
import types
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from visage import ApplyMakeup
import os

app = Flask(__name__, static_url_path='')
CORS(app)
 
@app.route("/api", methods=['POST'])
def hello():
    content = request.get_json()
    imgPath = content.get('imgPath')
    if isinstance(content.get('colors'), list):
        colorHexes = content.get('colors')
        colorList = []
        for color in colorHexes:
            r = color.get('R')
            g = color.get('G')
            b = color.get('B')
            AM = ApplyMakeup()
            output_file = AM.apply_lipstick(imgPath,float(r),float(g),float(b))
            fileLocation = {
                "fileLocation": f"{app.root_path}/output_color_{r}_{g}_{b}.jpg"
            }
            colorList.append(fileLocation)
        print(colorList)
        return jsonify(colorList)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')