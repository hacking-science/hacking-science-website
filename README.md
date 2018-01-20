# Welcome to Hacking Science
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Build Status](https://travis-ci.org/hacking-science/hacking-science-website.svg?branch=master)](https://travis-ci.org/hacking-science/hacking-science-website)
[![codecov](https://codecov.io/gh/hacking-science/hacking-science-website/branch/master/graph/badge.svg)](https://codecov.io/gh/hacking-science/hacking-science-website) 
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e897ffd108c344e9a81de621df3c2698)](https://www.codacy.com/app/hacking-science/hacking-science-website)
[![Known Vulnerabilities](https://snyk.io/test/github/hacking-science/hacking-science-website/badge.svg)](https://snyk.io/test/github/hacking-science/hacking-science-website) 

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/hacking-science/hacking-science-website)
## Info
Hacking Science is...

## Quickstart

### PreReq
Should only need to do this if it your 1st time with Python and virtual enviroments
```bash
sudo apt-get install python-pip python-dev build-essential
sudo pip install virtualenv virtualenvwrapper
sudo pip install --upgrade pip
printf '\n%s\n%s\n%s' '# virtualenv' 'export WORKON_HOME=~/virtualenvs' \
'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
source ~/.bashrc
mkdir -p $WORKON_HOME
```

### Using Virtualenv
````bash
git clone https://github.com/hacking-science/hacking-science-website.git
cd hacking-science-website
virtualenv virtualenv-hacking-science-website 
source virtualenv-hacking-science-website/bin/activate 
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
````

### Using Virtualenv Wrapper
````bash
git clone https://github.com/hacking-science/hacking-science-website.git
cd hacking-science-website
mkvirtualenv hacking-science-website
workon hacking-science-website
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
````

## Testing
Within your virtual environment run the following command
````bash
python manage.py test
````
