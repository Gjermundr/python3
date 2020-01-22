import cgi





# Displayed Web page
print('Content-Type: text/html')
print()
print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Noroff Grade Calculator!</title>')
print('</head>')
print('<body>')
print('<h1>Noroff grade-score calculator!</h1>')
print('<h3>Input your results and see your average letter grade</h3>')
print('''
<form method="POST" action="processgrades.py">
<
</form>
''')
print('</body>')
print('</html>')