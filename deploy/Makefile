#!/bin/bash

install:
	pip3 install -r requirements.txt

test:
	py.test -s -v tests

test-html:
	py.test -s -v --html=docs/test-html/test_report.html

coverage-report: clean-pyc
	py.test --cov-report html:docs/coverage-html --junit-xml=xunit-reports/xunit-report.xml \
	--cov=. tests/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean: clean-pyc
	rm -rf ./docs/api-html
	rm -rf ./docs/allure-results
	rm -rf ./docs/coverage-html
	rm -f .coverage

doc:
	apidoc -i docs/ -o docs/api-html

docker-doc: clean doc test-html coverage-report
	docker build -t research_management-api-doc:latest ./docs

