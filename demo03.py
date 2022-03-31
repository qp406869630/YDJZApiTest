# encoding = 'utf-8'
import os

cmd = 'cmd.exe /k rd/s/q report\my_allure_results'
# os.system(cmd)
os.popen(cmd)
# cmd2 = 'cmd.exe /k allure generate report\my_allure_results -o report\html --clean'
# os.system(cmd2)