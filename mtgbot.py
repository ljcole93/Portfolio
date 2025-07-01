#  Hopefully a working deal checking bot



import praw
import time
from requests import post

# Your Reddit credentials
client_id = 'E7WF-ATV_Z-B8LyuKEtC7Q'
client_secret = 'qQw_Zr_w7tkS65mXL5Sv8Np61IBeow'
user_agent = 'y_mtgbot_v1'
pushover_user_key = 'u5y9toezy4cbqyakqzivozi7pf3dk7'
pushover_api_token = 'awnro8s25d7wfkac38t18oprz48pzj'

# Create a Reddit instance
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

# Function to send notification using Pushover
def send_notification(title, url):
    message = f"New deal: {title}\n{url}"
    payload = {
        'user': pushover_user_key,
        'token': pushover_api_token,
        'message': message
    }
    post("https://api.pushover.net:443/1/messages.json", data=payload)

# Function to check new posts
def check_for_new_posts(last_seen_id):
    subreddit = reddit.subreddit('sealedmtgdeals')
    # Get the latest post (you can adjust this to get a list of posts or top posts as well)
    for submission in subreddit.new(limit=1):
        if submission.id != last_seen_id:  # Check if it's a new post
            send_notification(submission.title, submission.url)
            return submission.id  # Return the ID of the new post to track
    return last_seen_id  # Return the same ID if no new posts

# Track the last seen post ID
last_seen_id = None

# Run the script in a loop
while True:
    last_seen_id = check_for_new_posts(last_seen_id)
    time.sleep(60)  # Wait for 1 minute before checking again
