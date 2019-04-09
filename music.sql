#!/usr/bin/python
# -*- coding: utf-8 -*-
"""SQL file"""

CREATE TABLE artist (
    id int PRIMARY KEY,
    artist varchar(50) NOt NULL
);

CREATE TABLE album (
    id int PRIMARY KEY,
    album varchar(50) NOt NULL,
    artist_id int
 );

CREATE TABLE song (
    id int PRIMARY KEY,
    song varchar(50) NOt NULL, 
    album_id int, 
    artist_id int,
    track_num int,
    track_sec int
);
