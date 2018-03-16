import argparse

import os

parser = argparse.ArgumentParser(description='Files db')

parser.add_argument('scan', nargs='?',
                    help='root dir to start processing files(default is .)')

parser.add_argument('root',
                    help='root dir to start processing files(default is .)',
                    default='.', nargs='?')

parser.add_argument(
    '-d', '--database', nargs='?', const='db.sqlite3', default='db.sqlite3',
    dest='database', help='a database name, default is db.sqlite3')

args = parser.parse_args()

# get the root_dir
root_dir = args.root

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        print(os.path.join(subdir, file))



