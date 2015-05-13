# -*- coding: utf-8 -*-
import subprocess, time

class Envelope_print:
    
    def __init__(self,printer_name=None,infilename=None):
        
        self.printer_name, self.infilename = \
            printer_name, infilename


    def read_file(self):
        
        members = []
        inputfile = open(self.infilename,'r')
        inputfile.readline()

        for line in inputfile:
            line = line.split(',')
            members.append({'Medlemsnr.':line[0],\
                          'Etternavn':line[1],\
                          'Fornavn':line[2],\
                          'Gateadresse':line[3],\
                          'Postadresse':line[4],\
                          'E-mail':line[5],\
                          'Velkomstbrev':line[6],\
                          'Frøkort':line[7]})


        self.members = members
        inputfile.close()
        
    def print_envelopes(self):
        
        for reciever in self.members:

            if reciever['Frøkort'] == 'nei':
                printerfile = open("Printerfile.txt",'w')
                printerfile.write(reciever['Fornavn']+" "+\
                                  reciever['Etternavn']+"\n")
                printerfile.write(reciever['Gateadresse']+"\n")
                printerfile.write(reciever['Postadresse'])
                printerfile.close()
                '''
                subprocess.Popen(["lpr","-P%s"%self.printer_name,\
                                  "Printerfile.txt"])
                '''
                time.sleep(5)
                subprocess.Popen(["rm","Printerfile.txt"])
                '''
                command = "lpr -P"+self.printer_name+" <<< "+ " \" "+\
                          reciever['Fornavn']+" "+\
                          reciever['Etternavn']+" \n "+\
                          reciever['Gateadresse']+" \n "+\
                          reciever['Postadresse']+" \" "
                print command.split()
                subprocess.Popen(command.split())
                '''
                '''
                subprocess.check_call(["lpr","-P%s"%self.printer_name,\
                                       "<<<","\"",\
                                       reciever['Fornavn'],\
                                       reciever['Etternavn'],"\n",\
                                       reciever['Gateadresse'],"\n",\
                                       reciever['Postadresse'],"\""])
                '''

test = Envelope_print("fys7","test.csv")
test.read_file()
test.print_envelopes()
