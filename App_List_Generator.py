import ast, os

while True:
    console = input("""Choos your console:  Switch / 3DS / 

    \> """).upper()

    if console == 'SWITCH':
        url = '!!'
        break

    elif console == '3DS':
        url = '!!'
        break

    else:
        print('Pleas insert one of these Switch,3DS ')

os.system('cls')

try:
    with open(f'./{console}_list.ini', 'r') as File:
        apps = ast.literal_eval(File.read())

except FileNotFoundError:
    with open(f'./{console}_list.ini', 'w') as File:
        File.write('[]')

    with open(f'./{console}_list.ini', 'r') as File:
        apps = ast.literal_eval(File.read())


print('''   ######## Add a optional App ########
                        "x" finish ''')

while True:
    vorlage = {}

    name = input('Name der App: ')
    vorlage["name"] = name

    url = input('Url der App: ')
    vorlage["url"] = url

    type = input("""Downlaod types:     
        git : Github
        wd : Wiidatabase
        dl : DirectLink
    
    Download Typ: """).lower()
    vorlage["type"] = type

    if type == 'git':
        download_num = input('Download Number: ')
        vorlage["num"] = download_num


    path = input('Optionaler Download Path: ')

    if path != '' or path == ' ':
        vorlage["path"] = path
    else:
        vorlage["path"] = 'SD/'

    exit = input()
    apps.append(vorlage)

    if exit.upper() == 'X':
        break

apps = str(apps).replace("'",'"')
print(apps)
File = open(f'./{console}_list.ini', 'w').write(apps)
