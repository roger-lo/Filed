.PHONY: test

init:
	pip install -r requirements.txt

test:
	# pytest doesn't play nice with travis.
	py.test
