# -*- coding: utf-8 -*-
from dikulan.utils import pool
from dikulan.lib.string import validEmail
from MySQLdb import IntegrityError

class EmailExists(Exception):
    pass
class InvalidEmail(Exception):
    pass

def add_user(email, password):
    if not validEmail(email):
        raise InvalidEmail()
    
    conn = pool.take()
    cursor = conn.cursor()
    try:
        cursor.execute(u"insert into user (email, password) values(%s,%s)",
            (email,password)
        )
    except IntegrityError:
        raise EmailExists()
    finally:
        cursor.close()
        conn.commit()
        pool.give(conn)
        
class AuthFailureException(Exception):
    pass

def user_id_by_auth(email, password):
    conn = pool.take()
    cursor = conn.cursor()
    cursor.execute(u"select id from user where email=%s and password=%s",
        (email,password)
    )
    try:
        id, = cursor.fetchone()
    except TypeError:
        raise AuthFailureException()
    finally:
        conn.commit()
        cursor.close()
        pool.give(conn)
    return id

def get_email(id):
    conn = pool.take()
    cursor = conn.cursor()
    cursor.execute(u"select email from user where id=%s",(id,))
    email, = cursor.fetchone()
    conn.commit()
    cursor.close()
    pool.give(conn)
    return email
