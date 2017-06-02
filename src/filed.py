#!/usr/bin/env python
import logging
import re

from os import walk, path, listdir

from predicates.predicate import *
from actions.action import *


class Rule(object):
    src = None
    predicates = None
    actions = None


def parse_config_file(fd):
    """Parses the file descriptor line by line. Skips comments. This also
    validates all the configurations, therefore the return value should be safe
    and usable.
    """
    rules = []

    for num, line in enumerate(fd):
        line = line.strip()

        # Skip comments
        if line.startswith('#') or not len(line) > 1:
            continue

        # See resource/filedrc for example format
        parts = line.split(':')
        if len(parts) != 3:
            logging.warning("{}:{}: Error reading line".format(line, num))
            continue

        # Validate the parts of the config
        r = Rule()
        r.src = path.expanduser(parts[0])

        try:
            # TODO: Bad things will happen if pipe symbol inside the function
            # TODO: Avoid using eval()
            r.predicates = list(map(eval, parts[1].split('|')))
            r.actions = list(map(eval, parts[2].split('|')))
        except RuntimeError:
            # TODO: Doing proper exceptions.
            logging.warning("Something went wrong")
            continue

        if not path.isdir(r.src):
            logging.warning(
                "{}:{}: {} is not a directory"
                .format(line, num, r.src))

        rules.append(r)

    return rules


def load_config_file(filename):
    """Loads a configuration file, and logs any troubles. Returns None if there
    were any errors with reading or accessing the file. Returns [] if there are
    no rules, and returns [Rules(), ...] on success.
    """
    filename = path.expanduser(filename)

    if not path.isfile(filename):
        logging.info("{} does not exist as a file.".format(filename))
        return None

    try:
        with open(filename, 'r') as fd:
            return parse_config_file(fd)
    except IOError as e:
        logging.warning("Could not read {}: {}", filename, str(e))

    return None


def main():
    config_files = [
        path.join(path.dirname(__file__), 'resource/filedrc')
    ]

    rules = {}
    for filename in config_files:
        rules[filename] = load_config_file(filename)

    # Monitor folder for changes
    for filename, rules in rules.items():
        for rule in rules:
            files = listdir(path.expanduser(rule.src))

            for predicate in rule.predicates:
                files = filter(predicate.match, files)

            for action in rule.actions:
                files = map(action.process, files)

            # Because map and filters are lazy function. This is needed to execute map and filters
            list(files)

if __name__ == "__main__":
    main()
