<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://github.com/JuriRappold/a02">
    <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgameonfamily.com%2Fcdn%2Fshop%2Farticles%2Fpig-dice-game_31697a8e-ce87-4016-a6eb-032da3b497b4.png%3Fv%3D1740172681%26width%3D1100&f=1&nofb=1&ipt=1ae888654d0fedca36ea94e995f3a9657d56e70813dd8839b594c976fe228b82" alt="pig with dice" width="250">
  </a>

  <h3 align="center">Pig (Dice Game)</h3>

  <p align="center">
    Dice Game created for Sustainable development methods
	<br> 
	<i>by Juri Rappold, Varvara Aladyina and Gunnar Arias</i>
    <br />
    <a href="https://github.com/JuriRappold/a02"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/JuriRappold/a02">View Demo</a>
    &middot;
    <a href="https://github.com/JuriRappold/a02/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/JuriRappold/a02/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- until here everything is perfect, not counting license-->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

### Project File Structure

a02<br>
├── program --> the actual program files<br>
│   └── ...<br>
├── test --> unit tests for the program files<br>
│   └── ...<be>
├── docs_gen --> files/tools that generate documentation<br>
│   └── other generators<br>
├── doc_files --> documentation that has been generated and other documentation/note<br>
│   └── generated documentation<br>
│   └── other documentation<br>
├── README.md<br>
├── requirements.txt --> required packages<br>
└── makefile (from mikael's template)<br>
<br>
Some very cool description!!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [python][Python-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* Windows
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at 
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/JuriRappold/a02/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=JuriRappold/a02" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


#other (i didn't delete anything! you can find some commented out, but not deleted)

<!-- # Project File Structure
- a02
	- program -> the actual program files
	- test -> unit tests for the program files
	- docs_gen -> files/tools that generate documentation
		- other generators
	- doc_files -> documentation that has been generated and other documentation/note
		- generated documentation
		- other documentation
	- README.md
	- requirements.txt -> required packages (from mikael's template)
	- makefile (from mikael's template)
	- .venv-->
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

<!--
# Commits
1. Juri: 2025-10-06/19:30, first initial commit
   - file structure
   - installation of required packages
   - added `.gitignore` file for jetbrains .idea directory and virtual environment
     - apparently it is best if everybody creates their own virtual environment
     - adding instructions how to create the virtual environment and the required packages tmrw
2. Juri: 2025-10-06/19:40, added .gitkeep files to add empty directories to git
   - can be removed once actual files exist in those directories
3. Juri: 2025-10:07/23:15, commit for tmrw's unit testing, added dice class, changed directory name in command in the makefile
   - added dice class
     - tried to make it static, we shouldn't need a new dice for every new game
   - changed a command in the makefile (was a directory reference)
     - `guess` -> `program`
   - linted the class, tried solving the linting errors; couldn't solve them :(
4. Juri: 2025-10-08/16:30, unit tests, fully linted dice.py, uml class diagrams, and flow chart
   - unit test with pytest
   - fully linted dice.py
   - flow chart of a turn in game
   - marked program and tests directories as python packages-->



<!--example of link: [here](https://example.com)-->
[contributors-shield]: https://img.shields.io/github/contributors/JuriRappold/a02.svg?style=for-the-badge
[contributors-url]: https://github.com/JuriRappold/a02/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JuriRappold/a02.svg?style=for-the-badge
[forks-url]: https://github.com/JuriRappold/a02/network/members
[stars-shield]: https://img.shields.io/github/stars/JuriRappold/a02.svg?style=for-the-badge
[stars-url]: https://github.com/JuriRappold/a02/stargazers
[issues-shield]: https://img.shields.io/github/issues/JuriRappold/a02.svg?style=for-the-badge
[issues-url]: https://github.com/JuriRappold/a02/issues
[license-shield]: https://img.shields.io/github/license/JuriRappold/a02.svg?style=for-the-badge
[license-url]: https://github.com/JuriRappold/a02/blob/master/LICENSE.md
[Python.org]: https://img.shields.io/badge/Python-1C05FF?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com