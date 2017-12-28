# bcc-cms
Django/Wagtail Collective Website

# Development Requirements
### virtual environment
- [pyenv](https://github.com/pyenv/pyenv) - manage python versions
- [pyenv virtualwrapper](https://github.com/pyenv/pyenv-virtualenvwrapper) - create virtual environment

### dependencies
- `pip install -r requirements.txt`

### database
First time Postgres setup:
- Create the `bcc` database
- `./manage.py migrate`
- `./manage.py createsuperuser`


# Run Server
Set missing global environment variables in `.env`:
- `./manage.py runserver`