import json

from .manage_db_connection import use_database
from .model_architecture import *


@use_database(db_instance=db)
def db_init():
    try:
        if events.__name__.lower() not in db.get_tables():
            db.create_tables([events])
        if groups.__name__.lower() not in db.get_tables():
            db.create_tables([groups])
            groups.create(id=1, name='People')
            groups.create(id=2, name='Tools')
        if resources.__name__.lower() not in db.get_tables():
            db.create_tables([resources])
            resources.create(group_id=1, name='Person 1')
            resources.create(group_id=1, name='Person 2')
            resources.create(group_id=1, name='Person 3')
            resources.create(group_id=2, name='Tool 1')
            resources.create(group_id=2, name='Tool 2')
            resources.create(group_id=2, name='Tool 3')

        # print("Database initialization complete.")
        return True
    except Exception as e:
        print(__name__ + ": " + str(e))
        return False


@use_database(db_instance=db)
def get_backend_resources():
    db_init()
    grps = groups.select()
    response = []
    for g in grps:
        grp_dict = {}
        grp_dict['id'] = 'group_' + str(g.id)
        grp_dict['name'] = g.name

        children = resources.select(resources).where(resources.group_id == g.id).order_by(resources.name).objects()
        for child in children:
            grp_dict.setdefault('children', []).append({
                'id': child.id,
                'name': child.name
            })
        response.append(grp_dict)

    return json.dumps(response)


@use_database(db_instance=db)
def create_events(**kargs):
    db_init()
    name = kargs.get('name')
    start = kargs.get('start')
    end = kargs.get('end')
    resource = kargs.get('resource')

    res = events.create(name=name, start=start, end=end, resources_id=resource)
    response = {'result': 'OK',
                'message': 'Created with id: ' + str(res.id)}
    return json.dumps(response)


@use_database(db_instance=db)
def get_backend_events(**kargs):
    db_init()
    frm = kargs.get('frm')
    to = kargs.get('to')

    feached_events = events.select().where(frm >= events.end, to <= events.start).execute()

    response = []
    for row in feached_events:
        temp_dict = {}
        temp_dict['id'] = row.id
        temp_dict['name'] = row.name
        temp_dict['start'] = row.start
        temp_dict['end'] = row.end
        temp_dict['resource_id'] = row.resource_id

        response.append(temp_dict)

    return json.dumps(response)


@use_database(db_instance=db)
def update_backend_move(**kargs):
    id = kargs.get('id')
    start = kargs.get('newStart')
    end = kargs.get('newEnd')
    newResors = kargs.get('newResource')

    ret = events.update(start=start, end=end, resources_id=newResors).where(events.id == id).execute()

    response = dict()
    response['result'] = 'OK'
    response['message'] = 'Update successful'
