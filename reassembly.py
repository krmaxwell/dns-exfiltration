import base64
import struct

""" Reassemble small 8 byte chunks back into original file """

file_chunks = []
the_file = "\n---\n"

def back(chunk):
    b64_payload = chunk.split(".")[0]
    payload = base64.b64decode(b64_payload)
    file_data = struct.unpack('L8s', payload)
    file_chunks.append(file_data)

# Run Program

queries = []

fp = open("/path/to/dns/query/log")
lines = fp.readlines()
fp.close()

for line in lines:
    if "file1.16s.us" in line:
        FQDN = line.split()[7]
        queries.append(FQDN.strip())

uqueries = set(queries)

for q in uqueries:
    back(q)

file_chunks.sort()

for fc in file_chunks:
    the_file += fc[1]

the_file += "\n---\n"
print the_file
