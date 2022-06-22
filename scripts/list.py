import os

list_files = os.listdir("doc/devices/compare")

f = open("inventory/intended/structured_configs/compare.yml", "w")

f.write("compare_files:\n")
for file in list_files:
    f.write("\t- " + file +"\n")

f.close()