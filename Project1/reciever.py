import socket as sk

s=sk.socket(sk.AF_INET , sk.SOCK_DGRAM)# we will send msg and recieve via internet,protocol is UDP
ip_address="127.0.0.1"
port_no=2525
address=(ip_address,port_no)
s.bind(address)  #reister
#while True:
    #Data=s.recvfrom(100)
    #message=Data[0]
    #ip_address=Data[1][0]
    #print(ip_address,">>>>>>",message)
      # create file demo.txt and msg hii 
      #send this file from sender to reciever
      # read file  before sending it and write it 
    
with open('demo.txt','w') as f:
  while True:
      data,addr=s.recvfrom(100)
      print(f"recieved message from {addr}:{data}")
      if not data:
        break
      f.write(data)
  print("file transfer complete.")