try:
    with open("file.bin", "rb") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File not found")