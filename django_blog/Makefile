.PHONY: allcommands

git:
	git add .
	git commit -m "Building a Complete Django Application"
	git push

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

server:
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver
