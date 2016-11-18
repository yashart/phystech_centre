import sqlite3

def get_data(time, title, description, id_type, status, userid, order):
    conn = sqlite3.connect('tickets.sqlite')
    c = conn.cursor()

    param_tup = ()
    param_tup = param_tup + id_type + status + order

    response = []
    for row in c.execute('''SELECT * FROM tickets WHERE
                 id_type IN (''' +
              ",".join("?"*len(tuple(id_type))) + ''') AND
                 status IN (''' +
              ",".join("?"*len(tuple(status))) + ''')
                 ORDER BY ?
                 ''', param_tup):
        response.append(row)
    conn.close()
    return response

def make_json_from_data(database_answer):
    responseList = []
    for row in database_answer:
        rowDict = {}
        rowDict['id_ticket'] = row[0]
        rowDict['time'] = row[1]
        rowDict['id_user'] = row[2]
        rowDict['name'] = row[3]
        rowDict['email'] = row[4]
        rowDict['phone'] = row[5]
        rowDict['browser'] = row[6]
        rowDict['title'] = row[7]
        rowDict['text'] = row[8]
        rowDict['url'] = row[9]
        rowDict['id_type'] = row[10]
        rowDict['priority'] = row[11]
        rowDict['status'] = row[12]
        rowDict['conversation_id'] = row[13]
        rowDict['admin_id'] = row[14]

        responseList.append(rowDict)
    return responseList

if __name__ == "__main__":
    get_data(0,0,0,('zftsh',), ('abitu','zftsh',), ('solved',), 0, ('time',))
