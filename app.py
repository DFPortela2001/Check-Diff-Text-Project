from flask import Flask, render_template, request, jsonify
from difflib import Differ, SequenceMatcher

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compare', methods=['POST'])
def compare():
    data = request.get_json()
    text1 = data['text1']
    text2 = data['text2']

    differ = Differ()
    result = list(differ.compare(text1.splitlines(), text2.splitlines()))

    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True)
