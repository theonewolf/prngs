#!/usr/bin/env python
#
# Description: This is my attempt at making a PRNG.  It is my first attempt
# ever.  It is inspired from other PRNG's I have seen, but was done off the
# top of my head while very tired---so I don't expect it to be good at all.
#
# In fact, I bet it's horrible.  But this was just for fun.
#
# Author: Wolfgang Richter <wolf@cs.cmu.edu>
# Site: github.com/theonewolf/prng
# 
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import sys
import time

USAGE = '''%s - <number of random numbers to generate> [d6]'''


# seed = 169743212279 --> developed with this seed
# period experimentally determined with this seed
# period = 76860; appears to vary with seed
# distribution of d6 random numbers:
#  12752 0
#  12851 1
#  12797 2
#  12748 3
#  12859 4
#  12853 5
def wolf_random1(seed):
    static_ret = seed
    while True:
        ret = 37 ^ static_ret
        ret = ret >> 4
        ret = ret << 5
        ret *= 17
        static_ret = ret % seed
        if ret & 0x00008000: ret += 1
        yield ret


# provide values from 0-5; hopefully uniformly distributed
def d6(gen):
    while True:
        yield gen.next() % 6


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print USAGE % sys.argv[0]

    seed = int(time.time())
    generator = wolf_random1(seed)
    
    if len(sys.argv) > 2 and sys.argv[2].lower() == 'd6':
        generator = d6(generator)

    for x in xrange(int(sys.argv[1])):
        print generator.next()
