
## Running the tests

* First attempt as list, runs all tests in 5.4 s
* second attempt implementing my own linked list, using class/objects, all tests in 27.8 s
* third using collection.deque, but doing inserts and removes rather than rotating. All tests in 6 s
* removing all logging my object-base solution runs in 0.63 s

## Running part 2

464 players, 7173000 marbles

For reference, [/r/marcusandrews](https://old.reddit.com/r/adventofcode/comments/a4i97s/2018_day_9_solutions/ebepyc7/)' solution runs in 2.82 s

* Testing log level in my object-based solution to avoid args evaluation got it down to 40 s
* Completely remoivng logging, runs in 36 s
* Removing class counter (no longer needed) gets it further down to 30 s

I don't think this can be optimized much further while still using Python objects.

Apparently [Python classes are expensive because based on dictionary](https://stackoverflow.com/questions/41781048/overhead-of-creating-classes-in-python-exact-same-code-using-class-twice-as-slo), so the best perfomance characteristics a Python class can have are the characteristics of a dictionary.

