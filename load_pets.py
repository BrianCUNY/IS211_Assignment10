#! /usr/bin/env python3

#IS211 Assignment 10 - "load_pets.py" 1/2

import sqlite3 as lite
import sys

#loads below data into pets.db

people = (
	(1, 'James', 'Smith', 41),
	(2, 'Diana', 'Greene', 23),
	(3, 'Sara', 'White', 27),
	(4, 'William', 'Gibson', 23))

pets = (
	(1, 'Rusty', 'Dalmation', 4, 1),
	(2, 'Bella', 'Alaskan Malamute', 3, 0),
	(3, 'Max', 'Cocker Spaniel', 1, 0),
	(4, 'Rocky', 'Beagle', 7, 0),
	(5, 'Rufus', 'Cocker Spaniel', 1, 0),
	(6, 'Spot', 'Bloodhound', 2, 1))

person_pet = (
	(1, 1),
	(1, 2),
	(2, 3),
	(2, 4),
	(3, 5),
	(4, 6))

con = None

try:
	con = lite.connect('pets.db')
	cur = con.cursor()
	cur.execute('DROP TABLE IF EXISTS person')
	cur.execute("CREATE TABLE IF NOT EXISTS person(id INT PRIMARY KEY,"
				"first_name TEXT, last_name TEXT, age INT)")
	cur.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", people)
	cur.execute("DROP TABLE IF EXISTS pet")
	cur.execute("CREATE TABLE IF NOT EXISTS pet(id INT PRIMARY KEY, name TEXT,"
				"breed TEXT, age INT, dead INT)")
	cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?. ?)", pets)
	cur.execute("DROP TABLE IF EXISTS person_pet")
	cur.execute("CREATE TABLE person_pet(person_id INT, pet_id INT)")
	cur.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)
	
	
