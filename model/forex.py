from app import db


class Forex(db.Model):
    '''this class creates ta table tht stores data fro alpha vantage api'''
    id = db.Column(db.Integer(), primary_key=True)
    to=db.Column(db.String(),nullable=False)
    from_ = db.Column(db.String(),nullable=False)
    high = db.Column(db.Float(precision=4), nullable=False)
    low = db.Column(db.Float(precision=4),nullable=False)
    close=db.Column(db.Float(precision=4),nullable=False)
    datetime= db.Column(db.DateTime,nullable=False)