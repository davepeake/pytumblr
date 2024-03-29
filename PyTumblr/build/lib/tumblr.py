import urllib

writeurl = "http://www.tumblr.com/api/write"

class CTumblr:
    """
    A class to allow Tumblr post submission from python programs
    """
    init = 0
    verbose = 0

    def __init__(self, setemail, setpassword,verbose=0):
        self.email = setemail
        self.password = setpassword        
        self.init = 1
        self.verbose = verbose

    def msg(self,message):
        if self.verbose == 1:
            print "MSG: ", message
    

    def send(self,datadict):
        if self.init != 1:
            print "Email and Password not set, send canceled."
            return 1

        datadict["email"] = self.email
        datadict["password"] = self.password
        datadict["generator"] = "pyTumblr"

        # Fix: Add date function here

        # Debug, print the data sent.
        self.msg(" ".join(datadict.keys()))
        self.msg(" ".join(datadict.values()))

        data = urllib.urlencode(datadict)
    
        try:
            a = urllib.urlopen(writeurl, data)
        except:
            print "ERR: Unable to send data"

        try:
            self.msg("Return from tumblr" + a.readlines())
        except:
            print "ERR: Unable to readback. Data may still be sent."

        return 0

    def quote(self,quote,source='',private=False,tags=''):
        '''
        Create a Tumblr quote post, where the quote posted is provided through the quote variable.

        photourl(url,[clicktrue='', private=False, tags=''])

        The only required field is quote, which contains the quote for the post.

        Optional Fields:
            source: The attributed source of the quote (HTML Allowed). This appears with the quote in the post.
                    DEFAULT: Empty field (no source)
            private: If the post is designated as private then the post doesn't appear on the tumblog main page
                     only on the dashboard and authorised links
                     DEFAULT: False (post appears on main page)
            tags: A comma seperated list of post tags
                  DEFAULT: Empty string (no tags)
        '''
        data = {"type":"quote","quote":quote}

        if len(source) != 0:
            data["source"] = source

        if len(tags) != 0:
            data["tags"] = tags

        self.send(data)
        return 0

    def photourl(self, url, clickthru='',private=False, tags=''):
        '''
        Create a Tumblr photo post, where the photo is provided through a URL.
        For photos located on the local machine, use the photodata function

        photourl(url,[clicktrue='', private=False, tags=''])

        The only required field is url, which is a web accessible url.

        Optional Fields:
            clickthru: An url that, when the picture is clicked, the visitor is directed to.
                        DEFAULT: Empty string (no link)
            private: If the post is designated as private then the post doesn't appear on the tumblog main page
                     only on the dashboard and authorised links
                     DEFAULT: False (post appears on main page)
            tags: A comma seperated list of post tags
                  DEFAULT: Empty string (no tags)
        '''
        
        data = {"type":"photo","source":url}

        if len(clicktrue) != 0:
            data["click-thru-url"] = clickthru

        if len(tags) != 0:
            data["tags"] = tags

        if private:
            data["private"] = 1

        self.send(data)
        return 0
    
    def photodata(self, filename, clickthru='',private=False, tags=''):
        '''
        Create a Tumblr photo post, where the photo is provided from a filename.
        For photos located on the local machine, use the photodata function

        photourl(url,[clicktrue='', private=False, tags=''])

        The only required field is url, which is a web accessible url.

        Optional Fields:
            clickthru: An url that, when the picture is clicked, the visitor is directed to.
                        DEFAULT: Empty string (no link)
            private: If the post is designated as private then the post doesn't appear on the tumblog main page
                     only on the dashboard and authorised links
                     DEFAULT: False (post appears on main page)
            tags: A comma seperated list of post tags
                  DEFAULT: Empty string (no tags)
        '''

        # test post method (5M limit)
        fin = open(filename)

        # FIX: test to see if file is good
        
        filedata = "".join(fin.readlines())

        data = {"type":"photo","data":filedata}

        self.send(data)

    def videourl(self, url, caption='', private=False, tags=''):
        '''
        Create a Tumblr video post, where the video is provided through a URL.
        For videos located on the local machine, use the videodata function

        videourl(url,[caption='', private=False, tags=''])

        The only required field is url, which is a youtube url or the embed code from a video.

        Optional Fields:
            caption: A caption associated with the video (HTML allowed)
                     DEFAULT: Empty string (no caption)
            private: If the post is designated as private then the post doesn't appear on the tumblog main page
                     only on the dashboard and authorised links
                     DEFAULT: False (post appears on main page)
            tags: A comma seperated list of post tags
                  DEFAULT: Empty string (no tags)
        '''

        data = {'type' : 'video', 'embed' : url }

        if len(caption) != 0:
            data["caption"] = caption

        if len(tags) != 0:
            data["tags"] = tags

        if private:
            data["private"] = 1
            
        self.send(data)
        return 0

    def text(self, body, title, caption='', private=False, tags=''):
        '''
        Create a regular Tumblr text post. The main text is provided by the body or the title or both.

        text(body='',title='',[caption='', private=False, tags=''])

        The required fields are either body or title.

        Optional Fields:
            private: If the post is designated as private then the post doesn't appear on the tumblog main page
                     only on the dashboard and authorised links
                     DEFAULT: False (post appears on main page)
            tags: A comma seperated list of post tags
                  DEFAULT: Empty string (no tags)
        '''
        if (len(body) + len(title)) == 0:
            print "Text posts require either a body field or title field"
            return 1

        data = { "type" : "regular" }

        if len(body) != 0:
            data["body"] = body

        if len(title) != 0:
            data["title"] = title

        if len(tags) != 0:
            data["tags"] = tags

        if private:
            data["private"] = 1
        
        self.send(data)
        return 0
