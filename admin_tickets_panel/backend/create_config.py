import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('admin_panel_db')
config.set('admin_panel_db', 'host', 'localhost')
config.set('admin_panel_db', 'user', 'test')
config.set('admin_panel_db', 'passwd', 'test')
config.set('admin_panel_db', 'db', 'admin_tickets_db')
config.set('admin_panel_db', 'tickets_table', 'tickets')
config.set('admin_panel_db', 'charset', 'utf8')


with open('db_config.cfg', 'wb') as configfile:
    config.write(configfile)
