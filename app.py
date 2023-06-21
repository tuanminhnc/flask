from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_data():
    # Get list user Data
    data = {'id': '123456', 'name': 'tuan minh'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
