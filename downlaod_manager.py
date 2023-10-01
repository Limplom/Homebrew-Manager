import urllib.request, shutil, os, GetGit

def download_direct(direct_url,download_path='SD/'):
        file_name = str(direct_url).split('/')[-1]
        urllib.request.urlretrieve(direct_url,download_path + file_name)


def download_git(git_url, download_number: int, download_path: str ='SD/'):
    URL = GetGit.newest_releses(git_url)[download_number-1]
    file_name = str(URL).split('/')[len(str(URL).split('/'))-1]


    if file_name.endswith('.zip') or file_name.endswith('.rar'):
        urllib.request.urlretrieve(URL,file_name)
        shutil.unpack_archive(file_name,download_path)
        os.remove(file_name)
        
    else:
        os.makedirs(download_path,exist_ok=True)
        urllib.request.urlretrieve(URL,download_path+file_name)

def download_wiidatabase(URL, download_path='SD/'):
    try:
        file_name = str(URL).split('/')[len(str(URL).split('/'))-2]
        urllib.request.urlretrieve(URL,file_name)
        shutil.unpack_archive(file_name,download_path)
        os.remove(file_name)
    except:
        os.remove(file_name)

        file_name = file_name+'.zip'
        urllib.request.urlretrieve(URL,file_name)
        shutil.unpack_archive(file_name,download_path)
        os.remove(file_name)