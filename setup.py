#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
from dikulan.config import config
import MySQLdb

conn = MySQLdb.connect(
        host=config["mysql_address"],
        user=config["mysql_username"],
        passwd=config["mysql_password"],
        db=config["mysql_database"]
)

c = conn.cursor()

c.execute("""
create table if not exists `session` (
  `uuid` char(36) not null,
  `data` blob not null,
  primary key (`uuid`)
)
engine=InnoDB
default charset=utf8
collate=utf8_danish_ci
pack_keys=1;
""")
c.execute("""
create table if not exists `user` (
  `id` int unsigned not null auto_increment,
  `email` varchar(255) default null,
  `password` varchar(255) not null,
  `name` varchar(255) default null,
  primary key (`id`),
  unique `email` (`email`(10)),
  index `auth` (`email`(10),`password`(10)),
  index `name` (`name`(10))
)
engine=InnoDB
default charset=utf8
collate=utf8_danish_ci
pack_keys=1;
""")
