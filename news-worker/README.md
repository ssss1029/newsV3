# Coming Soon.

# Dependencies
 - Python 3.5
 - Java (For boilerpipe3. Make sure JAVA_HOME is set properly)
 - gcc (For boilerpipe3. Make sure you're using the gcc from your conda environment)

# Setup
```
$ conda create --name news-worker python=3.6
$ conda activate news-worker
$ conda install -c anaconda gcc # Needed for boilerpipe's C++ compilation
$ pip install -r requirements.txt
```

# Running the worker
```
$ python3 news-worker --news-api-key=YOUR_KEY_HERE
```

# Config
The app requires a `config.json` to run, but we have not included that. Instead, we have a `config_template.json`. You may copy/paste this and rename it `config.json`, and then change all appropriate fields for your local setup.
