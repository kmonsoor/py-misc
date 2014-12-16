#!/usr/bin/env python

# # licensed under: CreativeCommons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)
# # license details:  http://creativecommons.org/licenses/by-sa/3.0/
#
# # credits::   initial source:  http://stackoverflow.com/a/2257449/617185
# # licensed under:  CC-SA-3.0   http://creativecommons.org/licenses/by-sa/3.0/

"""
    Generate a random string consisting only uppercase(A-Z) and numbers(0-9).

    String length will be <length>
"""
from random import choice
from string import ascii_uppercase, digits


def generate_random_alphanum(length=None):
    """
    :param  length   length of the target random string
    :returns Returns a random string consisting only uppercase(A-Z) and numbers(0-9)
    """
    return '' if (not length) else ''.join(choice(ascii_uppercase + digits) for _ in range(length))

