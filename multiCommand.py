# Multiple Powershell Scripts in a Python Program

import subprocess

commandOne = ["powershell", "-Command", "Get-Date"]
commandTwo = ["powershell", "-Command", "Get-Process"]
commandThree = ["powershell", "-Command", "Get-ComputerInfo"]

commandList = [commandOne, commandTwo, commandThree]

for command in commandList:
    subprocess.run(command)