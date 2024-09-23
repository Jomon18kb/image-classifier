from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

notes_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('files')
    urls = []
    for file in files:
        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        urls.append(f'/static/uploads/{filename}')
    return jsonify({'urls': urls})

@app.route('/notes', methods=['POST'])
def save_notes():
    data = request.json
    notes_data[data['id']] = data['text']
    return jsonify({'status': 'success'})

@app.route('/notes/<photo_id>', methods=['GET'])
def get_notes(photo_id):
    return jsonify({'text': notes_data.get(photo_id, '')})

if __name__ == '__main__':
    app.run(debug=True)
