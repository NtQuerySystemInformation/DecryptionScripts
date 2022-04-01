import string

not_cracked_hash = [0x38EA0C1B,0x58E479EC,0xF5A79701,0x9F5473B,0xBA635AC6,0xBB18A65,0xFB7BF6AF,0x3F75D54B,0x5D112314,0x9D9F8189,0x67D8B725]
  
  
dictab = string.ascii_lowercase + string.digits
  
def strgen(l):
    if l == 1 :
        for i in dictab:
            yield i
    else:    
        for j in strgen( l - 1 ):
            for i in dictab:
                yield i + j
                
                
def CrackHashing():
    solution = {}
    for i in range(1, 10, 1):
        for s in strgen(i):
            for hashes in not_cracked_hash:
                hash = hashing(s)
                print("Trying: " + s)
                if hash == hashes:
                    print("Possible key: " + str(s) + " for hash: " + hex(final))
                    solution[hashes] = s
                    continue
    return solution            
                
                

def _rol(val, bits, bit_size):
    return (val << bits % bit_size) & (2 ** bit_size - 1) | \
           ((val & (2 ** bit_size - 1)) >> (bit_size - (bits % bit_size)))

__ROL4__ = lambda val, bits: _rol(val, bits, 32)


def hashing(input_text):
    _hash = 0xBADC0FFE
    for c in input_text:
        c = c.lower()
        _hash = ord(c) ^ __ROL4__(_hash, 5)
    return _hash    
    
    
def match_hash(hashed_key):
    bExists = False
    for hash in not_cracked_hash:
        if hashed_key ==  hash:
            bExists = True
    return bExists

def TestInput():
    while(1):
        string = input("insert Hash value:")
        if string == '':
            break
        length = 7
        hashed_key = hashing(string) 
        print("The hashed value is: " + hex(hashed_key))
        
        if match_hash(hashed_key) == True:
            print("Value matches a hash: True\n")
        else:
            print("Value matches a hash: False\n")    

def main():
    TestInput()

if __name__ == '__main__':
    main()