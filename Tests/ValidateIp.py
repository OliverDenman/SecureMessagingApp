IpAddress = input("Ip: ")

def IpCheck(IpAddress):
    IpSplit = IpAddress.split(".")
    if len(IpSplit) != 4:
        return "Invlaid IP"
    for i in IpSplit:
        print (i)
        if int(i) in range(0,255):
            next
        else:
            return "Invalid IP"
    return "Valid Ip"





print(IpCheck(IpAddress))
