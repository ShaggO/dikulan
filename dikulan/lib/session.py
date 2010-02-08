# -*- coding: utf-8 -*-
from pylons import g, request, response
from uuid import uuid4
from cPickle import dumps, loads

import logging

log = logging.getLogger(__name__)

class InvalidCookieException(Exception):
    pass

class Session(object):
    def __init__(self):
        uuid = request.cookies.get("session")
        if uuid != None:
            try:
                self.load_session(uuid)
            except InvalidCookieException:
                self.new_session()
        else:
            self.new_session()
        response.set_cookie("session", self.uuid, max_age=3600)
    
    def load_session(self, uuid):
        conn = g.dbpool.take()
        cursor = conn.cursor()
        cursor.execute("select data from session where uuid = %s",(uuid,))
        row = cursor.fetchone()
        if row == None:
            raise InvalidCookieException()
        self.data = loads(row[0])
        self.uuid = uuid
        cursor.close()
        g.dbpool.give(conn)
        
    def new_session(self):
        self.uuid = str(uuid4())
        self.data = list()
        conn = g.dbpool.take()
        cursor = conn.cursor()
        cursor.execute(
            "insert into session (uuid, data) VALUES(%s,%s)",
            (self.uuid,dumps(self.data,-1))
        )
        cursor.close()
        conn.commit()
        g.dbpool.give(conn)
