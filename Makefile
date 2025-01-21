# Variables
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Creating virtual environment
$(VENV)/bin/activate: requirements.txt
	python3.11 -m venv $(VENV)
	$(PIP) install -r requirements.txt

install: $(VENV)/bin/activate

format:	
	black src/*.py tests/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py src/*.py

refactor: format lint

test:
	$(PYTHON) -m pytest -vv --cov=tests tests/test_*.py
		
all: install refactor test