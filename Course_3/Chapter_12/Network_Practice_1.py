import socket

'''12.1'''
def Network_Part_one():
    mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org',80))

    return


'''12.2'''
def Network_Part_two():
    mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org',80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data)) < 1 :
            break
        print(data.decode())
    mysock.close()

    ''' #META DaTA
        HTTP/1.1 200 OK
        Date: Wed, 31 Jul 2019 22:56:58 GMT
        Server: Apache/2.4.18 (Ubuntu)
        Last-Modified: Sat, 13 May 2017 11:22:22 GMT
        ETag: "a7-54f6609245537"
        Accept-Ranges: bytes
        Content-Length: 167
        Cache-Control: max-age=0, no-cache, no-store, must-revalidate
        Pragma: no-cache
        Expires: Wed, 11 Jan 1984 05:00:00 GMT
        Connection: close
        Content-Type: text/plain
        
        #Result
        But soft what light through yonder window breaks
        It is the east and Juliet is the sun
        Arise fair sun and kill the envious moon
        Who is already s
        ick and pale with grief
        '''
    return






a = Network_Part_two()




