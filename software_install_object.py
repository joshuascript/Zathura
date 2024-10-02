import os
import json

_list = []
class ObjectLoader:
    def load():
        # assign directory
        directory = 'installs'

        # iterate over files in
        # that directory
        data = ""
        idx = 0
        for filename in os.scandir(directory):
            if filename.is_file():
                with open(filename.path, 'r') as file:
                    data = json.load(file)

                swo = SoftwareInstallObject(data.get('name'), data.get('version'), data.get('type'))
                _list.append(swo)
                idx+=1

class SoftwareInstallObject:
    def __init__(self, name, version, install_type):
        self.name = name
        self.version = version
        self.install_type = install_type

    def __str__(self):
        return self.name + " " + self.version + " " + self.install_type

