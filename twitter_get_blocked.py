import tweepy
from twitter_credentials import consumer_key, consumer_secret, bearer_token, access_token, access_token_secret

def save_usernames_to_file(user_ids, filename="blocked_users.txt"):
    """
    Saves a list of user_id to a text file, with each user_id on a new line.
    
    Parameters:
    - user_ids (list): A list of user IDs to save.
    - filename (str): The name of the file to write to. Defaults to "blocked_users.txt".
    """
    try:
        with open(filename, 'w') as file:
            for user_id in user_ids:
                file.write(f"{user_id}\n")
        print(f"User IDs saved to {user_id}")
    except Exception as e:
        print(f"Error saving user IDs to file: {e}")

def get_blocked_accounts():
    """
    Retrieves blocked accounts using Tweepy API and saves their user IDs to a text file.
    """
    api = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
    
    try:
        # Retrieve blocked accounts
        blocked_accounts = api.get_blocked()
        
        # Extract user IDs
        user_ids = [account.id for account in blocked_accounts]
        
        # Save user IDs to file
        save_usernames_to_file(user_ids)
        
    except Exception as e:
        print(f"Error retrieving blocked accounts: {e}")

if __name__ == "__main__":
    get_blocked_accounts()
