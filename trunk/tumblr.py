import urllib

'''data = urllib.urlencode({"email" : "dave.peake@yahoo.com.au", \
                         "password" : "tumblrpassword", \
                         "type" : "quote", \
                         "quote" : "This might be crazy enough to work!" } )
f = urllib.urlopen("http://www.tumblr.com/api/write", data)
s = f.read()'''

class CTumblr:
    init = 0
    
    def __init__(self, setemail, setpassword):
        self.email = setemail
        self.password = setpassword        
        self.init = 1

    def send(self,data):
        if self.init != 1:
            print "Send Buggered"
            return 1

        a= urllib.urlopen("http://www.tumblr.com/api/write", data)
        print a.readlines()
        return 0

    def quote(self,quote):
        if self.init != 1:
            print "Quote Buggered"
            return 1

        data = urllib.urlencode({"email" : self.email, \
                                 "password" : self.password, \
                                 "type" :  "quote", \
                                 "quote" : quote } )

        self.send(data)
        return 0

    def photourl(self, url, clickthru=''):
        if self.init != 1:
            print "Quote Buggered"
            return 1

        data = urllib.urlencode({"email" : self.email, \
                                 "password" : self.password, \
                                 "type" : "photo", \
                                 "source" : url, \
                                 "click-through-url" : clickthru } )
        self.send(data)
        return 0

    def text(self, body, title):
        if self.init != 1:
            print "Text Stuffed"
            return 1

        data = urllib.urlencode({"email" : self.email, \
                                 "password" : self.password, \
                                 "type" : "regular", \
                                 "body" : body , \
                                 "title" : title } )

        self.send(data)
        return 0
