#!/usr/bin/env python
# -*- coding:utf8 -*-

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello ithomer")

class StoryHandler(tornado.web.RequestHandler):
    def get(self,story_id):
        self.write("You requested the story " + story_id)

applicaction = tornado.web.Application([
    (r"/",MainHandler),
    (r"/story/([0-9]+)",StoryHandler),
])

if __name__ =="__main__":
    print("look at: http://localhost:8888")
    applicaction.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
