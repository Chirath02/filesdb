# coding=utf-8

from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_file = 'db.sqlite3'

engine = create_engine('sqlite:///' + db_file, echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)
    size = Column(Float)
    file_name = Column(String)
    dir_name = Column(String)

    owner = Column(String)
    group = Column(String)
    access_date = Column(Date)
    modified_date = Column(Date)
    changes_date = Column(Date)

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def base_name(self):
        name_parts = self.file_name.split('.')
        return "".join(name_parts[:-1])

    def extension(self):
        return self.file_name.split('.')

