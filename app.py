from flask import Flask, jsonify

app = Flask(__name)

@app.route('/')
def hello_world():
    response_data = {"message": "Hello, World!"}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
