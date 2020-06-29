import re
import socket
import ipaddress

#ip address validation 
def valid_ip(addr):
    #check ip address is valid or not
    try:    
        socket.inet_aton(addr)
    except socket.error:
        print("Invalid IP")

    temp_addr = ipaddress.IPv4Address(addr)

    #check ip is not loopback or unsuable 
    if temp_addr.is_loopback or temp_addr.is_unspecified or temp_addr.is_link_local:    
        print("Please enter usable ip address!")
    else:
        None

    return temp_addr


#find subnet address and broadcast address 
def subnet(ip,mask):
    
    ip_list = ip.split('.')
    mask_list = mask.split('.')
    
    subnet_addr = []
    broadcast_addr = []
    
    classfull_bit = 0
    borrow_bit = 0
    for i,j in zip(ip_list,mask_list):
        p = int(i) & int(j)
        subnet_addr.append(str(p))

        if int(j) == 255:
            broadcast_addr.append(str(p))
            classfull_bit = classfull_bit + 8
        else:
            temp_bin = format(int(j),'08b')
            for k in temp_bin:
                if int(k) == 1:
                    borrow_bit = borrow_bit + 1
                else:
                    no_of_network = 2**borrow_bit
                    total_network_bit = classfull_bit + borrow_bit
                    no_of_host_bit = 32 - total_network_bit
                    no_of_host = (2**no_of_host_bit)

            nor_bit = 255 - int(j)
            q = int(p) | int(nor_bit)
            broadcast_addr.append(str(q))
    ans_subnet = '.'.join(subnet_addr)
    ans_broadcast = '.'.join(broadcast_addr)    
    
    
    return ans_subnet,ans_broadcast,no_of_network,no_of_host



#start Program


#user input
input_ip = '152.25.60.20'
Subnet_mask = '255.240.0.0'



IP_address = str(valid_ip(input_ip))
#print(IP_address)

Subnet_address, Broadcast_address,No_of_network, No_of_host = subnet(IP_address,Subnet_mask)
#print(Subnet_address)

# = no_of_network_host(Subnet_mask)



print('Broadcast Address : '+ Broadcast_address)
print('Network Address   : '+ Subnet_address)
print('No of Network     : '+ str(No_of_network))
print('No of Host        : '+ str(No_of_host))
