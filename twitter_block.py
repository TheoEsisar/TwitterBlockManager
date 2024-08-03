import tweepy
from twitter_credentials import consumer_key, consumer_secret, bearer_token, access_token, access_token_secret

def read_user_ids_from_file(filename="blocked_users.txt"):
    """
    Reads user IDs from a text file, assuming one username per line.
    
    Parameters:
    - filename (str): The name of the file to read from. Defaults to "blocked_users.txt".
    
    Returns:
    - list: A list of user IDs read from the file.
    """
    user_ids = []
    try:
        with open(filename, 'r') as file:
            user_ids = [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading usernames from file: {e}")
    return user_ids

def block_users(user_ids):
    """
    Blocks a list of users using the Twitter API v2 via Tweepy.
    
    Parameters:
    - user_ids (list): A list of user IDs to block.
    """
    api = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
    
    for user_id in user_ids:
        try:
            api.block(username=user_id)
            print(f"Blocked user with User ID {user_id}")
        except Exception as e:
            print(f"Error blocking User ID {user_id}: {e}")

if __name__ == "__main__":
    user_ids_to_block = read_user_ids_from_file()
    block_users(user_ids_to_block)
