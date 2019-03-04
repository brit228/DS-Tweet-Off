"""SQLAlchemy models for Flask app."""
from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()


class TwitterUser(DB.Model):
    """Twitter users to pull tweets from."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Tweet(DB.Model):
    """Twitter tweets."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))
    user_id = DB.Column(DB.BigInteger,
                        DB.ForeignKey('twitter_user.id'),
                        nullable=False)
    user = DB.relationship('twitter_user',
                           backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
