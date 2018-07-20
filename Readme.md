django-react
1. install python 3.6.6
2. pipenv --three
	this command created a pipfile.
3. pipenv install django djangorestframework
4. pipenv shell
5. pipenv install coverage --dev
	run: coverage run --source='.' manage.py test
	     coverage html - generate html report

6. python manage.py runserver 7000 
	http://localhost:7000/api/lead/
7. load test data
	python manage.py loaddata leads
8. create-react-app react-ts --scripts-version=react-scripts-ts
9. git init
10. python manage.py runserver 7000 (my local 8000 is used)
11. npm start
12. Update git repo author info
