#!/usr/bin/env python


# The MIT License (MIT)
#
# Copyright (c) 2014 Khaled Monsoor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# # credits:: initially forked from:  https://github.com/bkkcoins/misc/


"""
Calculate distance and compass bearing between 2 GPS co-ordinates.

usage:
    gps_distance((lat1, long1), (lat2, long2))

    returns: tuple as (distance_in_kilometers, compass_heading_in_degree)
"""

from math import pi, sin, atan2, sqrt, cos
from sys import argv


def gps_distance(point_1, point_2):
    """
    Calculate distance and compass bearing between 2 GPS co-ordinates.

    usage:
        :param  gps_distance((lat1, long1), (lat2, long2))
        :returns tuple as (distance_in_kilometers, compass_heading_in_degree)
    """
    lat1, long1 = point_1
    lat2, long2 = point_2

    degree_to_rad = float(pi / 180.0)

    d_lat = (float(lat2) - float(lat1)) * degree_to_rad
    d_long = (float(long2) - float(long1)) * degree_to_rad

    # distance
    a = pow(sin(d_lat / 2), 2) + \
        cos(float(lat1) * degree_to_rad) * cos(float(lat2) * degree_to_rad) * pow(sin(d_long / 2), 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # bearing
    y = sin(d_long) * cos(float(lat2) * degree_to_rad)
    x = cos(float(lat1) * degree_to_rad) * sin(float(lat2) * degree_to_rad) - \
        sin(float(lat1) * degree_to_rad) * cos(float(lat2) * degree_to_rad) * cos(d_long)
    b = atan2(y, x) / degree_to_rad

    return 6371 * c, b if b >= 0 else b + 360


if __name__ == '__main__':
    if len(argv) < 5:
        print u"Usage: {0} <lat1> <long1> <lat2> <long2>\nValues in degree only or <deg min sec> triplets, \
                with S,W negative. Result in Kilometer(km) .\n".format(argv[0])
        exit()
    if len(argv) > 5:
        for n in xrange(4):
            argv[n + 1] = float(argv[n * 3 + 1]) + float(argv[n * 3 + 2]) / 60 + float(argv[n * 3 + 3]) / 3600

    print "Distance %3.2f km, Heading %3.1f" % gps_distance((argv[1], argv[2]), (argv[3], argv[4]))
