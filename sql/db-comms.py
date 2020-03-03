import myDBconfig
import mysql.connector as mysql
print('Database: python, Table: people')
conn = mysql.connect(**myDBconfig.dbConfig)
cursor = conn.cursor()
cursor.execute('use python')
cursor.execute('explain people')
columns = cursor.fetchall()

while True:
    print('Enter column you wish to use:')
    for i in columns:
        print('-', i[0])

    print()
    select = input('Enter column: ')
    keyword = input('Enter value to search for: ')
    try:
        cursor.execute(f'select * from people where {select}="{keyword}"')
        result = cursor.fetchall()
        print()
        print('ID=', result[0][0],':', 'Firstname=', result[0][1],':', 'Lastname=', result[0][2])
    except:
        print('not found')