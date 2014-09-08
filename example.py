#!/usr/bin/env python
import re
from socks5socket import *
s = Socks5Socket('ipip.kr', 80, 'localhost', 9150)
s.send("GET / HTTP/1.1\r\nHost: ipip.kr\r\n\r\n")
print re.search("<title>(.*?)</title>", s.recv(400)).group(1)
