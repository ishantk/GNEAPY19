import matplotlib.pyplot as plt

"""
A = [1, 2, 3, 4, 5]
B = [10, 20, 30, 40, 50]

plt.bar(A, B)
plt.show()
"""

scores = {"virat":90, "rohit":140, "dhoni":70, "pandya":50}

"""
plt.bar(0, scores["virat"])
plt.bar(1, scores["rohit"])
plt.bar(2, scores["dhoni"])
plt.bar(3, scores["pandya"])

plt.show()
"""

for i, key in enumerate(scores):
    # print(i, key)
    # plt.bar(i, scores[key])
    plt.bar(key, scores[key])

plt.xlabel("Batsmen")
plt.ylabel("Score")

plt.title("Indian Cricket Bating")

plt.show()