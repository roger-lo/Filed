#!/usr/bin/env python
import re

from os import walk, path, listdir


def main():
    # TODO: Reads the config file
    # Format: src:dest:regex
    sources = []
    sources.append("~/Workspace/filed/test/")
    patterns = [".*\.pdf"]

    # Monitor folder for changes
    matches = matcher(sources, patterns)
    print(matches)

    # TODO: Move the file if changes


# Returns the file path that match any of the rules
def matcher(sources, rules):
    f = []
    for s in sources:
        for filename in listdir(path.expanduser(s)):
            if multimatch(filename, rules):
                f.append(path.join(s, filename))
        # TODO: Future subtrees - for (dirpath, dirnames, filenames) in walk(path.expanduser(s)):
    return f


# Inefficient way to attempt to match against multiple patterns
def multimatch(word, patterns):
    for pattern in patterns:
        if re.search(pattern, word):
            return True

if __name__ == "__main__":
    main()
