from urllib.request import urlopen

page = urlopen('')

html_script = page.read().decode('utf-8')
#print(html_script)

f = html_script.find('mins')
print(f)













