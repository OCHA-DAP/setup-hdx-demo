#!/usr/bin/python3
"""Set up HDX demo server
Started 2016-06-04 by David Megginson
"""

import ckanapi
import config

ckan = ckanapi.RemoteCKAN(config.CONFIG['ckanurl'], apikey=config.CONFIG['apikey'], user_agent=config.CONFIG.get('user_agent', None))
"""Remote CKAN API object"""

def clear_datasets (entity):
    """Delete all datasets associated with an entity (such as a group or organization)."""
    datasets = entity.get('packages')
    if datasets:
        for dataset in datasets:
            print("Deleting dataset {}".format(dataset['name']))
            ckan.action.package_purge(id=dataset['id'])

def reset_group (group):
    """If the group exists, delete all datasets; otherwise, create it."""
    old_group = None
    try:
        # will throw an exception if group doesn't exist
        old_group = ckan.action.group_show(id=group['id']) # will fail if it doesn't exist
    except:
        print("Group {} does not exist: creating.".format(group['name']))
        ckan.call_action('group_create', group)
    else:
        print("Deleting all datasets in group {}.".format(group['name']))
        clear_datasets(group)
        #ckan.call_action('group_update', group)

def reset_user (user):
    """If the user does not exist, create it; otherwise, update."""
    old_user = None
    try:
        old_user = ckan.action.user_show(id=user['name'])
        print("Creating or updating {} ({})".format(user['name'], user['fullname']))
    except:
        print("User {} does not exist: creating.".format(user['name']))
        ckan.call_action('user_create', user)
    else:
        #print("User {} already exists: updating".format(user['name']))
        #ckan.call_action('user_update', user)
        pass

def reset_organization (org):
    """If the org exists, delete all datasets; otherwise, create it."""
    old_org = None
    try:
        # will throw an exception if org doesn't exist
        old_org = ckan.action.organization_show(id=org['name']) # will fail if it doesn't exist
    except:
        print("Organization {} does not exist: creating.".format(org['name']))
        ckan.call_action('organization_create', org)
    else:
        print("Deleting all datasets in organization {}.".format(org['name']))
        clear_datasets(old_org)
        #ckan.call_action('organization_update', org)

# Reset the Foolandia (foo) demo country
reset_group({
    'id': 'foo',
    'name': 'foo',
    'title': 'Foolandia',
    'display_name': 'Foolandia (demo)',
    'description': 'Fake country for training and demos'
})

for n in range(1, 21):
    org_id = "demo_org_{}".format(n)
    admin_id = "demo_user_{}a".format(n)
    editor_id = "demo_user_{}b".format(n)
    reset_user({
        'name': admin_id,
        'email': "{}@example.org".format(admin_id),
        'password': 'hdxdemo',
        'fullname': 'Demo User {}a'.format(n)
    })
    reset_user({
        'name': editor_id,
        'email': "{}@example.org".format(editor_id),
        'password': 'impact2016',
        'fullname': 'Demo User {}b'.format(n)
    })
    reset_organization({
        'name': org_id,
        'title': 'Demo Org {}'.format(n),
        'description': 'Temporary organization for demonstrations and tutorials',
        'users': [
            {'name': admin_id, 'capacity': 'admin'},
            {'name': editor_id, 'capacity': 'editor'}
        ]
    })

exit(0)

# end
