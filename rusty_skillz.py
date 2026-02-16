import struct
#this Bytes were extracted from the hex_view
encrypted_data=[0xAC, 0xBF, 0xD8, 0xA9, 0xF4, 0xE6,
    0xE6, 0x96, 0x88, 0x11, 0x3C, 0x8A, 0x12, 0x4C,
    0xEB, 0x02, 0x1A, 0x13, 0xCB, 0x23, 0x9B, 0x76,
    0xE5, 0x52, 0x37, 0xDD, 0xF6, 0x33, 0x5B, 0x35,
    0x91, 0xFD, 0x88, 0x55, 0x76, 0x79]
#this is the length
seed_arg=36
#the xor is extracted from the pseudo_code
state=seed_arg ^ 0xA5A5A5A5


flag=""
#this loop will iterate through each byte to decrypt the flag 
for i in encrypted_data:
    #this is the core logic of the encryption and we added & 0xFFFFFFFF to make sure it is a 32-bit integer and to prevent overflow
    state=(1103515245 * state + 12345) & 0xFFFFFFFF
    #the pseudo_code showed that its using the hibyte with will start at 24th bit so we shifted the bits 
    key_byte=(state>>24) & 0xFF
    #this will give us the final character will which will be added to the flag
    decrypted_character=i ^ key_byte

    flag+=chr(decrypted_character)




print(f"Flag:  {flag}")
