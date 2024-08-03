# Twitter Blocker and Blocked Accounts Viewer

This GitHub repository contains two Python scripts designed to interact with the Twitter API for managing blocked accounts. The scripts utilize the Tweepy library to facilitate interaction with the Twitter API.

## Requirements

- Tweepy library (`pip install tweepy`)
- Basic level access to the Twitter API ($100/month)

## Scripts Overview

`twitter_block.py`

This script reads a list of user IDs from a text file (`blocked_users.txt` by default) and blocks these users using the Twitter API v2 via Tweepy. It prints out the status of each blocking operation.

`twitter_get_blocked.py`

This script retrieves the list of currently blocked accounts via the Twitter API and saves their user IDs to a text file (`blocked_users.txt` by default).

## Usage

Before running these scripts, ensure you have set up your Twitter Developer account and obtained the necessary credentials (`consumer_key`, `consumer_secret`, `bearer_token`, `access_token`, `access_token_secret`). These should be stored in a file named `twitter_credentials.py` in the same directory as the scripts.
