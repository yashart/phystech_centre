import requests
import ConfigParser
import MySQLdb as mdb

config = ConfigParser.RawConfigParser()
config.read('db_config.cfg')

def get_id(cookies, url='http://abitu.net'):
    r = requests.get(url, cookies=cookies)
    splitRequest = r.text.split('id : ')
    if len(splitRequest) != 3:
        return -1
    return int(splitRequest[1].split(',')[0])

def is_admin(userId):
    if(userId == -1):
        return False

    conn = mdb.connect(host=config.get('admin_panel_db', 'host'),
                       user=config.get('admin_panel_db', 'user'),
                       passwd=config.get('admin_panel_db', 'passwd'),
                       db=config.get('admin_panel_db', 'db'),
                       charset=config.get('admin_panel_db', 'charset'))
    c = conn.cursor()

    c.execute('SELECT level_id FROM ' + config.get('admin_panel_db', 'users_table') + ' WHERE user_id = ' + str(userId))
    rows = c.fetchall()
    conn.close()

    for row in rows:
        if (row[0] == 1) or (row[0] == 2):
            return True
        else:
            return False

    return False