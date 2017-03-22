**Runing guacamole project**
| *after cloning*
| *cd repository*
| 
  **Install docker-compose**
  - virtualenv dockerenv
  - source dockerenv/bin/activate
  - pip install docker-compose
  
  **to set up javascript dependencies**
    - cd static
    - npm install
    - node_modules/bower/bin/bower install
**set up django project**
  - if in static folder: cd ..
  - docker-compose build
  - docker-compose up
  - Ctrl-C
  - docker-compose run web python manage.py migrate

**run django server with celery worker**
  - docker-compose up

**to test the code**
  - docker-compose run web python manage.py test --settings=notifier.settings_testing

:RESOURCES:
- https://docs.djangoproject.com/en/1.10/
- https://material.angularjs.org/latest/getting-started
- https://docs.angularjs.org/tutorial
- http://www.django-rest-framework.org/api-guide
- https://github.com/pydanny/cookiecutter-django
- https://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery
- https://github.com/dockerfile
- http://stackoverflow.com/questions/10543940/check-if-a-url-to-an-image-is-up-and-exists-in-python/10543969#10543969
