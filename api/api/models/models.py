from api.models.database import DatabaseConnection
# from flask import jsonify


cursor = DatabaseConnection().cursor

acquisitions = []

class Acquisitions:

    def __init__(self, id=None, when=None, acquired=None, acquiring=None, amount=None, source=None, created_at=None, updated_at=None, user_id=None):
        self.id = id
        self.when = when
        self.acquired = acquired
        self.acquiring = acquiring
        self.amount = amount
        self.source = source
        self.created_at = created_at
        self.updated_at = updated_at
        self.user_id = user_id

    def get_all_acquisitions(self):
        get_all_acquisitions = "SELECT * FROM Acquisitions"
        self.cursor.execute(get_all_acquisitions)
        results = self.cursor.fetchall()
        return results

#     def to_dict(self):
#         """A method to Convert the acquisitions instance to a dictionary"""
#         acquisition = {
#             'id': self.id,
#             'when': self.when,
#             'acquired': self.acquired,
#             'acquiring': self.acquiring,
#             'amount': self.amount,
#             'source': self.source,
#             'created_at': self.created_at,
#             'updated_at': self.updated_at,
#             'user_id': self.user_id
#         }
#         return acquisition