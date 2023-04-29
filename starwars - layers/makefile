.DEFAULT_GOAL := build

build:
	docker build -t my-flask-app .
.PHONY: build

run:
	docker run -p 3000:3000 my-flask-app
.PHONY: run
