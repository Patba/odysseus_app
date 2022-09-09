import re


class UserValidator:
    def __init__(self, username: str = None, email: str = None, password: str = None, phone_number: str = None, company_name: str = None) -> None:
        self.username = username
        self.email = email
        self.password = password


    def validate_username(self) -> bool:
        return re.match(r'^[^=]+$', self.username) is not None
    def validate_email(self) -> bool:
        return re.match(r'^[^=]+@[^=]+\.[a-z]+$', self.email) is not None

    def validate_password(self) -> bool:
        return re.match(r'^[^=]+$', self.password) is not None

    def validate_all(self) -> bool:
        return self.validate_username() and self.validate_password()


class UserGroupValidator:
    def __init__(self, user_id: int = None, group_id: int = None) -> None:
        self.user_id = user_id
        self.group_id = group_id

    # def validate_group_id(self) -> bool:
    #     Query.find_all()

