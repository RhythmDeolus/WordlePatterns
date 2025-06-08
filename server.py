import flask
app = flask.Flask(__name__)

from main import get_answer

@app.route('/')

def index():
    # return index.html file
    return flask.send_from_directory('.', 'index.html')

# read body from request
@app.route('/api/wordle', methods=['POST'])
def wordle():
    data = flask.request.get_json()
    print(data)
    pattern = data.get('pattern', '')
    wordle = data.get('wordle', '')

    if not pattern or not wordle:
        return flask.jsonify({'error': 'Invalid input'}), 400

    pattern = pattern.split(',')

    try:
        answer = get_answer(pattern, wordle)
        # print("Answer:", answer)
        return flask.jsonify(answer)
    except Exception as e:
        print("Error:", e)
        return flask.jsonify({'error': str(e)}), 500

@app.route('/static/<path:path>')
def static_files(path):
    """Serve static files from the 'static' directory."""
    return flask.send_from_directory('static', path)
    
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='localhost')