class Acquisitions:
    Acquisitions = []

    def __init__(self, id, when, acquired, acquiring, amount, source, created_at, updated_at, user_id):
        self.id = id
        self.when = when
        self.acquired = acquired
        self.acquiring = acquiring
        self.amount = amount
        self.source = source
        self.created_at = created_at
        self.updated_at = updated_at
        self.user_id = user_id

    def to_dict(self):
        """A method to Convert the acquisitions instance to a dictionary"""
        acquisition = {
            'id': self.id,
            'when': self.when,
            'acquired': self.acquired,
            'acquiring': self.acquiring,
            'amount': self.amount,
            'source': self.source,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'user_id': self.user_id
        }
        return acquisition