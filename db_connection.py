from sqlalchemy import create_engine, Integer, JSON, Column, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

EntityBase = declarative_base()


class Item(EntityBase):
    __tablename__ = "items"
    id = Column(Integer, Sequence("item_id_seq"), primary_key=True, nullable=False)
    information = Column(JSON, nullable=True)


# Setup a database connection. Using in-memory database here.
engine = create_engine("sqlite://", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# Create all tables derived from the EntityBase object
EntityBase.metadata.create_all(engine)

# Declare a new row
first_item = Item()
first_item.information = dict(a=1, b="foo", c=[1, 1, 2, 3, 5, 8, 13])

# Insert it into the database
session.add(first_item)
session.commit()

# Get all saved items from the database
for item in session.query(Item).all():
    print(type(item.information))
    # <class 'dict'>
    print(item.id, item.information)
    # 1 {'a': 1, 'b': 'foo', 'c': [1, 1, 2, 3, 5, 8, 13]}