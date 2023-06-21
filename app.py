from flask import Flask, jsonify, request, stream_with_context
from datetime import datetime

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY="dev"
)
app.config.from_prefixed_env()

html = f'''
    <html>
        <boby>
            <h1> Flask Rest API </H1>
            <p> The current time is {datetime.now()}. </p>
            <a href='/users' target='_bank'>users</a>
        </body>
    </html>
'''

@app.route('/')
def index():
    return stream_with_context(html)

@app.route('/users', methods=['GET'])
def get_data():
    # Get list user Data
    data = {'id': '123456', 'name': 'tuan minh'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
