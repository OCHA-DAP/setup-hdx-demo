## Setup script for the HDX demo server

_Started June 2016 by David Megginson_

Set up a demo server with a fake country called "Foolandia", 20 demo organisations, and 40 user accounts (1 admin and 1 editor for each organisation).

The short name for Foolandia will be "foo".

The short names for the demo orgs will be "demo_org_1", "demo_org_2", ... "demo_org_20".

The short names for the users will be "demo_user_1a", "demo_user_1b", "demo_user_2a", "demo_user_2b", ... "demo_user_20b", where "demo_user_1a" is an admin for "demo_org_1" and "demo_user_1b" is an editor for "demo_org_1" (etc.).

If the country or organisations already exist, delete any datasets associated with it/them.

### Installation

Designed for use with Python3 (Python2 may also work, but not tested).

Install the ckanapi module:

    pip install ckanapi

Copy the file ``config.py.TEMPLATE`` to ``config.py`` and fill in the appropriate values. Your user name and API key are available from CKAN when you are logged in; talk to the CKAN sysadmin to find out if a user-agent string is required (to get around HTTP basic authentication).

### Usage

```
python3 setup-hdx-demo.py
```

The script will print progress reports to standard output.
