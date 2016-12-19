#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('db_config.cfg')

def get_data():

    conn = mdb.connect(host=config.get('admin_panel_db', 'host'),
                       user=config.get('admin_panel_db', 'user'),
                       passwd=config.get('admin_panel_db', 'passwd'),
                       db=config.get('admin_panel_db', 'db'),
                       charset=config.get('admin_panel_db', 'charset'))
    c = conn.cursor()

    response = []
    c.execute('''SELECT * FROM ''' + config.get('admin_panel_db', 'tickets_table'))
    rows = c.fetchall()
    for row in rows:
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
        rowDict['conversation_id'] = str(row[13])
        rowDict['admin_id'] = str(row[14])
        rowDict['editButton'] = u'<button type="button" id="editButton' + str(row[0]) +\
                                u'" class="btn btn-primary">' +\
                               u'Редактировать' + u'</button>'

        responseList.append(rowDict)
    return responseList

def change_data(ticket_id, ticket_type, ticket_priority,
                ticket_status, conversation_id, admin_id):

    param_tup = (str(ticket_type), str(ticket_priority), str(ticket_status), str(conversation_id), str(admin_id), str(ticket_id), )
    conn = mdb.connect(host=config.get('admin_panel_db', 'host'),
                       user=config.get('admin_panel_db', 'user'),
                       passwd=config.get('admin_panel_db', 'passwd'),
                       db=config.get('admin_panel_db', 'db'),
                       charset=config.get('admin_panel_db', 'charset'))
    c = conn.cursor()
    c.execute('UPDATE ' + config.get('admin_panel_db', 'tickets_table') + ''' SET
    id_type = %s,
    priority = %s,
    status = %s,
    conversation_id = %s,
    admin_id = %s
    WHERE id_ticket = %s''', param_tup)
    conn.commit()

    conn.close()
    return

if __name__ == "__main__":
    print get_data()