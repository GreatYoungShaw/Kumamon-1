'''
Created on Dec 26, 2013

@author: scanlom
'''

import configparser, os

config = configparser.SafeConfigParser()
config.read(os.path.expanduser('~/.Kumamon'))
config_email_server     = config.get('Email','Server')
config_email_port       = config.getint('Email','Port')
config_email_user       = config.get('Email','User')
config_email_password   = config.get('Email','Password')
config_email_fumi       = config.get('Email','Fumi')
config_database_connect = config.get('Database','Connect')

config_backup           = 'Backup'
config_dropbox_dir      = os.path.expanduser('~/Dropbox/') + config_backup + '/'
config_backup_days      = 5
config_backup_tmp_dir   = os.path.expanduser('~/') + config_backup + '/'
config_backup_zip_dirs  = [ 
                [ os.path.expanduser('~/Mike'), 'Mike' ], 
                [ os.path.expanduser('~/bin'), 'bin' ],
                [ os.path.expanduser('~/misc'), 'misc' ],
                [ os.path.expanduser('~/dev'), 'dev' ],                
                [ os.path.expanduser('~/.vim'), '.vim' ],                
            ] 
