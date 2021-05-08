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

* Note: The project has two limitations:

* 1. The project only displays the actions of "pull_request", I could not figure it out for push and merge as I donot have complete knowledge of Git.
* 2.The projects loads whenever there is a "pull_request" from the user. I have tried using Jenkins to update the application every 15 seconds, but it would require a separate flask folder which is not ideal for this project.

*******************
