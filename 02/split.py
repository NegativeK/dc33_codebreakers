#!/usr/bin/env python3
import sys

inputs = []
filter = "abcdefghijklmnopqrstuvwxyz"
filter += "abcdefghijklmnopqrstuvwxyz".upper()
filter += "!\"#%&'()*+,./:;<=>?@[\\]^_`{|"
filter += "^-}~©$0123456789"

for line in sys.stdin:
    chars = list(line)

    inputs += chars

filtered = (i for i in inputs if i not in filter)

output = filtered
# output = str(list(filtered))
# output = "\n".join(output)
output = "".join(output)
output = output.strip()
print(output)
