from pydal import DAL, Field

from datetime import date
from database.controllers.db_wrappers import autocommit
"""
All functions in this file follow the same format.
Each function creates a new entry in the database
@param db: The Database pointer
@param param#: All variables to be put into the created object in the database
@return: returns the object that was inserted into the database
"""
class create_entry:
    def __init__(self, db):
        self.db = db

    @autocommit
    def create_user(
        self,
        discord_tag = None,
        twitch_tag = None,
        points = 0
    ):
        ret = self.db.user.insert(discord_tag = discord_tag, twitch_tag = twitch_tag, points = points)
        return ret

    @autocommit
    def create_polls(
        self,
        name='',
        total = 0,
        amount = 0,
    ):
        ret = self.db.user.insert(name = name, total = total, amount = amount)
        return ret