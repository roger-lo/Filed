.PHONY: test

init:
	pip install --user -r requirements.txt

test:
	pytest
