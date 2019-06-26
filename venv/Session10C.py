import matplotlib.pyplot as plt

jobs = [120, 80, 90]
domains = ["Java", "Python", "C++"]

plt.pie(jobs, labels=domains)
plt.legend()
plt.show()