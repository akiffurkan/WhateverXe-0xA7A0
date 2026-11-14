#!/usr/bin/env python3
"""Print a version's CHANGELOG section for its GitHub Release body."""
import argparse
import re
from pathlib import Path


def release_notes(changelog, version):
    version_clean = version.removeprefix('v').split('-')[0]
    sections = re.split(r'^## (.+)\n', changelog, flags=re.MULTILINE)
    matches = [body.strip() for heading, body in zip(sections[1::2], sections[2::2])
               if heading == version_clean]
    if matches and matches[0]:
        return matches[0] + '\n'
    return f"WhateverXe release {version}\n\nAutomated release build for Raptor Lake-P A7A0."


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('version', help='release tag, with or without a v prefix')
    args = parser.parse_args()
    changelog = Path(__file__).resolve().parents[1] / 'CHANGELOG.md'
    try:
        print(release_notes(changelog.read_text(), args.version), end='')
    except ValueError as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
