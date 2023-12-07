import os
import psutil
# clear = lambda: os.system('cls')
# i = int(input())

# if i == 1:
#     clear()
parent_pid = os.getppid()
print(psutil.Process(parent_pid).name())