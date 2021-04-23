import os

#make more stuff configurable later
commandsFile = "hotspot_setup_commands.txt"
#commandsFile = "test.txt"

def performSetup() -> bool:
    #read in shell commands to execute
    f = open(commandsFile, "r")
    commandsToRun = [line.rstrip() for line in f]
    f.close()

    print(commandsToRun)

    for command in commandsToRun:
        output = os.system(command)
        print(output)
        if output != 0:
            print("An command was unsuccessful, edit the command file and try running this again!")
            return False
    
    print("The hotspot was successfully set up and configured to redirect to your Apache2 website!")
    return True

if __name__ == "__main__":
    performSetup()

