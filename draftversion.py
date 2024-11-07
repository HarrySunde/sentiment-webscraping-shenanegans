import praw
import requests
from typing import List, Optional
from datetime import date 


#reddit API
#resorces = https://www.youtube.com/watch?v=FdjVoOf9HN4


 

# Reddit API credentials , DO NOT ADD YOUR DETAILS HERE FOR SECURITY REASONS
username = 
password = 
public_key = 
secret_key = 

# List of subreddits to search
subreddit_list = ['wallstreetbets', 'investing',
                  'stockmarket', 'trading', 'cryptocurrency',
                  'Bitcoin', 'ethtrader', 'altcoin',
                  'crypto_currency_news', 'cryptomarkets']

# Search term
search_term = 'BitCoin'


def authenticate_reddit(username, password, public_key, secret_key):
    """Authenticate with the Reddit API."""
    reddit = praw.Reddit(client_id=public_key,
                          client_secret=secret_key,
                          username=username,
                          password=password,
                          user_agent='my_reddit_scraper/1.0')

    return reddit


def fetch_post_text(reddit, subreddit_list, search_term):
    """Fetch post text from specified subreddits."""
    post_text = []

    for subreddit_name in subreddit_list:
        subreddit = reddit.subreddit(subreddit_name)

        # Search the subreddit for the specified term
        search_results = subreddit.search(search_term, sort='relevance', limit=10)

        # Iterate through the search results and append the post title and selftext to the post_text list
        for submission in search_results:
            post_text.append(submission.title + "\n" + submission.selftext)

    return post_text

def save_post_text(post_text, filename):
    current_date = date.today()

    formatted_date = current_date.strftime("%m-%d-%Y")

    # Create a filename with the current date
    filename = 'post_text_{}.txt'.format(formatted_date)
    """Save the post text to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        for text in post_text:
            file.write(text + '\n')


def main():
    reddit = authenticate_reddit(username, password, public_key, secret_key)
    post_text = fetch_post_text(reddit, subreddit_list, search_term)
    save_post_text(post_text, 'post_text.txt')
    print("Post text stored in post_text.txt")


if __name__ == '__main__':
    main()
