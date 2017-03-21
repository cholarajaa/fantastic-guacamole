after cloning
cd notify
# Install docker-compose
run
  - virtualenv dockercompose
  - source dockercompose/env/bin/activate
  - pip install docker-compose
  - cd static
  # to set up javascript dependencies
  run 
    - npm install
    - node_modules/bower/bin/bower install
# set up django project
run
  - docker-compose build
  - docker-compose run web python manage.py makemigrations notification
  - docker-compose run web python manage.py migrate

# run django server with celery
run
  - docker-compose up

# to test the code
run
  - docker-compose run web python manage.py test --settings=notifier.settings_testing

RESOURCES REFFERED
https://docs.djangoproject.com/en/1.10/
https://material.angularjs.org/latest/getting-started
https://docs.angularjs.org/tutorial
http://www.django-rest-framework.org/api-guide
https://github.com/pydanny/cookiecutter-django
https://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery
https://github.com/dockerfile
http://stackoverflow.com/questions/10543940/check-if-a-url-to-an-image-is-up-and-exists-in-python/10543969#10543969
