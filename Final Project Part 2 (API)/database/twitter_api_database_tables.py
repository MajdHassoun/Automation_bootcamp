import sqlite3
from responses import Responses


class TwitterApiDatabaseTables:
    def __init__(self, db_name='twitter_api.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def reset_database(self):
        """Drop the user, tweet, and follower tables if they exist."""
        tables = [('user',), ('tweet',), ('follower',)]
        self.cursor.executemany('DROP TABLE IF EXISTS ?', tables)
        self.conn.commit()

    def create_user_table(self):
        """Create the user table."""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY,
            user_name TEXT NOT NULL,
            creation_date TEXT NOT NULL,
            following_count INTEGER NOT NULL,
            followers_count INTEGER NOT NULL
        )
        ''')
        self.conn.commit()

    def create_tweet_table(self):
        """Create the tweet table."""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tweet (
            tweet_id INTEGER PRIMARY KEY,
            creation_date TEXT NOT NULL,
            text TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user(user_id)
        )
        ''')

        self.conn.commit()

    def create_follower_table(self):
        """Create the follower table."""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS follower (
            follow_id INTEGER PRIMARY KEY AUTOINCREMENT,
            followed_user_id INTEGER NOT NULL,
            follower_id INTEGER NOT NULL,
            FOREIGN KEY (followed_user_id) REFERENCES user(user_id),
            FOREIGN KEY (follower_id) REFERENCES user(user_id)
        )
        ''')
        self.conn.commit()

    def insert_user(self, user_id, user_name, creation_date, following_count, followers_count):
        """Insert a new user into the user table."""
        self.cursor.execute('''
           INSERT INTO user (user_id, user_name, creation_date, following_count, followers_count)
           VALUES (?, ?, ?, ?, ?)
           ''', (user_id, user_name, creation_date, following_count, followers_count))
        self.conn.commit()

    def insert_tweet(self, tweet_id, creation_date, text, user_id):
        """Insert a new tweet into the tweet table."""
        self.cursor.execute('''
           INSERT INTO tweet (tweet_id, creation_date, text, user_id)
           VALUES (?, ?, ?, ?)
           ''', (tweet_id, creation_date, text, user_id))
        self.conn.commit()

    def insert_follower(self, followed_user_id, follower_id):
        """Insert a new follower relationship into the follower table."""
        self.cursor.execute('''
           INSERT INTO follower (followed_user_id, follower_id)
           VALUES (?, ?)
           ''', (followed_user_id, follower_id))
        self.conn.commit()

    def fetch_all_records(self, table):
        """Fetch and return all records from the students table."""
        self.cursor.execute(f'SELECT * FROM {table}')
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.conn.close()


def main():
    response = Responses()
    db = TwitterApiDatabaseTables()
    db.create_user_table()
    db.create_tweet_table()
    db.create_follower_table()
    db.insert_user(response.get_user_response("user id"), response.get_user_response("user name"),
                   response.get_user_response("creation date"), response.get_user_response("following count"),
                   response.get_user_response("follower count"))

    db.insert_tweet(response.get_tweet_response("tweet id"), response.get_tweet_response("creation_date"),
                    response.get_tweet_response("text"), response.get_tweet_response("user_id"))
    db.insert_follower(response.get_tweet_response("follower_id"), response.get_tweet_response("followed_user_id"))
    all_users = db.fetch_all_records("user")
    print("\n user:")
    for user in all_users:
        print(user)

    all_tweet = db.fetch_all_records("tweet")
    print("\n tweet:")
    for tweet in all_tweet:
        print(tweet)

    all_follower = db.fetch_all_records("follower")
    print("\n follower:")
    for follower in all_follower:
        print(follower)

    db.reset_database()
    db.close()


if __name__ == "__main__":
    main()
