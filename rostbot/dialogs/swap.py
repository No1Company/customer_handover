import os

rootdir = os.getcwd()

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if any([s in file for s in [".en-us.lg", ".sv.lg"]]):
            path = os.path.join(subdir, file)

            with open(path, "r+") as f:
                for line in f:
                    if '"data":' in line:
                        value = line.replace('"data": ', '')
                        value = value.replace("  ", "")
                        value = value.replace("\n", "")
                        print("'" + value + "'")


print("end")