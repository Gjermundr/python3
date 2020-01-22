import os, cgi
data = cgi.FieldStorage()
upload = data['imagefile']
filename = os.path.basename(upload.filename)

with open(filename, 'wb') as copy:
    copy.write(upload.file.read())



burger_meat = data.getvalue('meat')
burger_bread = data.getvalue('bread')
lprogram = data.getvalue('lprogram')
price = 0

if burger_meat == data.getvalue('beef'):
    price += 7
elif burger_meat == data.getvalue('chicken'):
    price += 4
elif burger_meat == data.getvalue('rib'):
    price += 11
elif burger_meat == data.getvalue('vegetarian'):
    price += 7
if burger_bread == data.getvalue('normal'):
    price += 3
elif burger_bread == data.getvalue('ciabatta'):
    price += 4
elif burger_bread == data.getvalue('angus'):
    price += 5

toppings = '<ul>'

if data.getvalue('cheese'):
    toppings += '<li>Cheese: 3 NOK</li>'
    price += 3
if data.getvalue('tomato'):
    toppings += '<li>' + 'Tomato' + ': 2 NOK</li>'
    price += 2
if data.getvalue('bacon'):
    toppings += '<li>' + 'Bacon' + ': 4 NOK</li>'
    price += 4
if data.getvalue('raddish'):
    toppings += '<li>' + ' Raddish' + ': 6 NOK</li>'
    price += 6
if data.getvalue('redonions'):
    toppings += '<li>' + ' Red onions' + ': 2 NOK</li>'
    price += 2
if data.getvalue('pickles'):
    toppings += '<li>' + ' pickles' + ': 1 NOK</li>'
    price += 1

toppings += '</ul>'



print('Content-Type: text/html')
print()
print('<!DOCTYPE HTML>')
print('<html>')
print('<head>')
print('<meta charset=\"UTF-8\">')
print('<title>Ham-Builder results!</title>')
print('</head>')
print('<body>')
print('<h3>Build-A-Burger Receipt:</h3>')
print('Meat: {}<br>'.format(burger_meat))
print('Bread: {}<br>'.format(burger_bread))
print('Thank you for choosing: ', lprogram, '<br>')
print('Toppings:')
print(toppings)
print('Total: ', price,'<br><br>')
print("Image Upload:<br><img src=\"{}\"/><br/><br/>".format(filename))
print("<a href=\"buildhamburger.html\">Back</a>")
print('<br>')
print('</body>')
print('</html>')