from flask import Flask, jsonify, request

app = Flask(__name)

@app.route('/')
def hello_world():
    response_data = {"message": "Hello, World!"}
    return jsonify(response_data)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()

    if 'num1' in data and 'num2' in data:
        result = data['num1'] +  data['num2']
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Please provide 'num1' and 'num2' in the request body."}, 400)


if __name__ == '__main__':
    app.run(debug=True)
