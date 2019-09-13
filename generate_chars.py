# Generate 5000 chars (does not count \n)
with open("generate_chars.txt", "w") as fp:
    for i in range(50):
        print("{0:02d}_100CharsPerLine_{1}".format(i+1, "Globality"*9))
        fp.write("{0:02d}_100CharsPerLine_{1}\n".format(i+1, "Globality"*9))
