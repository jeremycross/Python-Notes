#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt: break
    if count == 3: continue
    pw = input(f"{count}: What's the secret word? ")
else:
    auth = True

# an else outside of a loop means that it will excecute if the loop ended without a break

print("Authorized" if auth else "Not authorized ...")