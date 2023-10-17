def convert_mac_to_link_local_addr(mac):
    link_local_addr = ''
    mac = mac.replace('.', '')
    mac = mac.replace(':', '')
    first_byte_xor_2 = format(int(mac[0:2], 16)^2, '02x')   ### XOR 1st byte of mac with 2
    mac = mac.replace(mac[0:2], first_byte_xor_2, 1)        ### Replace 1st byte of MAC with XOR value
    link_local_mac = mac[0:6] + 'fffe' + mac[6:12]          ### add 'fffe' inmiddle of MAC
    for i in range(0,len(link_local_mac),4):
        if i >= 11:                                         ### condition i >= 11 is to avoid to append ':' at end of string
            link_local_addr += link_local_mac[i:i+4] 
        else: 
            link_local_addr += link_local_mac[i:i+4] + ':'
    link_local_addr = 'fe80::' + link_local_addr            ### Prepend 'fe80' in converted ipv6 adderess
    return link_local_addr
