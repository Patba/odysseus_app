from datetime import datetime

from app import db as db
from app import bcrypt
from app.utils.validators import UserValidator
from app.models.models import User, Ticket, Group


class Query:

    @staticmethod
    def find_first(table: 'db.Model', names_and_values: dict) -> 'db.Model':
        return table.query.filter_by(**names_and_values).first()

    @staticmethod
    def find_all(table: 'db.Model', names_and_values: dict) -> list['db.Model']:
        return table.query.filter_by(**names_and_values).all()

    @staticmethod
    def find_all_without_condition(table: 'db.Model'):
        return table.query.all()






