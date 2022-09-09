from app import Ticket, User
from app.utils.queries import Query


class DbModelQuery:
    def __init__(self, model_id: int | str):
        self.id = model_id

    pass


#
#
class UserQuery(DbModelQuery):
    def __init__(self, model_id):
        super().__init__(model_id)
        self.result = Query.find_first(User, {"id": self.id})


#
class TicketQuery(DbModelQuery):
    def __init__(self, model_id):
        super().__init__(model_id)
        self.result = Query.find_first(Ticket, {"id": self.id})


#
#
# class NoteQuery(DbModelQuery):
#     pass
#
#
# class GroupQuery(DbModelQuery):
#     pass
#
#
# class UserGroupQuery(DbModelQuery):
#     pass

if __name__ == '__main__':
    t1 = TicketQuery(1)
    print(t1.result)
