from pathlib import Path

import peewee as pv
from playhouse.sqlite_ext import SqliteExtDatabase

db_path = Path('daypilot.sqlite')
if not db_path.parent.exists():
    print("Database doesn't exists. Will be created a new one.")
    db_path.parent.mkdir()
db = SqliteExtDatabase(str(db_path), pragmas=(
    ('journal_mode', 'wal'),
    ('foreign_keys', 1),
))


class events(pv.Model):
    id = pv.IntegerField(primary_key=True)
    name = pv.CharField()
    start = pv.DateTimeField()
    end = pv.DateTimeField()
    resources_id = pv.CharField()

    class Meta:
        database = db


class groups(pv.Model):
    id = pv.IntegerField(null=False, primary_key=True)
    name = pv.CharField()

    class Meta:
        database = db


class resources(pv.Model):
    name = pv.CharField()
    group_id = pv.IntegerField()

    class Meta:
        database = db
