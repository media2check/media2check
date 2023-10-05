#Function to find whether the post is the original and if not, find the original post.
# Twitter API tweepy used, credential and authenticate here removed for security reasons

# Insert twitter ID for checkup on 'id_to_check' to find the original tweet
tweet_id = 'id_to_check'
def get_original_poster_user_id(tweet_id):
    try:
        tweet = api.get_status(tweet_id)
        user_id = tweet.user.id_str  # Get the user's ID as a string
        return user_id
    except tweepy.TweepError as e:
        print(f"Error: {e}")
        return None
