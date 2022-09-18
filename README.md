
![Logo](https://startupdecks.co/wp-content/uploads/2020/08/logo-5.svg)


# Startup Scrapping

A Web Scrapping project, which extracts multimedia from Startup Decks (https://startupdecks.co/decks/) and stores it in your local directory.

## Overview

This is a web scrapping project, which is used to represent how information like text, multimedia and various hyperlinks from a webpage, irrespective of it's static or dynamic nature.

## About Startup Decks

StartupDecks is the leading resource for startup pitch decks. See what leading companies like Airbnb, Facebook and more did to raise their rounds.
Find out more at https://startupdecks.co/


## Tech Stack
This project is made using **Python**. The various Python libraries used for the same are mentioned below:

- **Web Scrapping:** BeautifulSoup 4, Selenium
- **Driver Auto-Installation:** chromedriver-autoinstaller
- **HTML Parsing:** html5lib
- **URL Calling and Requests:** urllib3, requests
- **Encodings:** webencodings, charset-normalizer

## Installation

Since the project is built completely in Python, installing the project is pretty simple.
Follow the steps below

- Open your Terminal.
- Change the current working directory to the location where you want the cloned directory.
- Run the command below to clone the project:

```pip
git clone https://github.com/hiferli/Startup-Scrapping.git
```
- After the cloning is done, use the following code to enter the current working directory
```pip
cd Startup-Scrapping
```
- You can execute the code after this step. However, to run the code with optimum dependancies, install ```virtualenvironment``` using the code below:
```pip
pip install virtualenv
```
- Following this, create a virtual environment using the code below
```pip
virtualenv Environment
```
- Run the code below to activate the environment
```pip
source Environment/Scripts/bin/activate
```
- Install the dependancies
```pip
pip install -r requirements.txt
```
- You're all set to go now.

## Run the Application
To run the program:
- Open Command Prompt in the same directory as the project
- Run the command below:

```python
python main.py
```

## Contributing

Contributions are always welcome!

Please fork the project in your account and create a local repository of the same. 
Create pull requests for any Contributions. I'll be more than happy to add authors to the repository.