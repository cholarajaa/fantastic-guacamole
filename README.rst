after cloning
cd notify
# Install docker-compose
run
  - virtualenv dockercompose
  - source dockercompose/env/bin/activate
  - pip install docker-compose

# set up django project
run
  - docker-compose build
  - docker-compose run web django-admin startproject notifier .
 
