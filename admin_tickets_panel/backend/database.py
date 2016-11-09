import sqlite3

def get_data(time, title, description, ticket_type,
             domain, status, userid, order):
    conn = sqlite3.connect('tickets.sqlite')
    c = conn.cursor()

    param_tup = ()
    param_tup = param_tup + ticket_type + domain + status + order

    response = []
    for row in c.execute('''SELECT * FROM tickets WHERE
                 ticket_type IN (''' +
              ",".join("?"*len(tuple(ticket_type))) + ''') AND
                 domain IN (''' +
              ",".join("?" * len(tuple(domain))) + ''') AND
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
        rowDict['time'] = row[0]
        rowDict['title'] = row[1]
        rowDict['description'] = row[2]
        rowDict['ticket_type'] = row[3]
        rowDict['domain'] = row[4]
        rowDict['status'] = row[5]
        rowDict['userid'] = row[6]
        responseList.append(rowDict)
    return responseList

if __name__ == "__main__":
    get_data(0,0,0,('zftsh',), ('abitu','zftsh',), ('solved',), 0, ('time',))
