import subprocess
import json

#sudo flatpak list >> installed-flatpaks
#sudo apt list --installed >> installed-apt-gets
#sudo snap list >> installed-snaps


## NOTES
########################################################################
##
## <-- First we want to load the data from the shell. We receive the
## data for apt packages, flatpaks, and snap packages. It's simple, we
## just execute the commands
##      - apt list
##      - flatpak list
##      - snap list
## in the terminal and then store the output into separate files for each.
## After that we turn the text into objects that can be readable by the
## program and give us the most consistent output for each -->
##
########################################################################

## InstalledPackagesToObjectLists Class
########################################################################
class InstalledPackagesToObjects:

    def __init__(self):

        # IO Path !-> Keep the slash
        io_path = "list_of_installs"

        #Listed installed apps
        self.fp = subprocess.check_output(["flatpak list"], shell=True)
        self.apt = subprocess.check_output(["apt list"], shell=True)
        self.snap = subprocess.check_output(["snap list"], shell=True)

        #To file IO
        _io = open("installed_flatpaks", "wb+")
        _io.write(self.fp)
        _io.close()

        _io = open("installed_apts", "wb+")
        _io.write(self.apt)
        _io.close()

        _io = open("installed_snaps", "wb+")
        _io.write(self.snap)
        _io.close()

        # Debug
        # !-> Can be commented out later
        # print(fp.decode("utf-8"))
        # print(apt.decode("utf-8"))
        # print(snap.decode("utf-8"))

    ##############################
    ##  Objects should carry    ##
    ##      - Name              ##
    ##      - Version           ##
    ##      - Type of Install   ##
    ##############################

    # Underscored values represent variables used
    # temporarily within the scope of the function

    def ObjectifyFlatpaks(self):
        _io = open("installed_flatpaks", "r")
        print("> Installed Flatpaks")

        # Formatting needs work but we'll keep it for now
        for _ in _io:

            name = _.split()[0]
            application_id = _.split()[1]
            version = _.split()[2]
            branch = _.split()[3]
            installation_type = "Flatpak Installation"

            dictionary = {
                "name": name,
                "version": version,
                "type": installation_type
            }

            # Serializing json
            json_object = json.dumps(dictionary, indent=4)

            # Writing to sample.json
            file_name = "installs/" + name + ".json"
            with open(file_name, "w") as outfile:
                outfile.write(json_object)

            print(name, end = " ") #Field 0
            print(application_id, end = " ") #Field 1
            print(version, end = " ") #Field 2
            print(installation_type) #Field 3
        _io.close()


    def ObjectifyApts(self):
        _io = open("installed_apts", "r")
        print("> Installed Apts")

        ignoreFirstRun = True
        for _ in _io:
            if ignoreFirstRun:
                ignoreFirstRun = False
                continue

            name = _.split()[0]
            version = _.split()[1]
            installation_type = "Apt Installation"

            dictionary = {
                "name": name,
                "version": version,
                "type": installation_type
            }

            # Serializing json
            json_object = json.dumps(dictionary, indent=4)


            # Writing to sample.json
            file_name = "installs/" + name.split("/")[0] + ".json"
            with open(file_name, "w") as outfile:
                outfile.write(json_object)

            print(name, end=" ")
            print(version, end=" ")
            print(installation_type)

    def ObjectifySnaps(self):
        _io = open("installed_snaps", "r")
        print("> Installed Snaps")

        ignoreFirstRun = True
        for _ in _io:
            if ignoreFirstRun:
                ignoreFirstRun = False
                continue

            name = _.split()[0]
            version = _.split()[1]
            installation_type = "Snap Installation"

            dictionary = {
                "name": name,
                "version": version,
                "type": installation_type
            }

            # Serializing json
            json_object = json.dumps(dictionary, indent=4)

            # Writing to sample.json
            file_name = "installs/" + name + ".json"
            with open(file_name, "w") as outfile:
                outfile.write(json_object)


            print(_.split()[0], end=" ")
            print(_.split()[1], end=" ")
            print(_.split()[2])
########################################################################




obj = InstalledPackagesToObjects()
obj.ObjectifyFlatpaks()
obj.ObjectifyApts()
obj.ObjectifySnaps()

