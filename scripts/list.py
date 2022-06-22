import os

list_files = os.listdir("doc/devices/compare")

f = open("inventory/intended/structured_configs/compare.yml", "w")

f.write("comparefiles: ")
for file in list_files:
    if file != "list.html":
        f.write("\n  - " + file.replace(".html", ""))

if len(list_files) == 1:
    f.write("[]\n")
f.close()