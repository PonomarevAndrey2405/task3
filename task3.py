
filenames = ["2.txt", "1.txt"]
with open("newfile.txt", "w") as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(f'File: {fname[0]}\n')
                outfile.write(line + "\n")
