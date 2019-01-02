## StackOverflow-Lite API
[![Build Status](https://travis-ci.org/wathigo/StackOverflow2.svg?branch=develop)](https://travis-ci.org/wathigo/StackOverflow2)

This is a project aimed at developing API endpoints for the StackOverflow-lite.
StackOverflow-lite is a platform where users can ask questions, contribute to answering question or even comment on the answers already provided.
Here are the concepts that are necessary for completion of this project
1. Pivotal tracker [here](https://www.pivotaltracker.com/n/projects/2232261)
2. Test Driven Development(TDD)
3. Git and version Control
4. Object Oriented Programming
5. Data structures
6. Continous Integration with TavisCl
7. Flask-restful

### Getting Started
This project requires a number of the following packages installed.

### Prerequisites
1. Pip
2. Python 3.6

### How to run API
1. Enter 'git clone https://github.com/wathigo/StackOverflow2.git' to clone this repository.
2. Install a virtual environment 'pip install virtualenv'.
3. Create a virtual environment 'virtualenv myenv'
4. Activate the environment 'source myenv/bin/activate'.
5. Install the necessary packages 'pip install -r requirements.txt'.
6. Enter 'Flask run' to test the API.

### Running Tests
Enter 'coverage run --source=app -m pytest && coverage report' command to run tests.

### Author
Simon Wathigo
