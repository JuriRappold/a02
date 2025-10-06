# Project File Structure
- a02
	- program --> the actual program files
	- test --> unit tests for the program files
	- docs_gen --> files/tools that generate documentation
		- other generators
	- doc_files --> documentation that has been generated and other documentation/note
		- generated documentation
		- other documentation
	- README.md
	- requirements.txt --> required packages (from mikael's template)
	- makefile (from mikael's template)
	- .venv
# Code Style
## Naming conventions for variables, methods, and classes
`lower_case_with_undescors` for all variables, methods/functions, and classes

## Comment Requirements
- a few sentences describing the class
- comment lambdas
- comment constants (why this value? to avoid magic numbers)
- comment complex stuff
	- logic
	- pattern matching?

## Formatting
- use new lines for each cmd
- 1 empty line between functions/methods (function comments count as part of function)
- tab = 4 spaces
- clean up code before committing and pushing
# Git & GitHub
- naming of branches (types of branches)
	- feature-branches (fea)
	- bug-branches (bug)
	- hot-fix-branches (htx)
	- unit-tests (unt)
- pull (update) from github before starting a coding session
- only merge into main branch when the branch passes all tests
`<person_responsible>/<type_of_branch>_<short_description>`<br>
Example: `Juri/fea_menu_imp`
# Preparation and After-Care for a coding session
1. pull from remote repo (main branch)
2. switch to feature branch/create new feature branch
   3. if necessary: merge new main branch into your already existing feature branch (NOT THE OTHER WAY AROUND!!!)
3. code 
4. clean up code 
5. commit at the end of coding session 
6. push to non-main branch 

# Commits
1. 2025-10-06/19:30, first initial commit
   - file structure
   - installation of required packages
   - added `.gitignore` file for jetbrains .idea directory and virtual environment
     - apparently it is best if everybody creates their own virtual environment
     - adding instructions how to create the virtual environment and the required packages tmrw