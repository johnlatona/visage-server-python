import http.server
import socketserver
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from visage import ApplyMakeup
import os

app = Flask(__name__, static_url_path='')
CORS(app)
 
@app.route("/api", methods=['POST'])
def hello():
    content = request.get_json()
    r = content.get('R')
    g = content.get('G')
    b = content.get('B')
    imgPath = content.get('imgPath')

    print(r)
    print(g)
    print(b)
    AM = ApplyMakeup()
    output_file = AM.apply_lipstick(imgPath,float(r),float(g),float(b))
    # print('ooutput file', output_file)
    # file_output = f"output_color_{r}_{g}_{b}.jpg"
    # filename = os.path.join(app.instance_path, '', file_output)
    return jsonify({
      "fileLocation": f"{app.root_path}/output_color_{r}_{g}_{b}.jpg"
    })
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')