# Open election system

## Adding secret keys
In the root directory create a file **env_variables.yaml** and paste the following content:
```shell
env_variables:
  FIREBASE_PROJECT_ID: 'project_id'
  GAE_USE_SOCKETS_HTTPLIB : 'true'
```
## Running  a project

### ubuntu
```shell
virtualenv -p python3 .venv
source .venv/bin/activate
python3 setup.py develop
gunicorn --bind 0.0.0.0:8080 wsgi
```
### windows
```shell
python3 -m venv venv
source venv/bin/activate
python3 setup.py develop
python3 wsgi.py
```

## Explore Swagger

<p>Local version: https://0.0.0.0:8080/api/1/ </p>
<p>Development version: https://lyrical-amulet-276713.ew.r.appspot.com/api/1/ </p>