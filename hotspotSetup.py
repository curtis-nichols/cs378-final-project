import os
import config
from typing import List

def readFileLines(fileName: str) -> List[str]:
    f = open(fileName, "r")
    fileLines = [line.rstrip() for line in f]
    f.close()
    return fileLines

def writeFileContents(fileName:str, contents: List[str]) -> None:
    f = open(fileName, "w")
    for line in contents:
        f.write(line + "\n")
    f.close()

def runCommands(commandsToRun: List[str]) -> bool:
    for command in commandsToRun:
        successRequired = True
        #allow comments in the commands file
        if command[0] == "#":
            continue
        #put this character at the start for commands that 
        #aren't required to have exit code 0
        elif(command[0] == "!"):
            successRequired = False
            command = command[1:]
        output = os.system(command)
        print(command, output)
        if successRequired and output != 0:
            print("A command was unsuccessful, edit the command file and try running this again!")
            return False
    
    print("The hotspot was successfully set up and configured to redirect to your Apache2 website!")
    return True

def performSetup() -> bool:
    #read in shell commands to execute
    commandsToRun = readFileLines(config.COMMANDS_FILE)
    dnsmasqTemplate = readFileLines(config.DNSMASQ_TEMPLATE_FILE)
    hostapdTemplate = readFileLines(config.HOSTAPD_TEMPLATE_FILE)

    #replace variables in the template file with our configuration
    dnsmasqFile = [line.format(wifiInterface=config.WIFI_INTERFACE) for line in dnsmasqTemplate]
    hostapdFile = [line.format(wifiInterface=config.WIFI_INTERFACE, ssid=config.HOSTAPD_SSID, driver=config.HOSTAPD_DRIVER) for line in hostapdTemplate]

    writeFileContents("dnsmasq.conf", dnsmasqFile)
    writeFileContents("hostapd.conf", hostapdFile)

    return runCommands(commandsToRun)

if __name__ == "__main__":
    performSetup()

