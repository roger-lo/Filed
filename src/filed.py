#!/usr/bin/env python
import logging
import re

from os import walk, path, listdir


class Rule(object):
    src = None
    dst = None
    reg = None


def parse_config_file(fd):
    """Parses the file descriptor line by line. Skips comments. This also
    validates all the configurations, therefore the return value should be safe
    and usable.
    """

    rules = []

    for num, line in enumerate(fd):

        line = line.strip()

        # Skip comments
        if line.startswith('#'):
            continue

        # Format of the line is src:dst:regexpression
        parts = line.split(':')
        if len(parts) != 3:
            logging.warning("{}:{}: Error reading line".format(filename, num))
            continue

        # Validate the parts of the config
        r = Rule()
        r.src = path.expanduser(parts[0])
        r.dst = path.expanduser(parts[1])
        r.reg = parts[2]

        if not path.isdir(r.src):
            logging.warning(
                "{}:{}: {} is not a directory"
                .format(filename, num, r.src))


        if not path.isdir(r.dst):
            logging.warning(
                "{}:{}: {} is not a directory"
                .format(filename, num, r.dst))

        try:
            re.compile(r.reg)
        except Exception as e:
            logging.warning(
                "{}:{}: error parsing regex: {}"
                .format(filename, num, str(e)))

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
        '~/.filedrc'
    ]

    rules = {}
    for filename in config_files:
        rules[filename] = load_config_file(filename)

    # Monitor folder for changes
    for filename, rules in rules.items():
        for rule in rules:
            matches = matcher(rule.src, rule.reg)
            print(matches)

    # TODO: Move the file if changes


# Returns the file path that match any of the rules
def matcher(source, rule):
    f = []
    for filename in listdir(path.expanduser(source)):
        if re.match(rule, filename):
            f.append(path.join(source, filename))
    # TODO: Future subtrees - for (dirpath, dirnames, filenames) in walk(path.expanduser(s)):
    return f

if __name__ == "__main__":
    main()
