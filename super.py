import matplotlib.pyplot as plt



# bar plot
superheroes=["Spiderman","Iron Man","Hulk"]
ratings=[87,96,67]
plt.bar(superheroes,ratings)
plt.title("Ratings of Three Superheroes")
plt.xlabel("Superheroes")
plt.ylabel("My Ratings of the Three Superheroes")
plt.show()

