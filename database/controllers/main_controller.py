from pydal import DAL, Field
from pydal.migrator import InDBMigrator
from datetime import date
from database.controllers.create_entry import create_entry  as create
import database.db_schema as db_schema
from database.controllers.db_wrappers import autocommit
import logging

class main_controller:
    def __init__(self, uri = 'sqlite://storage.sqlite'):
        self.db = db_schema.connect_to_db(uri)
        self.create = create(self.db)

    def set_twitch(self, discord_tag, twitch_tag):
        x = self.db.user.discord_tag == discord_tag
        user = self.db(x).select().first()
        user.twitch_tag = twitch_tag
        user.update_record()
        self.db.commit()

    def set_discord(self, twitch_tag, discord_tag):
        x = self.db.user.twitch_tag == twitch_tag
        user = self.db(x).select().first()
        user.discord_tag = discord_tag
        user.update_record()
        self.db.commit()

    def add_user_points(self):
        pass

    def add_poll_points(self):
        pass

    def change_poll_total(self):
        pass

    