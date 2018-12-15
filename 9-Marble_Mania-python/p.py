#!/usr/bin/env python3

import sys
import cProfile
from mania_object_linked_list import high_score

num = 5000
if len(sys.argv) >= 2:
    num = int(sys.argv[1])


cProfile.run('high_score(13, num)')

