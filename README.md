# Capital City Guessing Game

A simple Django-based web application to guess the capital city of a random country.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)
  - [Database Setup](#database-setup)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This web application is a simple guessing game that presents the user with a random country and asks them to guess its capital city. It provides feedback on whether the answer is correct or not.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Django installed
- An internet connection to fetch country data (optional, see Database Setup)

## Getting Started

Follow these steps to set up and run the project in a new environment:

### Clone the Repository

Clone the repository to your local machine using the following command:


git clone https://github.com/Samarth-Baronia/capital-city-guessing-game.git

Setting Up a Virtual Environment
It's recommended to use a virtual environment to manage project dependencies. Create a virtual environment by running:


## python3 -m venv venv

Activate the virtual environment:

## For Linux/macOS:

source venv/bin/activate

## For Windows (PowerShell):

.\venv\Scripts\Activate

## Installing Dependencies
## Install the project dependencies using pip:


pip install -r requirements.txt

## By default, the project uses a SQLite database. To set up the database and populate it with country data, run the following commands:

python manage.py migrate
python populate_db.py

If you prefer to use a different database, update the DATABASES configuration in settings.py accordingly.

Running the Application
Start the Django development server:

python manage.py runserver
The application should now be running locally. Access it in your web browser at http://localhost:8000/.

Usage
Visit http://localhost:8000/ in your web browser.
Guess the capital city of the displayed country.
Press the "Check" button to see if your guess is correct.

![image](https://github.com/Samarth-Baronia/capital-city-guessing-game/assets/61177336/68b3bb9b-2983-4250-af17-6c8e6bbddc88)


Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your fork.
Create a pull request to the main repository.
