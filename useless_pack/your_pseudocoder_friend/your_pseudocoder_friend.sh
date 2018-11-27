#!/bin/bash
pylint $1 1>t
python3 your_pseudocoder_friend.py t
rm -f t
