import downlaod_manager, os, base_files

    
if __name__ == '__main__':
## Configuration
    while True:
        console = input("""Choos your console:  Switch / 3DS / 

        \> """).upper()

        if console == 'SWITCH':
            url = '!!'
            base_files.nintendo_switch()
            break

        elif console == '3DS':
            url = '!!'
            base_files.nintendo_3ds()
            break

        else:
            print('Pleas insert one of these Switch, 3DS ')
    
    optional = base_files.list_ini(url,console)
    os.system('cls')

## Main Script

    def optional_downlaod(app):
        
        if app['type'] == 'git':
            downlaod_manager.download_git(app['url'],int(app['num']),app['path'])

        elif app['type'] == 'wd':
            downlaod_manager.download_wiidatabase(app['url'],app['path'])
        
        elif app['type'] == 'dl':
            downlaod_manager.download_direct(app['url'],app['path'])

        else:
            print('Unkonown download type!')

    while True:
        for i,App in enumerate(optional):
            print(f"{i+1}.  {App['name']}")

        if len(optional) == 0:
            break
        
        print('''\n   ######## Add a optional App ########
        add all with "all"  |   "x" for next step\n''')
        choos = input('\> ')

        if str(choos).upper() == 'X':
            break
        
        elif str(choos).upper() == 'ALL' or str(choos).upper() == 'A':
            for i,App in enumerate(optional):
                optional_downlaod(App)
            break

        else:
            
            optional_downlaod(optional[int(choos)-1])

            optional.remove(optional[int(choos)-1])
            os.system('cls')