#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module queries_pet DB ."""


import sqlite3 as lite
import sys

con = None 

try:
    con = lite.connect('pets.db') 
    con.row_factory = lite.Row 

    while True:
        choice_person = raw_input('Enter an ID number: ')

        if choice_person == '-1':
            sys.exit() 
        
        else:
            try:
                choice_person = int(choice_person)

            except:
                print "ERROR: Enter another ID number!"
                continue

        cur = con.cursor()
        cur.execute("SELECT * FROM person WHERE id =?", [(choice_person)]) 
        row = cur.fetchone() 

        if row == None:
            print 'Invalid ID number. Make another choice.'
            continue

        print row['first_name'] + ' ' + row['last_name'] + ' is ' + str(
            row['age']) + ' yrs old.'


        for row in con.execute(
            "SELECT * FROM person_pet WHERE person_id =?", [(choice_person)]):

            for name in con.execute(
                "SELECT * FROM person WHERE id =?", [(choice_person)]):
                pet_owner = name['first_name'] + ' ' + name['last_name']


            for row_pet in con.execute(
                "SELECT * FROM pet WHERE id =?", [(row['pet_id'])]):

                if row_pet['dead'] == 0:
                    print (pet_owner + ' owned ' + row_pet[
                    'name'] + ', a ' + row_pet['breed'] + ' who was ' + str(
                        row_pet['age']) + ' years old.')
            else:
                if row_pet['dead'] != 0:
                    print (pet_owner + ' owns ' + row_pet[
                        'name'] + ', a ' + row_pet['breed'] + ' who is ' + str(
                            row_pet['age']) + ' years old.')

except lite.Error as e:
    print "Closing."
    print "Error: %s " % e.args[0]
    sys.exit(1)

finally:
    if con:
        con.close()
