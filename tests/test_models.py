import sqlite3
import unittest
import os

from sqlalchemy import create_engine

from filesdb.models import File, database_config


class FileTest(unittest.TestCase):

    def setUp(self):
        """
        Create the test database
        """
        self.db_file = 'test-db.sqlite3'
        self.engine, self.Session, self.Base = database_config(
            db_file=self.db_file)
        self.Base.metadata.create_all(self.engine)

    def tearDown(self):
        """
        Remove the test database
        """
        os.remove(self.db_file)

    def test_database_config_return_default(self):
        """
        Tests if the database_config() function returns a default sqlite file
        """
        output = database_config()
        self.assertEqual(len(output), 3)
        self.assertEqual(str(output[0].url), 'sqlite:///db.sqlite3')

    def test_database_config(self):
        """
        Tests if the database_config() function sets the correct db name
        """
        engine = create_engine('sqlite:///' + self.db_file)
        self.assertEqual(engine.url, self.engine.url)

    def test_file_save_to_databas(self):
        """
        Tests saving a file to the database.
        """
        session = self.Session()

        file = File(name='test.txt', path='./test', size=100)
        session.add(file)

        self.Base.metadata.create_all(self.engine)

        conn = sqlite3.connect(self.db_file)
        cur = conn.cursor()
        cur.execute('select * from files;')
        rows = cur.fetchall()

        self.assertEqual(len(rows), 0)

        session.commit()
        session.close()

        cur.execute('select * from files;')
        rows = cur.fetchall()

        self.assertEqual(len(rows), 1)


if __name__ == '__main__':
    unittest.main()
