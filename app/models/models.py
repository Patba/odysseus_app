from datetime import datetime
from app import db, bcrypt


class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, unique=True)
    username = db.Column("username", db.String(100), unique=True)
    email = db.Column('email', db.String(100), unique=True)
    email_not = db.Column("email_notifications", db.Boolean)
    password = db.Column("password", db.String())

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)


class UserGroup(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, unique=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey('user.id'))
    group_id = db.Column("group_id", db.Integer, db.ForeignKey('group.id'))

    def __init__(self, user_id: int, group_id: int):
        self.user_id = user_id
        self.group_id = group_id


class Group(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, unique=True)
    name = db.Column("name", db.String(30), unique=True)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"{self.id, self.name}"


class Ticket(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, unique=True)
    owner = db.Column("owner", db.String, db.ForeignKey('user.username'))
    title = db.Column("title", db.String(50))
    date = db.Column("date", db.DateTime)
    group = db.Column("group", db.Integer, db.ForeignKey('group.id'))
    description = db.Column("description", db.String(1000))
    priority = db.Column('priority', db.Integer)
    is_open = db.Column('is_open', db.Boolean)

    def __init__(self, owner: int, title: str, date: datetime, group: int, description: str, priority: int,
                 is_open: bool = True) -> None:
        self.owner = owner
        self.title = title
        self.date = date
        self.group = group
        self.description = description
        self.priority = priority
        self.is_open = is_open

    def __repr__(self):
        return f"Ticket no. {self.id}, created by {self.owner}, created on {self.date}, priority: {self.priority}"


#
class Note(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, unique=True)
    ticket_id = db.Column("ticket_id", db.Integer, db.ForeignKey('ticket.id'))
    owner = db.Column("owner", db.String, db.ForeignKey('user.username'))
    date = db.Column("date", db.DateTime)
    content = db.Column('content', db.String(500))
    closing = db.Column('closed', db.Boolean)

    def __init__(self, ticket_id: int, date: datetime, content: str, owner: int, closing: bool) -> None:
        self.ticket_id = ticket_id
        self.owner = owner
        self.date = date
        self.content = content
        self.closing = closing

    def __repr__(self):
        return f"Note no.{self.id} designated to tickets no. {self.ticket_id}"
