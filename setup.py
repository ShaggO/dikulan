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

c.execute("drop table if exists `outgoing_mail`")
c.execute("drop table if exists `ticket`")
c.execute("drop table if exists `session`")
c.execute("drop table if exists `user_has_privilege`")
c.execute("drop table if exists `user`")
c.execute("""
create table `session` (
  `uuid` char(36) not null,
  `data` blob not null,
  primary key (`uuid`)
)
engine=InnoDB
default charset=utf8
collate=utf8_danish_ci
pack_keys=1
""")
c.execute("""
create table `user` (
  `id` int unsigned not null auto_increment,
  `email` varchar(255) not null,
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
pack_keys=1
""")
c.execute("""
create table `user_has_privilege` (
  `user_id` int unsigned not null,
  `privilege_id` int unsigned not null,
  primary key (`user_id`,`privilege_id`),
  constraint `user_has_privilege` foreign key (`user_id`) references `user` (`id`)
    on delete cascade
    on update cascade
)
engine=InnoDB
default charset=utf8
collate=utf8_danish_ci
pack_keys=1
""")
c.execute("""
create table `ticket` (
  `id` char(40) not null,
  `user` int unsigned default null,
  primary key (`id`),
  key `user`(`user`),
  constraint `ticket_user` foreign key (`user`) references `user` (`id`)
    on delete set null
    on update cascade
)
engine=InnoDB
default charset=utf8
collate=utf8_danish_ci
pack_keys=1
""")

c.execute("""
create table `outgoing_mail` (
  `id` int unsigned not null auto_increment,    
  `sent_time` datetime default null,
  `sender` varchar(255) not null,
  `recipient` varchar(255) not null,
  `content` blob not null,
  `error_message` text default null,
  primary key (`id`),
  key `sent_time`(`sent_time`)
)
engine=InnoDB
default charset=utf8
collate=utf8_danish_ci
pack_keys=1
""")
