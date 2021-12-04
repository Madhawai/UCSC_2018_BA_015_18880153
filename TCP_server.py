# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:00:54 2021

@author: madhawa
"""

import socket 
import sys
import time
import Data_Manage_2 as DM


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

server_address = (HOST, PORT)
print (sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
#    print (sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    try:
#        print (sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
#            print (sys.stderr, 'received "%s"' % data)
            if data:
#                print (sys.stderr, 'sending data back to the client')
                txt= data.decode("utf-8")                
                D1 = txt.split(", ")
                print("01   txt  ==============" , txt)
                print("02 Split Data List  ==============" ,D1)
                if D1[0]=="CLIENT_SEND_CONFIG_DATA":                   
                    Lower = float(D1[1])
                    Upper = float(D1[2])
                    Ratio = float(D1[3])
                    No_of_Variable =int(D1[4])
                    
                    Customer= ["NULL"]
                    Out_put_data,Out_Fea_List,Load_Parametres = DM.main(Lower,Upper,Ratio,No_of_Variable,Customer) 
                    
#                    Send_data = "SERVER_SEND_CONFIG_OUT_DATA" + "," +"68" + "," +"71000"  + "," + "67"  + "," +"25000"  + "," + "66" + "," + "20000" + "," + "65"  + "," + "5000"  + "," + "64"  + "," + "15000" + "," +"63" + "," +"11000" + "," +"62" + "," +"4000"  + "," +"1" + "," +"2" + "," +"3" + "," +"4" + "," +"5" + "," +"6"
                    Send_data1 = "SERVER_SEND_CONFIG_OUT_DATA"
                    for i in range (26):
                        A= Out_put_data[i+1]
                        if isinstance(A, str):
                            Send_data1=Send_data1+","+A
                        else:
                            Send_data1=Send_data1+","+str(A)
                    
                    print("\n\n ==== Data Send to Server  ================================", Send_data1 )
                    connection.sendall(bytes(Send_data1, 'utf-8'))
                    
                    time.sleep(1)
                    
                    Numer_FL , Bool_FL = Out_Fea_List
                    Nume_ls = Numer_FL["Specs"].tolist()
                    Bool_ls = Bool_FL["Specs"].tolist()
                        

                    Send_data2 = "SERVER_SEND_FEA_LIST_DATA"
                    for i in range (len(Nume_ls)):
                        A= Nume_ls[i]
                        if isinstance(A, str):
                            Send_data2=Send_data2+","+A
                        else:
                            Send_data2=Send_data2+","+str(A)
                            
                    for i in range (len(Bool_ls)):
                        A= Bool_ls[i]
                        if isinstance(A, str):
                            Send_data2=Send_data2+","+A
                        else:
                            Send_data2=Send_data2+","+str(A)
                    
                    connection.sendall(bytes(Send_data2, 'utf-8'))

#'''============ Customer Data LOAD============================== '''

                if D1[0]=="CUSTMER_DATA_LOAD":   
                    print("\n\nCUSTMER_DATA_VALI",)
                    Lower = float(D1[1])
                    Upper = float(D1[2])
                    Ratio = float(D1[3])
                    No_of_Variable =int(D1[4])
                    
                    
                    Customer= ["LOAD"]
                    
                    Out_put_data,Out_Fea_List,OUT_Parametres = DM.main(Lower,Upper,Ratio,No_of_Variable,Customer) 
                    
                    Send_data3 = "CUSTMER_DATA_LOAD_OUT"
                    for i in range (len(OUT_Parametres)):
                        Load= OUT_Parametres[i]
                        print('==== ', i ,'=======',Load)
                        if isinstance(Load, str):
                            Send_data3=Send_data3+"," + Load
                        else:
                            Send_data3=Send_data3+","+str(round(Load,3))
                            
                    print("\n\n ==== Data Send to Server  ================================", Send_data3 )
                    time.sleep(1)
                    connection.sendall(bytes(Send_data3, 'utf-8'))
                    time.sleep(1)

#'''============ Customer Data validation============================== '''

                if D1[0]=="CUSTMER_DATA_VALI":   
                    print("\n\nCUSTMER_DATA_VALI  :",txt)
                    Lower = float(D1[1])
                    Upper = float(D1[2])
                    Ratio = float(D1[3])
                    No_of_Variable =int(D1[4])
                    
                    var_n=[]
                    print("lenDi-------",len(D1), '====',((len(D1)-5)/2))
                    for i in range (int((len(D1)-5)/2)) :
                        var_n= var_n+ [str(D1[i+5])]

                    var_V=[]
                    for i in range (int((len(D1)-5)/2)) :
                        var_V=var_V +[ float(D1[i+19])]
                                            
                    
                    Customer= ["VALID"] + var_n + var_V
                    
                    Out_put_data,Out_Fea_List,OUT_Parametres = DM.main(Lower,Upper,Ratio,No_of_Variable,Customer) 
                    
                    Send_data4 = "CUSTMER_DATA_VALI_OUT"
                    print("\n\n\nOUT_Parametres==== : ", OUT_Parametres)
                    for i in range (len(OUT_Parametres)):
                        Load= OUT_Parametres[i]
                        print('==== ', i ,'=======',Load)
                        if isinstance(Load, str):
                            Send_data4=Send_data4+"," + Load
                        else:
                            Send_data4=Send_data4+","+str(round(Load,3))
                            
#                    Send_ACC=""
#                    for i in range (5):
#                        A= Out_put_data[i+19]
#                        if isinstance(A, str):
#                            Send_ACC=Send_ACC+","+A
#                        else:
#                            Send_ACC=Send_ACC+","+str(A)
#                    
#                    Send_data4=Send_data4+Send_ACC
#                            
                    
                    print("\n\n ==== Data Send to Server  ================================", Send_data4 )
                    time.sleep(1)
                    connection.sendall(bytes(Send_data4, 'utf-8'))
                    time.sleep(1)

            
    finally:
        # Clean up the connection
        connection.close()

