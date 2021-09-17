import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

for subdir, dirs, files in os.walk("./"):
    for file in files:
        filename = os.path.join(subdir, file)

        if filename.split(".")[-1].lower() != "gbot":
            continue


        with open(filename, 'r') as file :
          filedata = file.read()


        filedata = filedata.replace('"Blank"', '"Wait"')


        with open(filename, 'w') as file:
          file.write(filedata)
        print(f"Done {filename}")

 