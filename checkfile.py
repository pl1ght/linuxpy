import os.path

#if os.path.exists("/etc/hosts"):
#    print("hosts file exists")
#else:
#    print("no hosts file")

try:
    f = open("/etc/hosts")
    # go ahead and read the file
except FileNotFoundError:
    print("no hosts file")

