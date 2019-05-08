# Coming Soon.

# Dependencies
 - Python 3.5

# Setup
```
$ conda create --name news-worker python=3.6
$ conda activate news-worker
$ pip install -r requirements.txt
```

# Running the worker
```
$ python3 news-worker --news-api-key=YOUR_KEY_HERE
```

# Config
The app requires a `config.json` to run, but we have not included that. Instead, we have a `config_template.json`. You may copy/paste this and rename it `config.json`, and then change all appropriate fields for your local setup.
