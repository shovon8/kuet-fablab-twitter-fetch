# Installation
I used Python3 to write this program. For this program to work, you must have 'tweepy' Python3 module installed.

On Debian/Ubuntu you can install tweepy for Python3 with the following command:

> $ sudo apt-get install python3-tweepy



Or from PIP3, you may be able to install it with the following command:

on Linux Based Systems:
> $ sudo -H pip3 install tweepy

on Windows:
> pip3 install tweepy










# Basic Usage
To run this program, you need a Twitter account. Signup for Twitter and go to https://apps.twitter.com. Then create a
new Twitter App. Then generate the required access and consumer tokens. Once you have the tokens, run the
following script to generate a configuration file.
> $ python3 genconfig.py

It should ask you for access and consumer token, provide the tokens correctly. It should create a file 'config.py'
under your project's root.

Then you can run the app using the following command to view the last Tweet:
> $ python3 app.py

or pass a tweet as an argument to post it on Twitter
> $ python3 app.py "YOUR_TWEET"
