ENV = env
PYBIN = $(ENV)/scripts
PYTHON = $(PYBIN)/python
PIP = $(PYBIN)/pip
PYTEST = $(PYTHON) -m pytest
COVERAGE = $(PYTHON) -m coverage
PYFLAKE8 = $(PYTHON) -m flake8
TESTDIR = tests
MODULE_NAME = ksuid
DEV_CONFIG_FILE = ./conf/reqlog-dev.conf

SHELL=C:/Windows/System32/cmd.exe
VIRTUALENV_APP_P27 = d:/Python27/python.exe -m virtualenv

.PHONY: environ
environ: clean requirements-dev.txt
	virtualenv $(ENV)
	$(PIP) install -r requirements-dev.txt
	
.PHONY: environ_p27
environ_p27: clean requirements-dev.txt
	$(VIRTUALENV_APP_P27) $(ENV)
	$(PIP) install -r requirements-dev.txt

.PHONY: help
help:
	@echo "make                 # create virtual env and setup dependencies"
	@echo "make tests           # run tests"
	@echo "make coverage        # run tests with coverage report"
	@echo "make lint            # check linting"
	@echo "make flake8          # alias for `make lint`"
	@echo "make clean           # remove more or less everything created by make"

.PHONY: tests
tests:
	$(PYTEST) $(TESTDIR) -vv

.PHONY: coverage
coverage:
	$(PYTEST) $(TESTDIR) -vv --cov=$(MODULE_NAME)
	$(COVERAGE) html

.PHONY: lint
lint:
	$(PYFLAKE8)
	
.PHONY: flake8
flake8:
	$(PYFLAKE8)

.PHONY: clean
clean:
	if exist $(ENV) rd $(ENV) /q /s
	if exist reqlog.egg-info rd reqlog.egg-info /q /s
	if exist .coverage del .coverage
	del /S *.pyc
