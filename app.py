from flask import Flask, request
from flask_cors import CORS
from process import build_jcamp
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def testing_route():
    return '<h1>Flask App is currently running</h1>'
    

@app.route('/build_jcamp', methods=['POST'])
def build_jcamp_route():
    data = request.json
    metadatas = data.get('metadatas', {})
    assignments = data.get('assignments', [])
    spec_jcamp = data.get('specJcamp', '')
    struc_jcamp = data.get('strucJcamp', '')

    built_jcamp = build_jcamp(metadatas, struc_jcamp, spec_jcamp, assignments)  # type: ignore

    return built_jcamp

@app.route('/identify_peak_and_build_jcamp', methods=['POST'])
def identify_peak_and_build_jcamp_route():
    return


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    
    