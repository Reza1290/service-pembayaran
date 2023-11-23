

- create a virtual environment `python -m venv venv` (if you use another name, adjust .gitignore)

- enable virtual env `venv/bin/activate`

- install dependencies `pip install -r requirements.txt`

- Running Server: `python server.py` or `FLASK_APP=server.py python -m flask run`

- Running CLI Commands: `FLASK_APP=server.py python -m flask <command name>`