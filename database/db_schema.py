import datetime
import traceback
import logging

#from safelog import Log
from pydal.migrator import InDBMigrator
from pydal import DAL, Field

def connect_to_db(uri = 'sqlite://storage.sqlite'):
    db = DAL(uri,
        migrate=True,
        fake_migrate=False,
        migrate_enabled=True,
        fake_migrate_all=False,
        adapter_args=dict(migrator=InDBMigrator),
        pool_size=10)

    try:
        db.define_table(
            'user',

            Field('discord_tag', 'string'),
            Field('twitch_tag', 'string'),
            Field('points', 'integer'),
        )
    except:
        logging.debug(traceback.format_exc())
    
    try:
        discUnique = "CREATE UNIQUE INDEX discUnique ON user(discord_tag) WHERE discord_tag IS NOT NULL"
        db.executesql(discUnique)
    except:
        logging.debug(traceback.format_exc())
    
    try:
        twitchUnique = "CREATE UNIQUE INDEX twitchUnique ON user(twitch_tag) WHERE twitch_tag IS NOT NULL"
        db.executesql(twitchUnique)
    except:
        logging.debug(traceback.format_exc())

    try:
        db.define_table(
            'polls',

            Field('name', 'string'),
            Field('total', 'integer'),
            Field('amount', 'integer'),
        )
    except:
        logging.debug(traceback.format_exc())
    
    return db