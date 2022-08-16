import pandas as pd

df = pd.read_csv("controltwo.csv")

freq = df["UserID"].value_counts().value_counts()

actualfreq = []
with open("userwordfrequency.txt","r") as file:
    for line in file.readlines():
        actualfreq = list(map(int, line[:-1].split(" ")))

for i in range(27):
    pred = freq.get(i + 1) if freq.get(i + 1) is not None else 0
    actual = actualfreq[i]
    print(str(i + 1) + " " + str(pred) + " " + str(actual) + " " + str(actual - pred))

print()

counts = df["UserID"].value_counts()
print(counts[counts == 10])
