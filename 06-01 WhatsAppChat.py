import re
fhandle = open('chat.txt')

# Initialize sender list to Empty List
senderList = []
for line in fhandle:
    line = line.replace("\xe2\x80\xaa","")
    line = line.replace("\xe2\x80\xac","")
    sender = re.findall('[0-3][0-9]/[0-1][0-9]/1[5-6], [0-9]{1,2}:[0-6][0-9] [AP]M - (.+?):',line)
    if(len(sender) > 0):
        if(sender[0] not in senderList):
            senderList.append(sender[0])
print senderList
print len(senderList)
