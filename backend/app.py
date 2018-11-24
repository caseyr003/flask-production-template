from flask import Flask, request, jsonify

# declare constants
HOST = '0.0.0.0'

# initialize flask application
app = Flask(__name__)

# sample api endpoint
@app.route('/api/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        # get parameters from post request
        data=request.get_json()
        if 'value' in data:
            return jsonify(status=201, value=data['value'])
        return jsonify(status=400, value='error')
    else:
        return jsonify(status=200, value='success')


if __name__ == '__main__':
    app.run(host=HOST)
