.PHONY: test

init:
	pip install -r requirements.txt

test:
	pytest
