#!/usr/bin/env python3

import bcrypt

passwd = b's$cret12'

salt = b'cgjjhjh'
print(salt)
hashed = bcrypt.hashpw(passwd, salt)
print(salt)
print(hashed)
