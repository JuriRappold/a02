#!/usr/bin/env make

# Change this to be your variant of the python command
# Set the env variable PYTHON to another value if needed
# PYTHON=python3 make version
PYTHON ?= python # python3 py

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

all:


# ---------------------------------------------------------
# Check the current python executable.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version


# ---------------------------------------------------------
# Setup a venv and install packages.
#
venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc: clean
	@$(call MESSAGE,$@)
	rm -rf doc

clean-all: clean clean-doc
	@$(call MESSAGE,$@)
	rm -rf .venv


# ---------------------------------------------------------
# Work with static code linters.
# `guess` changed to `program`
pylint:
	@$(call MESSAGE,$@)
	$(PYTHON) -m pylint program/*.py > doc_files/pylint/pylint_report_program.txt 2>&1
	$(PYTHON) -m pylint tests/*.py > doc_files/pylint/pylint_report_tests.txt 2>&1


flake8:
	@$(call MESSAGE,$@)
	-flake8 program/ > doc_files/flake/flake_report_program.txt 2>&1
	-flake8 tests/ > doc_files/flake/flake_report_tests.txt 2>&1

lint: flake8 pylint


# ---------------------------------------------------------
# Work with codestyle.
#
black:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m black program/ tests/

codestyle: black


# ---------------------------------------------------------
# Work with unit test and code coverage.
#
unittest:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m tests/dice_unit_tests.py

coverage:
	@$(call MESSAGE,$@)
	coverage run -m tests/dice_unit_tests.py
	coverage html
	coverage report -m

coverage-xml:
	@$(call MESSAGE,$@)
	coverage run -m pytest tests/dice_unit_tests.py
	coverage xml

test: lint coverage


# ---------------------------------------------------------
# Work with generating documentation.
#
.PHONY: pydoc
pydoc:
	@$(call MESSAGE,$@)
	install -d docs_gen/pydoc
	$(PYTHON) -m pydoc -w program/*.py
	mv *.html docs_gen/pydoc

pdoc:
	@$(call MESSAGE,$@)
	pdoc --force --html --output-dir doc_files/pdoc program/*.py

pyreverse:
	@$(call MESSAGE,$@)
	install -d doc/pyreverse
	pyreverse -a1 -s1 program/*.py
	dot -Tpng classes.dot -o doc_files/pyreverse/classes.png
	dot -Tpng packages.dot -o doc_files/pyreverse/packages.png
	rm -f classes.dot packages.dot

doc: pdoc pyreverse #pydoc sphinx



# ---------------------------------------------------------
# Calculate software metrics for your project.
#
radon-cc:
	@$(call MESSAGE,$@)
	radon cc --show-complexity --average program

radon-mi:
	@$(call MESSAGE,$@)
	radon mi --show program

radon-raw:
	@$(call MESSAGE,$@)
	radon raw program

radon-hal:
	@$(call MESSAGE,$@)
	radon hal program

cohesion:
	@$(call MESSAGE,$@)
	cohesion --directory program

metrics: radon-cc radon-mi radon-raw radon-hal cohesion



# ---------------------------------------------------------
# Find security issues in your project.
#
bandit:
	@$(call MESSAGE,$@)
	bandit --recursive guess
# ---------------------------------------------------------
# own cmds
pytest:
	@$(call MESSAGE,$@)
	-cd tests && pytest dice_unit_tests.py
