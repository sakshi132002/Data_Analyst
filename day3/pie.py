import matplotlib.pyplot as plt

subjects=["DSA","Web development","SAD","AI"]
marks=[90,80,45,50]
plt.pie(marks, labels=subjects, startangle=90)
plt.title("marks in different subjects")
plt.show()