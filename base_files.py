import downlaod_manager, os, json, shutil

def list_ini(url, console):
    try:
        optional  = open(f'./{console}_list.ini', 'r').read()

    except FileNotFoundError:
        downlaod_manager.download_direct(url,f'./{console}_list.ini')
        optional  = open(f'./{console}_list.ini', 'r').read()

    return  json.loads(optional)
    

def nintendo_switch():
    print('Downlaoding Base Files...')   
    downlaod_manager.download_git('https://github.com/Atmosphere-NX/Atmosphere',1)
    downlaod_manager.download_git('https://github.com/CTCaer/hekate',1)
    downlaod_manager.download_git('https://github.com/WerWolv/nx-ovlloader',1)
    downlaod_manager.download_wiidatabase('https://wiidatabase.de/switch-downloads/hacks/signatur-patches/?dl=0')
    downlaod_manager.download_wiidatabase('https://wiidatabase.de/switch-downloads/hacks/dvr-patches/?dl=0')
    downlaod_manager.download_git('https://github.com/Atmosphere-NX/Atmosphere/',2,'SD/bootloader/payloads/')
    downlaod_manager.download_wiidatabase('https://wiidatabase.de/switch-downloads/switch-tools/switch-homebrew-app-store/?dl=0')

def nintendo_3ds():
    print('Downlaoding Base Files...')
    downlaod_manager.download_git('https://github.com/d0k3/SafeB9SInstaller',1,'SD/')
    for file in os.listdir('SD/'):
        file_path = os.path.join('SD/', file)

        if file != 'SafeB9SInstaller.bin':
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                shutil.rmtree(file_path)

    downlaod_manager.download_git('https://github.com/d0k3/GodMode9/',1,'SD/luma/payloads/')
    for file in os.listdir('SD/luma/payloads/'):
        file_path = os.path.join('SD/luma/payloads/', file)

        if file == 'GodMode9.firm' or file == 'gm9':
            pass

        else:
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                shutil.rmtree(file_path)       
    shutil.move('SD/luma/payloads/gm9','SD/gm9/')

    downlaod_manager.download_git('https://github.com/SciresM/boot9strap/',4,'SD/boot9strap/')
    downlaod_manager.download_git('https://github.com/LumaTeam/Luma3DS/',1)
    downlaod_manager.download_git('https://github.com/zoogie/unSAFE_MODE/',2)
    downlaod_manager.download_git('https://github.com/Steveice10/FBI/',1,'SD/3ds/')
    downlaod_manager.download_git('https://github.com/Steveice10/FBI/',2,'SD/cias/')
    downlaod_manager.download_git('https://github.com/PabloMK7/homebrew_launcher_dummy/',1,'SD/cias/')



if __name__ == '__main__':
   pass