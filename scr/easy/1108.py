def defangIPaddr(address=str):
    address = address.replace('.','[.]')
    return address

address = defangIPaddr("1.1.1.1")
print(address)
