from flask import Flask, request, jsonify, Response
import database
app = Flask(__name__)
import json


@app.route('/', methods=['GET'])
def get_info():
    if request.method == 'GET':
        callback = request.args.get('callback')
        ticket_type = tuple(json.loads(request.args.get('ticket_type')))
        domain = tuple(json.loads(request.args.get('domain')))
        status = tuple(json.loads(request.args.get('status')))
        order = tuple(json.loads(request.args.get('order')))
        response = database.get_data(0, 0, 0, ticket_type,
                          domain, status, 0, order)
        response = database.make_json_from_data(response)
        return callback + '(' + json.dumps(response) + ')'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5022)
