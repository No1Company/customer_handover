import os

rootdir = os.getcwd()

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if any([s in file for s in [".en-us.lg", ".sv.lg"]]):
            path = os.path.join(subdir, file)

            values = []
            with open(path, "rt") as fr:
               
                for line in fr:
                    if '"data":' in line:
                        value = line.replace('"data": ', '')
                        value = value.replace("  ", "")
                        value = value.replace("\n", "")
                        value = value.replace(",", "")
                        if "{" not in value:
                            values.append(value)
                fr.close()

            text = ""
            with open(path, "rt") as fr:
                text = fr.read()
                
                for value in values:
                    
                    print(value in text)    
                    text = text.replace(value, '{\n"msteams": {\n"type": "imBack",\n"value": '+value+'\n}\n}')
                fr.close()
                
            with open(path, "wt") as fw:
                fw.write(text)
                fw.close()
print("end")