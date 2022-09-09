from flask import session
from app import UserGroup, Group, Ticket, User
from app.utils.queries import Query


def session_active() -> bool:
    return True if session.get('user_id') else False


def get_session_user() -> str:
    return session.get('user')


def get_user_group(user_id: int) -> list['Group']:
    groups = Query.find_all(UserGroup, {"user_id": user_id})
    groups = [group.group_id for group in groups]
    user_groups = []
    for group in groups:
        user_groups += Query.find_all(Group, {"id": group})
    return user_groups

def get_group_name(group_id: int) -> list['Group']:
    group = Query.find_first(Group, {'id': group_id})
    return group.name

def get_user_tickets_with_condition(user_id: int, is_open: bool) -> list['Ticket']:
    groups = Query.find_all(UserGroup, {"user_id": user_id})
    groups_ids = [group.group_id for group in groups]
    tickets = []
    for group_id in groups_ids:
        tickets += Query.find_all(Ticket, {"group": group_id, "is_open": is_open})
    return tickets


def get_user_by_group(group_id: int):
    groups = Query.find_all(UserGroup, {"group_id": group_id})
    users = [group.user_id for group in groups]
    return users



def get_email_by_user_id(user_id: int):
    user = Query.find_first(User, {'id': user_id})
    return user.email


def get_ticket_by_id(ticket_id: int) -> 'Ticket':
    return Query.find_first(Ticket, {"id": ticket_id})

def get_user_details(user_id: int) -> 'User':
    user = Query.find_first(User, {'id': user_id})
    return user


def get_ticket_by_title(ticket_title: str) -> 'Ticket':
    return Query.find_first(Ticket, {'title': ticket_title})


def get_user_name(user_id: int):
    user = Query.find_first(User, {'id': user_id})
    return user.username
