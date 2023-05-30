#Nombre: Isaac Emilio Esparza Vazquez
#Matricula: 2012872

import nmap

ecaner = nmap.PortScanner()
scaner.scan('192.168.1.5','1-1024','-v-sV')
scaner.command_line() 
scaner.all_hosts()
scaner['192.168.1.5'].state() 
scaner['192.168.1.5'].all_protocols() 
scaner['192.168.1.5']['tcp'].keys() 
scaner['192.168.1.5'].has_tcp(21) 
scaner['192.168.1.5'].has_tcp(22)
print(scanner['192.168.1.5']['tcp'][22])
print(scanner['192.168.1.5']['tcp'][22]["product"])
