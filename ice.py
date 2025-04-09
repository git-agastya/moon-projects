import matplotlib.pyplot as plt

#bar Plot
icecream=["Caramel","Vanilla","Mint"]
rating=[9,8,4]
plt.bar(icecream,rating)
plt.title("My Ratings of Three Icecream Flavors")
plt.xlabel(icecream)
plt.ylabel("My Ratings of the Three Icecream Flavors")
plt.show()