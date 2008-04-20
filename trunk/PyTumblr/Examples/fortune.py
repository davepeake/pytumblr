#!/usr/bin/python

import tumblr
import os

email = "testing@test.com"
password = "password"
debug = 1

cTumblr = tumblr.CTumblr(email,password,debug)

fortpipe = os.popen('fortune -l')

fortune = "".join(fortpipe.readlines())

# Set up a translation map to remove \t and \n characters
transmap = [chr(i) for i in range(256)]
transmap[ord('\t')] = ' '
transmap[ord('\n')] = ' '

transmap = "".join(transmap)

fortune = fortune.translate(transmap)

cTumblr.quote(fortune,"Fortune")

