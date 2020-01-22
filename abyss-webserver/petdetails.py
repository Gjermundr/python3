import cgi
data = cgi.FieldStorage()
pet = data.getvalue("pet")

pet_name = 'error'
pet_age = 'error'
pet_type = 'error'
pet_description = 'error'


if pet == '1':
    pet_name = 'Rassefant'
    pet_age = '100 år'
    pet_type = 'Bikje'
    pet_description = '''
    En stor svær feit bikje.
    '''
elif pet == '2':
    pet_name = 'Kønthøl'
    pet_age = '12'
    pet_type = 'menneske'
    pet_description = '''
    liten bitch, må vaskes en gang i månden.
    '''

elif pet == '3':
    pet_name = 'Saturn'
    pet_age = '3'
    pet_type = 'katt'
    pet_description = '''
    en kul katt. RIP <3
    '''

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Pet details</title>")
print("</head>")
print("<body>")
print("<h1> My pet: <h1/>")
print("<h3>Name: {}<br/>Type: {}</h1>".format(pet_name, pet_type))
print("<p>Age: {}<br/>Description: {}</p>".format(pet_age, pet_description))
print("</body>")
print("</html>")