#!/usr/bin/python3
"""Set up HDX demo server
Started 2016-06-04 by David Megginson
"""

import ckanapi
import urllib
import pprint

# read configuration values from config.py
import config

#
# Create the CKAN API object
#
ckan = ckanapi.RemoteCKAN(config.CONFIG['ckanurl'], apikey=config.CONFIG['apikey'], user_agent=config.CONFIG.get('user_agent', None))

#
# Delete old Foolandia datasets (and create Foolandia if necessary)
#
try:
    print("Try deleting any old Foolandia datasets...")
    foo = ckan.action.group_show(id='foo') # will fail if it doesn't exist
    # delete and purge any datasets belonging to Foolandia
    for dataset in foo.get('packages'):
        print("  ... deleting dataset " + dataset['name'])
        ckan.action.package_purge(id=dataset['id'])
except:
    print("Foolandia did not exist ... creating")
    ckan.action.group_create(
        id='foo',
        name='foo',
        title='Foolandia (demo)',
        display_name='Foolandia (demo)',
        description='Fake country for training and demos'
    )
    print("  ... created new, empty Foolandia")


exit(0)

# end
