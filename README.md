# Welcome to Hacking Science
[![Build Status](https://travis-ci.org/hacking-science/hacking-science-website.svg?branch=master)](https://travis-ci.org/hacking-science/hacking-science-website)
We are here to do something...

## Quickstart
````
git clone https://github.com/hacking-science/hacking-science-website.git
cd hacking-science-website
sudo apt-get install python-pip python-dev build-essential
sudo pip install virtualenv virtualenvwrapper
sudo pip install --upgrade pip
printf '\n%s\n%s\n%s' '# virtualenv' 'export WORKON_HOME=~/virtualenvs' \
'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
source ~/.bashrc
mkdir -p $WORKON_HOME
mkvirtualenv hacking-science-website
workon hacking-science-website
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
````