import shutil
import sqlite3
import unittest

import os
import subprocess


class CoreTest(unittest.TestCase):

    def setUp(self):
        """
        Create test folders and files
        """
        self.test_dir = './test/'
        self.db_file = 'test-db.sqlite3'
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        fp = open(self.test_dir + 'test.txt', 'w')
        fp.write(self.test_dir)
        fp.close()

    def tearDown(self):
        """
        Remove temp files and folders
        """
        shutil.rmtree(self.test_dir)
        os.remove(self.db_file)

    def test_quick_scan(self):
        """
        Tests if the quick command works correctly.
        """
        command = 'python -m filesdb.core quickscan %s -d %s' % \
                  (self.test_dir, self.db_file)

        subprocess.call(command.split(' '))

        conn = sqlite3.connect(self.db_file)
        cur = conn.cursor()
        cur.execute('select * from files;')
        rows = cur.fetchall()

        self.assertEqual(len(rows), 1)


if __name__ == '__main__':
    unittest.main()
