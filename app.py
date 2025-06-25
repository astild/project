import argparse
import sys
from tinydb import TinyDB, Query
import re

DB_PATH = 'forms_db.json'

def detect_type(value):
    t = None
    # Проверка телефона (гибко: пробелы, дефисы, скобки)
    if re.match(r'^\+7[\s\-\(\)]*\d{3}[\s\-\(\)]*\d{3}[\s\-\(\)]*\d{2}[\s\-\(\)]*\d{2}$', value):
        t = 'phone'
    elif re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
        t = 'email'
    elif re.match(r'^(\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})$', value):
        t = 'date'
    else:
        t = 'text'
    return t

def load_db():
    return TinyDB(DB_PATH)

def get_tpl(args):
    db = load_db()
    templates = db.all()
    input_fields = {k: detect_type(v) for k, v in args.items() if k != 'command'}
    for tpl in templates:
        tpl_fields = {k: v for k, v in tpl.items() if k != 'name'}
        if all(f in input_fields and input_fields[f] == tpl_fields[f] for f in tpl_fields):
            return tpl['name']
    return '{"result": "not found"}'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['get_tpl'])
    # Парсим все параметры вида --key=value
    known, unknown = parser.parse_known_args()
    args = {'command': known.command}
    for arg in unknown:
        if arg.startswith('--') and '=' in arg:
            k, v = arg[2:].split('=', 1)
            args[k] = v
    if known.command == 'get_tpl':
        print(get_tpl(args))

if __name__ == '__main__':
    main() 