# fileDB

The command line utility collects metadata about every file in the given 
directory.

```bash
$ python -m filesdb.core [-h] [-d [DATABASE]] {scan,version,quickscan} [root_dir]
```

## Scan command

The scan command is used to store meta data about each and every file in the 
given directory, archive or git repository.

```bash
$ python -m filesdb.core scan
```

By default the scan command looks in the current directory and creates a db file
 named db.sqlite3.
 
#### Optional parameters

```bash
$ python -m filesdb.core scan [dir] [--d/--database] db_filename
```

## Quick scan command

Quick scan command is similar to scan command. It does store the hashes.

```bash
$ python -m filesdb.core quickscan [dir] [--d/--database] db_filename
```

## Development

### Install dependencies

Create a virtual env using virtualenvwarpper
```bash
$ mkvirtualenv --python=/usr/bin/python3 filesdb
$ workon filesdb
$ pip install -r requirements.txt 
```

### Tests

The current tests checks the db scheme and checks the core functionality

```bash
$ python -m tests.test_models
$ python -m tests.test_core
```
