import matplotlib.pyplot as plt

fruits=["apple","orange","grapes","mango"]
quantity=[10,15,20,25,]

plt.bar(fruits,quantity)
plt.title("Fruits vs Quantity")
plt.xlabel("Fruits",fontsize=14,color='red')
plt.ylabel("Quantity",fontsize=14,color='orange')
plt.show()