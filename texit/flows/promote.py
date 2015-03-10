#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import fileinput
import json
import sys


replacements = {
    'test': [
        ('sitterfied.ngrok.com', 'test.sitterfied.com'),
    ],
    'prod': [
        ('test.sitterfied.com', 'www.sitterfied.com'),
    ],
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Promote a flow to another environment')
    parser.add_argument('flow', action='store', help='The source flow json file.')
    parser.add_argument('env', action='store', help='The target environment.')

    args = parser.parse_args()
    if args.env not in ['test', 'prod']:
        raise ValueError('env argument must be [test, prod]')

    # Open the source file and convert it to json
    with open(args.flow) as f:
        source = json.load(f)

    # We only need to work with the version and flows sections of the
    # json flow
    version = source.get('version')
    flows = source.get('flows')

    # Grab the destination file (based on env) and load it as json
    dest = '{}-find-a-sitter.json'.format(args.env)
    with open(dest) as f:
        target = json.load(f)

    # Update the source the json with the correct id and name values
    flows[0]['id'] = target.get('flows')[0].get('id')
    flows[0]['name'] = target.get('flows')[0].get('name')

    # Reset the version and flows sections to the source versions
    target['version'] = version
    target['flows'] = flows

    # Write the file out via a json dump
    with open(dest, 'w') as f:
        json.dump(target, f, indent=2)

    # Now read the file back and alter any lines that match our
    # replacements list.
    items = replacements.get(args.env)
    for line in fileinput.input(files=[dest], inplace=True):
        for src, repl in items:
            if line.find(src) > -1:
                sys.stdout.write(line.replace(src, repl))
            else:
                sys.stdout.write(line)
