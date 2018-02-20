maxuid = 0
for line in open("/etc/passwd"):
    split = line.split(":")
    if int(split[2]) > maxuid:
          maxuid = int(split[2])

print(maxuid)



# BASH - sort -n -t: -k3 /etc/passwd | tail -1 | cut -d: -f3
