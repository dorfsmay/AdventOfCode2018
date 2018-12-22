#!/bin/bash
here=$(dirname $0)
curl -b ${here}/cookie.jar -svoinput.txt https://adventofcode.com/2018/day/${1}/input
