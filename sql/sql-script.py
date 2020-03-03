import mysql.connector as mysql

conn = mysql.connect(user='jerry', password='fuckMe', host='127.0.0.1')
cursor = conn.cursor()


cursor.execute('create database if not exists python')
cursor.execute('use python')
cursor.execute('create table if not exists people(id int, firstname varchar(20), lastname varchar(20))')
# create 4 rows
cursor.execute('insert into people (id, firstname, lastname) values ("1","Gjermund","Fougner Haugen")')
cursor.execute('insert into people (id, firstname, lastname) values ("2","Aud","Haugen Fougner")')
cursor.execute('insert into people (id, firstname, lastname) values ("3","Egil","Haugen")')
cursor.execute('insert into people (id, firstname, lastname) values ("4","Ingrid","Haugen Fougner")')
cursor.execute('insert into people (id, firstname, lastname) values ("5","Rigmor","Fougner")')
cursor.execute('insert into people (id, firstname) values ("6","Foufou")')
# update a row
cursor.execute('update people set id= "10" where id="1"')

# delete a row
cursor.execute('delete from people where lastname="haugen"')

conn.commit()
cursor.execute('select * from people')
print(cursor.fetchall())
