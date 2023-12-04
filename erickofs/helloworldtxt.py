# Open hello.txt file with explicit encoding and strip lines
with open("hello.txt", "r+", encoding="utf-8") as file: lines = [line.strip() for line in file.readlines()]
# print only lines that are not empty or commented
print("\n".join([line for line in lines if line != "" and not line.startswith("#")]))
