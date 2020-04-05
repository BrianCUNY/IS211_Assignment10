#! /usr/bin/env python3

#IS211 Assignment 10 - "query_pets.py" 2/2

import sqlite3 as lite
import sys

#query for the pets.db

con = lite.connect('pets.db')

with con:
	cur = con.cursor()
	
	while True:
		id_num = input('Enter person\'s ID number or enter -1 to exit')
		if id_num == '-1':
			print('Exiting DB query now')
			raise SystemExit
		
		cur.execute('SELECT first_name, last_name, person.age, name, breed,'
					'pet.age, dead FROM person, pet, person_pet'
					'WHERE person.id = person_pet.person_id AND'
					'pet.id = person_pet.pet_id AND person.id =(?)', (id_num))
		
		person = cur.fetchall()
		
		if len(person) == 0:
			print('Invalid Input/Entry')
			continue
		
		for row in person:
			first_name = row[0]
			last_name = row[1]
			age = row[2]
			pet_name = row[3]
			pet_type = row[4]
			pet_age = row[5]
			living = row[6]
			if living == 1:
				print('{} {}, age {} has a {} called {}, who was {} old.').format(
						first_name, last_name, age, pet_type, pet_name, pet_age)
			
			else:
					print('{} {}, age {}, had a {} called {}, who was {} years old.').format(
							first_name, last_name, age, pet_type, pet_name, pet_age)
							
