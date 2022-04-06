from time import sleep
import virtualbox
import os
import shutil

vbox = virtualbox.VirtualBox()

machines = {}
sessions = {}

quit = False

def getMachines():
    counter = 0
    for m in vbox.machines:
        counter += 1
        machines[counter] = m.name
getMachines()

def checkMachines():
    getMachines()
    print("Machines available:\n-------------------")
    for id, m in machines.items():
        print(id, " => ", m)

def startMachine():
    checkMachines()
    print()
    id = int(input("Enter de machine's ID: "))
    machineName = machines[id]
    if(machineName not in sessions):
        session = virtualbox.Session()
        sessions[machineName] = session
        machine = vbox.find_machine(machines[id])
        progress = machine.launch_vm_process(session, "gui", [])
        progress.wait_for_completion()
        print("Machine up")
    else:
        print("Machine already up")

def startMachineAdmin(id):
    machineName = machines[id]
    if(machineName not in sessions):
        session = virtualbox.Session()
        sessions[machineName] = session
        machine = vbox.find_machine(machines[id])
        progress = machine.launch_vm_process(session, "gui", [])
        progress.wait_for_completion()
        print("Machine up")
    else:
        print("Machine already up")

def powerOffMachine():
    checkMachines()
    print()
    id = int(input("Enter the machine's ID to power off: "))
    if(machines[id] not in sessions):
        print("Machine not powered up")
    else:
        session = sessions[machines[id]]
        session.console.power_down()
        del sessions[machines[id]]
        print("Machine down")

def powerOffMachineAdmin(id):
    if(machines[id] not in sessions):
        print("Machine not powered up")
    else:
        session = sessions[machines[id]]
        session.console.power_down()
        del sessions[machines[id]]
        print("Machine down")

def createMachine():
    machine = input("Enter the machine name (vagrant format): ")
    dirname = machine.split("/")[0]
    dirname = directoryExists(dirname)
    os.mkdir("./" + dirname)
    os.chdir("./" + dirname)
    os.system("vagrant init " + machine)
    os.system("vagrant up")
    getMachines()
    id = list(machines.keys())[-1]
    # powerOffMachineAdmin(id)
    os.system("vagrant halt")
    startMachineAdmin(id)
    os.chdir("../")

def directoryExists(dirname):
    counter = 0
    if(os.path.exists(dirname)):
        directories = os.listdir()
        for dir in directories:
            if(dirname in dir):
                counter += 1
        
        return dirname + "_" + str(counter)
    else:
        return dirname

def deleteMachine():
    checkMachines()
    print()
    id = int(input("Enter de machine's ID: "))
    if(id in machines):
        if(machines[id] in sessions):
            powerOffMachineAdmin(id)

        dirname = str(machines[id]).split("_default")[0]
        os.chdir("./" + dirname)
        os.system("vagrant destroy")
        os.chdir("../")
        shutil.rmtree("./" + dirname)
        del machines[id]
        print("Machine deleted")
    else:
        print("Machine not found")

while not quit:
    print("VM MANAGER\n==========")
    print("0 to quit")
    print("1 Check machines available")
    print("2 Start machine")
    print("3 Power off the machine")
    print("4 Create machine")
    print("5 Delete machine")

    option = int(input("Enter an option: "))

    print("\n==========================================")

    if(option == 0):
        quit = not quit
    elif(option == 1):
        checkMachines()
    elif(option == 2):
        startMachine()
    elif(option == 3):
        powerOffMachine()
    elif(option == 4):
        createMachine()
    elif(option == 5):
        deleteMachine()

    print("==========================================\n")

    sleep(3)