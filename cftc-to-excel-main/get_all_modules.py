import os

imports = []

path = "."
files = (file for file in os.listdir(path) 
         if os.path.isfile(os.path.join(path, file)))

for f in files:
    try: 
        print(f)
        with open(f,  "r") as r:
            i = r.readlines()
            for l in i:
                if "import" in l:
                    if l.strip not in imports:
                        imports.append(l.strip())
    except Exception as e: print(e);print(f)

print("printing imports")
for i in imports:
    print(i)
