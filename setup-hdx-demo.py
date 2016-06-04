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
    try:
        print("Deleting all datasets in group {} ({}) ...".format(group['id'], group['title']))
        group = ckan.action.group_show(id=group['id']) # will fail if it doesn't exist
        clear_datasets(group)
    except:
        print("Group {} ({}) did not exist: creating an empty version ...".format(group['id'], group['title']))
        ckan.call_action('group_create', group)
        print("  ... created new, empty group")


# Reset the Foolandia (foo) demo country
reset_group({
    'id': 'foo',
    'name': 'foo',
    'title': 'Foolandia',
    'display_name': 'Foolandia (demo)',
    'description': 'Fake country for training and demos'
})

exit(0)

# end
