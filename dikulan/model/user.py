# -*- coding: utf-8 -*-
from dikulan.utils import pool
from dikulan.lib.string import validEmail
from MySQLdb import IntegrityError
import random

__all__ = [
    "EmailExists",
    "InvalidEmail",
    "add_user",
    "get_email",
    "user_id_by_auth"
]

class EmailExists(Exception):
    pass
class InvalidEmail(Exception):
    pass
class AuthFailureException(Exception):
    pass

characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def _generate_password():
    password = "".join(random.sample(characters,10))
    return password

def add_user(name, email):
    if not validEmail(email):
        raise InvalidEmail()
    
    password = _generate_password()
    
    conn = pool.take()
    cursor = conn.cursor()
    try:
        cursor.execute(u"insert into user (name, email, password) values(%s,%s,%s)",
            (name, email,password)
        )
    except IntegrityError:
        raise EmailExists()
    finally:
        cursor.close()
        conn.commit()
        pool.give(conn)


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
