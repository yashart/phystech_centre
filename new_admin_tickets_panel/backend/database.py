#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

def get_data():
    conn = sqlite3.connect('tickets.sqlite')
    c = conn.cursor()

    response = []
    for row in c.execute('''SELECT * FROM tickets'''):
        response.append(row)
    conn.close()

    return response

def make_json_from_data(database_answer):
    responseList = []
    for row in database_answer:
        print row
        rowDict = {}
        rowDict['id_ticket'] = u'<b>' + str(row[0]) + u'</b>'
        rowDict['time'] = row[1]
        rowDict['user_info'] = u'id - ' + str(row[2]) + u'<br>' +\
                               row[3] + u'<br>' + \
                               row[4] + u'<br>' + \
                               str(row[5])
        rowDict['browser'] = row[6]
        rowDict['ticket_data'] = u'<b>' + row[7] + u'</b>' + u'<br>' + \
                                 row[8]
        rowDict['url'] = row[9]
        rowDict['id_type'] = row[10]
        rowDict['priority'] = row[11]
        rowDict['status'] = row[12]
        rowDict['conversation_id'] = row[13]
        rowDict['admin_id'] = row[14]
        rowDict['editButton'] = u'<button type="button" id="editButton' + str(row[0]) +\
                                u'" class="btn btn-primary">' +\
                               u'Редактировать' + u'</button>'

        responseList.append(rowDict)
    return responseList

def change_data(ticket_id, ticket_type, ticket_priority,
                ticket_status, conversation_id, admin_id):

    param_tup = ticket_type, ticket_priority, ticket_status, conversation_id, admin_id, int(ticket_id)
    print "^^^^^^^^^^^^^^^^"
    print param_tup
    print "^^^^^^^^^^^^^^^^^^"
    conn = sqlite3.connect('tickets.sqlite')
    c = conn.cursor()
    c.execute('''UPDATE tickets SET
    id_type = ?,
    priority = ?,
    status = ?,
    conversation_id = ?,
    admin_id = ?
    WHERE id_ticket = ?''', param_tup)
    conn.commit()

    conn.close()
    return

if __name__ == "__main__":
    print get_data()