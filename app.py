from flask import Flask, request
from flask_cors import CORS
from process import build_jcamp
import gc
import os

app = Flask(__name__)
CORS(app)

level = 0
correctAns = {}

metadatas = {}
assignments = []
spec_jcamp = ""
struc_jcamp = ""

@app.route('/')
def testing_route():
    return '<h1>Flask App is currently running</h1>'


@app.route('/app_input', methods=['POST'], strict_slashes=False)
def get_input():
    global assignments, spec_jcamp, struc_jcamp, metadatas

    metadatas = request.json['metadatas']
    assignments = request.json['assignments']
    spec_jcamp = request.json['specJcamp']
    struc_jcamp = request.json['strucJcamp']


@app.route('/build_jcamp')
def check_draw():
    global level, correctAns

    built_jcamp = build_jcamp(metadatas, struc_jcamp, spec_jcamp, assignments)  # type: ignore
    
    return built_jcamp


@app.route('/identify_peak_and_build_jcamp')
def identify_peak_and_build_jcamp():
    return 


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    
    