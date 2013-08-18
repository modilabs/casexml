#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

import sys
import csv

from utils import transmit_form, save_casexmlform, check_file


#Form Templates
from forms import CaseXMLInterface


class Main:

    file_name = ""
    save = True
    template = ""
    submit = False

    def __init__(self):
        ''' Get arguments '''
        args = sys.argv
        if len(args):
            try:
                self.file_name = args[1]
                self.template = args[2]
            except:
                self.file_name = ""
                self.template = ""

            if not check_file(self.file_name, "csv"):
                print "Invalid file location or file does not exist." \
                      "Check if it has a .csv extenion"
            else:
                self.export_csv()
        else:
            self.help()

    def help(self):
        print (u"------------------------------------------\n"
               u"GENERATE CASEXML USING DATA AND TEMPLATE \n"
               u"------------------------------------------\n"
               u"Contains function to generate Casexml and save or \n"
               u"submit to CommcareHq\n"
               u"To run:\n $ python casexml.py csvfile template "
               u"\n\nOPTIONS:\n-------- \n"
               u"csvfile     A full path of csv file to be exported to"
               u" CommcareHQ ")

    def export_csv(self):
        info = {}
        #Check if template exist before
        if not check_file(self.template, "xml"):
            print "Template doesnot exist, or invalid template. Check if " \
                "it has a .xml extenion"
            return 0

        try:
            data = csv.reader(open(self.file_name, 'rb'))
        except:
            print "Data doesnt exist"

        #Remove Header
        header = data.next()
        info = {}
        #Loop through each row and get data
        for x in data:
            for label, value in zip(header, x):
                info[label] = value

            form = CaseXMLInterface(info, self.template)
            save_casexmlform(form)
            if self.submit:
                transmit_form(form)


if __name__ == '__main__':
    main = Main()
