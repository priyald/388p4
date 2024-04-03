#!/usr/bin/env python3

import sys

payload = b'Priyal' + b'\x00'*4 +b'A+'
sys.stdout.buffer.write(payload)
