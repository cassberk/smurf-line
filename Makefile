SHELL := /bin/bash
.DEFAULT := help

.PHONY: format
format            : ## reformats code
	black smurf_line
	ruff --fix smurf_line
