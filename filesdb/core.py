import argparse

import os

from filesdb.models import database_config, File

parser = argparse.ArgumentParser(description='Files db')

commands = ['scan', 'version', 'quickscan']

parser.add_argument('scan', default=False, choices=commands,
                    help='root dir to start processing files(default is .)')

parser.add_argument('root',
                    help='root dir to start processing files(default is .)',
                    default='.', nargs='?')

parser.add_argument(
    '-d', '--database', nargs='?', const='db.sqlite3', default='db.sqlite3',
    dest='database', help='a database name, default is db.sqlite3')

# get the arguments
args = parser.parse_args()
command = args.scan
database_path = args.database

print(args)

# set up the database
engine, Session, Base = database_config(database_path)

if not os.path.exists(database_path):
    # 2 - generate database schema
    Base.metadata.create_all(engine)

session = Session()

if command == 'quickscan':
    # get the root_dir
    root_dir = args.root

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            try:
                print(file)
                details = os.stat(os.path.join(subdir, file))
                new_file = File(name=file.split('/')[-1],
                                path=os.path.join(subdir, file),
                                size=details.st_size)
                session.add(new_file)
            except FileNotFoundError:
                print('error')
        session.commit()
    session.close()
