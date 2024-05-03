SHELL := /bin/bash
.DEFAULT := help

.PHONY: format
format            : ## reformats code
	black smurf_line
	ruff --fix smurf_line

.PHONY: launch-rest-api
launch-rest-api            :
	. .venv/bin/activate && uvicorn smurf_line.app.main:app --reload
