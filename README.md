# Simple Python App

This is a simple boilerplate for structuring a small, simple Python application. I typically use this whenever I need something which consists of one, or few, scripts. 

This quick setup is mainly for very small projects like one-off scripts. This is not intended for use in creating large applications, but can probably be adapted to do so.

## Setup 

```bash
git clone https://github.com/kishstats/Simple-Python-App.git <your project name>
```

Rename `myapp.py` with an appropriate file name and update its contents. The `run_myapp` method was added to this file as a placeholder.

### Setting Up a Virual Environment (optional)

```bash
pip install --upgrade virtualenv
virtualenv -p python venv
source venv/bin/activate
```

### Tests

One of the reasons why this setup is better than just using a single-file script is that unit tests have been setup. This can prevent you from having to deal with the tedious task of having to keep re-running your script manually with different inputs. 

Replace the dummy test in `tests.py` with your own.

Running Tests
```bash
python -m unittest tests.py
```

## Dependencies

This section is for any dependencies that have been added using `pip`.

Freeze list of dependencies:

```bash
pip freeze > requirements.txt
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Application Packaging (optional)

A boilerplate `setup.py` file has been created. Replace all necessary values.