#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, Response
import database
app = Flask(__name__)
import json


@app.route('/', methods=['GET'])
def get_info():
    if request.method == 'GET':
        callback = request.args.get('callback')

        response = database.get_data()
        respDict = {}
        respDict["data"] = database.make_json_from_data(response)
        return callback + '(' + json.dumps(respDict) + ')'

@app.route('/send_data', methods=['GET'])
def send_data():
    if request.method == 'GET':
        callback = request.args.get('callback')
        ticket_id = request.args.get('ticket_id')
        ticket_type = request.args.get('ticket_type')
        ticket_priority = request.args.get('ticket_priority')
        ticket_status = request.args.get('ticket_status')
        conversation_id = request.args.get('conversation_id')
        admin_id = request.args.get('admin_id')

        database.change_data(ticket_id, ticket_type, ticket_priority,
                             ticket_status, conversation_id, admin_id)

        return callback + '()'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5022)
