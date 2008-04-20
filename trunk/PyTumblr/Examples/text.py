#!/usr/bin/python

import tumblr

email = "test@testing.com"
password = "tumblrpassword"

cTumblr = tumblr.CTumblr(email, password)

title = "Testing 1,2,3"
text = "Some awesome text."

cTumblr.text(text,title)
