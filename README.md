# Twitter CLI

## Description 
Twitter CLI is a simple python CLI tool that uses thw tweepy package to interact
with Twitter thorugh OAuth and the Twitter API.

This project is meant to provide me practice with using the Twitter API.


## Setup
Copy the env.example file and remane it .env. Make sure to add the required info.
(Can get keys through Twitter Development console)
```
cp env.example .env
```

Make you are in the folder
```
cd  twitter_bot_example
```

Setup virtual environment and activate it,
```
python -m venv venv
source .venv/bin/activate
```

Install dependecies, 
```
pip install -r requirements.txt
```

Start the CLI tool using script or manually,
```
./run
```
or
```
python twitter_cli/cli.py
```