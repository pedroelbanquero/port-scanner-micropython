### MICROPYTHON PORTSCAN V.NOS , A.CANTO
import socket as socket


def getIpRange(start,end):
    x = []
    ip_range = ipRange(start, end)
    for ip in ip_range:
        x.append(ip)

    return x


def portscan(iprange, portlist):
    rang = split("-")
    for y in getIpRange(rang[0],rang[1]):
        for x in portlist:
            addr = socket.getaddrinfo(y, x)[0][-1]
            s = socket.socket()
            s.settimeout(3.0)

            try:
                s.connect(addr)
                s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % ("/", iprange), 'utf8'))
                data = s.recv(800)
                if data:
                    print(str(data, 'utf8'), end='')
            except:
                pass
            s.close()

    return 0

