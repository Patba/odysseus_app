from app import db as db
from app import bcrypt
from app.utils.queries import Query
from app.utils.validators import UserValidator
from app.models.models import User, Ticket, Group, UserGroup
import datetime


class DbManager:
    def __init__(self, database: 'db') -> None:
        self.database = database

    def commit_changes(self) -> None:
        self.database.session.commit()

    def delete_record(self, record: db.Model) -> None:
        if record and isinstance(record, db.Model):
            self.database.session.delete(record)
            self.commit_changes()

    def add_record(self, record: 'db.Model') -> None:
        if record and isinstance(record, db.Model):
            self.database.session.add(record)
            self.commit_changes()

    def revert_last_commit(self) -> None:
        self.database.session.revert()

    def create_models_tables(self) -> None:
        self.database.create_all()


class RecordManager:
    def __init__(self, record: 'db.Model') -> None:
        self.record = record

    def get_id(self) -> int:
        return self.record.id

    def exists(self) -> bool:
        return self.record is not None

    def name(self) -> str:
        return self.record.__name__

    def __repr__(self) -> str:
        return f"{self.name} Model Manager"

    def get_record(self) -> 'db.Model':
        return self.record


class UserManager(RecordManager):

    def __init__(self, record: 'db.Model') -> None:
        super().__init__(record)
        if not isinstance(self.record, User):
            raise ValueError(f"{self.record.__name__} object is not instance of a User")

    def get_username(self) -> str:
        return self.record.username

    def get_email(self) -> str:
        return self.record.email

    def get_password(self) -> str:
        return self.record.password

    def update_username(self, new_value: str) -> None:
        if UserValidator(username=new_value).validate_username():
            self.record.username = new_value
    def update_email(self, new_value: str) -> None:
        if UserValidator(email=new_value).validate_email():
            self.record.email = new_value

    def update_password(self, new_value: str) -> None:
        if UserValidator(password=new_value).validate_password():
            self.record.password = bcrypt.generate_password_hash(new_value)


class UserGroupManager(RecordManager):

    def __init__(self, record: 'db.Model') -> None:
        super().__init__(record)
        if not isinstance(self.record, UserGroup):
            raise ValueError(f"{self.record.__name__} object is not instance of a UserGroup")

    def get_user_id(self) -> str:
        return self.record.user_id

    def get_group_id(self) -> str:
        return self.record.group_id


class TicketManager(RecordManager):

    def __init__(self, record: 'db.Model') -> None:
        super().__init__(record)
        if not isinstance(self.record, Ticket):
            raise ValueError(f"{self.record.__name__} object is not instance of a Ticket")

    def get_owner(self) -> str:
        return self.record.owner

    def get_title(self) -> str:
        return self.record.title

    def get_date(self) -> 'datetime.datetime':
        return self.record.date

    def get_group_id(self) -> int:
        return self.record.group

    def get_group(self) -> str:
        return Query.find_first(Group, {"id": self.record.group}).name

    def get_description(self) -> str:
        return self.record.decription

    def get_priority(self) -> str:
        return self.record.priority

    def get_is_open_status(self) -> bool:
        return self.record.is_open

    def update_owner(self, new_value: str) -> str:
        self.record.owner = new_value

    def update_title(self, new_value: str) -> str:
        self.record.title = new_value

    def update_date(self, new_value: 'datetime.datetime') -> 'datetime.datetime':
        self.record.date = new_value

    def update_group_id(self, new_value: int) -> int:
        self.record.group = new_value

    def update_group(self, new_value: str) -> str:
        pass

    def update_description(self, new_value: str) -> str:
        self.record.description = new_value

    def update_priority(self, new_value: str) -> str:
        self.record.priority = new_value

    def update_is_open_status(self, new_value: bool) -> bool:
        self.record.is_open = new_value


class Usr:
    def __init__(self, _id):
        self.id = _id
        self.name = Query.find_first(User, {"id": _id}).username
        self.email = Query.find_first(User, {"id": _id}).email


class Dep:
    def __init__(self, _id, current_user_id: int):
        self.name = Query.find_first(Group, {"id": _id}).name
        users_id = [user_group.user_id for user_group in Query.find_all(UserGroup, {"group_id": _id}) if user_group.user_id != current_user_id]
        self.users = [Usr(user_id) for user_id in users_id]


class RequestDepartments:
    def __init__(self, _id, current_user_id: int):
        departments_id = [user_group.group_id for user_group in Query.find_all(UserGroup, {"user_id": _id}) ]
        self.departments = [Dep(_id, current_user_id) for _id in departments_id]


