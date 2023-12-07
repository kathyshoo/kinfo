## import
import os
import psutil
import time
import requests
import tqdm
import zipfile

toro_toro = """
            ,.  ,.
            ||  ||
           ,''--''.
          : (.)(.) :
         ,'        `.
         :          :
         :          :
   -ctr- `._m____m_,' 
   """

parent_pid = os.getppid()
parInterp = psutil.Process(parent_pid).name()

match parInterp:
    case "cmd.exe": clear = lambda: os.system('cls')
    case "powershell.exe": clear = lambda: os.system('cls')
    case _: clear = lambda: os.system('')

fil = open("infos/info.txt", 'r')
temp = fil.read()
urls = {
    temp.split('\n')[0].split('$')[0]:temp.split('\n')[0].split('$')[1],
    temp.split('\n')[1].split('$')[0]:temp.split('\n')[1].split('$')[1]
}

def main():
    clear()
    print(toro_toro)
    print("""What r u need?
1. install DLC crack for HOI4
2. download and install DLCs for HOI4
0. exit""")
    try:
        num = int(input('answer: '))
    except:
        print("error... returning to main menu")
        time.sleep(3)
        clear()
        main()
    match num:
        case 0: exit()
        case 1: download_crack()
        case 2: pass
        case _: 
            print('неправильный номер')
            main()

def download_crack():
    clear()
    path_game = input("please enter the path to the HOI4 directory [C:\\Program Files (x86)\\Steam\\steamapps\\common\\Hearts of Iron IV]: ")
    if path_game == "":
        path_game = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Hearts of Iron IV"
    if not os.path.isfile(path_game + "\\hoi4.exe"):
        print("the executable file was not found in the directory... returning to main menu")
        time.sleep(3)
        clear()
        main()
    else:
        print("the executable file was detected, starting to download fix")

    with open("crack.zip", 'wb') as f:
        with requests.get(urls['crack'], stream = True) as r:
            r.raise_for_status()
            total = int(r.headers.get('content-length', 0))
            tqdm_parametrs = {
                'desc': 'crack',
                'total': total,
                'miniters': 1,
                'unit': 'it',
                'unit_scale': True,
                'unit_divisor': 1024
            }
            with tqdm.tqdm(**tqdm_parametrs) as pb:
                for chunk in r.iter_content(chunk_size=8192):
                    pb.update(len(chunk))
                    f.write(chunk)

    os.rename(path_game + '\\steam_api64.dll', path_game + '\\steam_api64_o.dll')
    
    with zipfile.ZipFile('crack.zip', 'r') as archive:
        archive.extractall(path_game)

    print("ready... returning to main menu")
    time.sleep(3)
    clear()
    main()
    

if __name__ == '__main__':
    main()