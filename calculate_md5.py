#!/usr/bin/env python

# # licensed under: CreativeCommons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)
# # license details:  http://creativecommons.org/licenses/by-sa/3.0/
#
# # credits:: initially forked from:  http://stackoverflow.com/a/4213255/617185,
# # licensed under:  CC-SA-3.0    http://creativecommons.org/licenses/by-sa/3.0/

"""
Calculate md5 checksum value of any file of any size

usage:
    :param  get_hash(filename)
    :returns md5 checksum value of the file
"""
import hashlib


def checksum_md5(filename):
    _chunk_size = 1024 * 8

    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(_chunk_size), b''):
            md5.update(chunk)
    return md5.digest()
