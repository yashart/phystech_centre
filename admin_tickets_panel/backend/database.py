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
        #print row
        #print len(row)
        rowDict = {}
        rowDict['id_ticket'] = u'<b>' + unicode(row[0]) + u'</b>'
        rowDict['user_info'] = u'id - ' + unicode(row[1]) + u'<br>' + \
                               unicode(row[3]) + u'<br>' + \
                               unicode(row[4]) + u'<br>'
        rowDict['admin_id'] = unicode(row[2])
        rowDict['browser'] = unicode(row[6]) + u'<br>' + \
                             unicode(row[7])
        rowDict['url'] = unicode(row[8])
        rowDict['ticket_data'] = u'<b>' + unicode(row[9]) + u'</b>' + u'<br>' + \
                                 unicode(row[10])
        rowDict['screenshots'] = unicode(row[11])
        rowDict['time'] = u'creation data - ' + unicode(row[12]) + u'<br>' + \
			  u'modified data - ' + unicode(row[13])
        rowDict['id_type'] = unicode(row[14])
        rowDict['priority'] = unicode(row[15])
        rowDict['status'] = unicode(row[16])
        rowDict['conversation_id'] = unicode(row[17])
        rowDict['editButton'] = u'<button type="button" id="editButton' + unicode(row[0]) +\
                                u'" class="btn btn-primary editButton">' +\
                                u'Редактировать' + u'</button>'
        rowDict['conversation_id'] = u'<button type="button" id="conversationButton' + unicode(row[17]) +\
                                     u'" class="btn btn-primary conversationButton">' +\
                                     u'Диалог' + u'</button>'

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
    type_id = %s,
    priority = %s,
    status = %s,
    conversation_id = %s,
    admin_id = %s
    WHERE ticket_id = %s''', param_tup)
    conn.commit()

    conn.close()
    return

if __name__ == "__main__":
    print get_data()
