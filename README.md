# Dev Assessment - Webhook Receiver

Please use this repository for constructing the Flask webhook receiver.

*******************

## Setup

* Create a new virtual environment

```bash
pip install virtualenv
```

* Create the virtual env

```bash
virtualenv venv
```

* Activate the virtual env

```bash
venv\scripts\activate
```

* Install requirements

```bash
pip install -r requirements.txt
```

* Run the flask application (In production, please use Gunicorn)

```bash
python run.py
```

* The endpoint is at:

```bash
http://127.0.0.1:5000/webhook/receiver
```

* Note: The project has one limitation:
The project only displays the actions of "pull_request", I could not figure it out for push and merge,  as I donot have complete understanding of Git.


*******************
