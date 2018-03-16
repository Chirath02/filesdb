import unittest

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from filesdb.models import File, database_config


class FileTest(unittest.TestCase):

    def setUp(self):
        self.db_file = 'db.sqlite3'
        self.engine = create_engine('sqlite:///' + self.db_file)
        self.Session = sessionmaker(bind=self.engine)
        self.Base = declarative_base()

    def test_database_config_return_default(self):
        output = database_config()
        self.assertEqual(len(output), 3)
        self.assertEqual(str(output[0].url), 'sqlite:///db.sqlite3')

    def test_database_config(self):
        output = database_config(db_file=self.db_file)
        self.assertEqual(len(output), 3)
        self.assertEqual(output[0].url, self.engine.url)


if __name__ == '__main__':
    unittest.main()
