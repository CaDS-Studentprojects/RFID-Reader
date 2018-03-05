#!/usr/bin/env python

import json
import os.path

class File_Manager:

    def export_JSON(self, data, filename):
        json_string = json.dumps(data)
        file = open(filename, "w+")
        file.write(json_string)
        file.close()


    def import_JSON(self, file_path):
        json_string = ""

        if os.path.exists(file_path):
            print "Found file " + file_path
            file = open(file_path, "r+")
            json_string = file.read()
            file.close()
        else:
            print "File not found"

        return json_string
