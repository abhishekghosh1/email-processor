#### Email Preprocessor API

### Usage
Email Preprocessor API requires python 3.6.8
```bash
    https://www.python.org/ftp/python/3.6.8/python-3.6.8-macosx10.6.pkg
```

Pre-required Setup:

MacOS/Linux/Windows

git

Python3 / pip3 /

### Activating virtual Environment

```bash
$ python3.6 -m venv venv    # Create virtual environment. Run it only once
$ source venv/bin/activate # Activate virtual environment
```

### Install requi

pip install -r requirements.txt

### Service Up and running

```bash
$ docker-compose -f docker-compose.services.yml up -d 
```

### migrate database for initial setup
    python3.6 manage.py db init
    python3.6 manage.py db migrate --message 'initial database migration'
    python3.6 manage.py db upgrade

### Terminal commands

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

    For testing authorization, url for getting all user requires an admin token while url for getting a single
    user by public_id requires just a regular authentication.
