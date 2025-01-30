import matplotlib.pyplot as plt

days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
sales=[160,130,135,120,170,180,145]

plt.plot(days,sales,marker="o")
plt.title("Sales over Days")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()

