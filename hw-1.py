myfile = "hw.txt"

with open(myfile) as f:
    result = f.read().split()

long_words = []
for i in result:
    if len(i) >= 7:
        long_words.append(i)
print(long_words)

with open("hw2.txt", "w") as f2:
    for word in long_words:
        f2.write(word + "\n")

#2
with open(myfile) as f:
    result = f.read().split()

print(f"Words: {len(result)}")

#3
with open(myfile) as f:
    result = f.read().split()

banned = ["or", "to", "die"]

for i in range(len(result)):
    if result[i] in banned:
        result[i] = "***"
result = " ".join(result)
print(result)


