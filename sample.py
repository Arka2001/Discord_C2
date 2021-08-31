#!/usr/bin/python3

import os
import subprocess

cmd = input("Enter a command: ")

proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

result = proc.stdout.read() + proc.stderr.read()	# stdout and stderr
result = result.decode('utf-8')				# decoding result to utf-8

print(result)
