## DNS Client
## Based on "Computer Networking A Top Down Approach 6th Edition"

from socket import *

serverName = '193.136.224.100' ## Address of ualg.com
serverPort = 53
clientSocket = socket(AF_INET, SOCK_DGRAM)

query = bytearray(); ## Byte = 8 bits = 00000000

### HEADER
## ID 16 bits   #Array index
query.append(3) #0 -> 00000011
query.append(4) #1 -> 00000100

## Flags 16 bits
query.append(0) #2 -> 00000000
query.append(0) #3 -> 00000000

## Number of queries
query.append(0)  #4 -> 00000000
query.append(1)  #5 -> 00000001

## Number of answers
query.append(0)  #6 -> 00000000
query.append(0)  #7 -> 00000000

## Number of authority RRs
query.append(0)  #8 -> 00000000
query.append(0)  #9 -> 00000000

## Number of addicional RRs
query.append(0)  #10 -> 00000000
query.append(0)  #11 -> 00000000

## Question for www.ualg.pt
## Numbers identify the number of characters that follow
query.append(3)     #12 -> 00000011
query.append('w')   #13
query.append('w')   #14
query.append('w')   #15
query.append(4)     #16 -> 00000100
query.append('u')   #17
query.append('a')   #18
query.append('l')   #19
query.append('g')   #20
query.append(2)     #21 -> 00000010
query.append('p')   #22
query.append('t')   #23
query.append(0)     #24 -> 00000000

## Type A
query.append(0)     #25 -> 00000000
query.append(1)     #26 -> 00000001

## Class = IN
query.append(0)     #27 -> 00000000
query.append(1)     #28 -> 00000001

clientSocket.sendto(query,(serverName, serverPort))

clientSocket.close()
