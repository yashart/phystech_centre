#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, Response, abort
import database
import check_admin
app = Flask(__name__)
import json


@app.route('/get_data', methods=['GET'])
def get_info():
    if request.method == 'GET':
        callback = request.args.get('callback')
        userId = check_admin.get_id(request.cookies)

        if(check_admin.is_admin(userId) == False):
            abort(401)

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

    return

@app.route('/get_conversation', methods=['GET'])
def get_conversation():
    if request.method == 'GET':
        callback = request.args.get('callback')
        conversationId = request.args.get('conversation_id')
        userId = check_admin.get_id(request.cookies)

        if(check_admin.is_admin(userId) == False):
            abort(401)

        response = database.get_conversations(conversationId)
        respDict = {}
        respDict['conversation'] = database.make_conversation_html(response)

        return callback + '(' + json.dumps(respDict) + ')'

    return

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5022)
