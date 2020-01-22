import cgi

data = cgi.FieldStorage()
username = data.getvalue('user_cred')
password = data.getvalue('user_pass')

name = 'not found'
surname = 'not found'
email = 'not found'
phonenr = 'not found'
pet1 = ''
pet2 = ''
pet3 = ''

if username == 'jerry' and password == 'abc123':
    name = 'Gjermund'
    surname = 'fuckface'
    email = 'kuk@gmail.com'
    phonenr = '93592485791'


print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Student details</title>")
print("</head>")
print("<body>")
print("<h1>Name: {}<br/>Surname: {}</h1>".format(name, surname))
print("<p>Email: {}<br/>Phone: {}</p>".format(email, phonenr))
print("<h3> My pets: <h3/>")
print("<a href=\"petdetails.py?pet=1\">Pet 1</a></br>")
print("<a href=\"petdetails.py?pet=2\">Pet 2</a></br>")
print("<a href=\"petdetails.py?pet=3\">Pet 3</a></br>")
print("<a href=\"login.html\">Logout</a>")
print("</body>")
print("</html>")