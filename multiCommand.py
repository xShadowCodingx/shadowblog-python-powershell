# Multiple Powershell Scripts in a Python Program

import subprocess

commandOne = ["powershell", "-Command", "Get-Date"]
commandTwo = ["powershell", "-Command", "Get-Process"]
commandThree = ["powershell", "-Command", "Get-ComputerInfo"]

subprocess.run(commandOne)
subprocess.run(commandTwo)
subprocess.run(commandThree)
