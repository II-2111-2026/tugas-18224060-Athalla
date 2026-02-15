.PHONY: test-w01

test-w01:
	python -m pip install -r requirements.txt
	pytest -q tests_bank/w01/quiz_tests.py
