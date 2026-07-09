from model import get_model
from sklearn.metrics.pairwise import cosine_similarity

model = get_model("all-MiniLM-L6-v2")
dog = model.encode("dog")
puppy = model.encode("puppy")
truck = model.encode("truck")

print("Dog-Puppy:",
    cosine_similarity([dog], [puppy])[0][0])

print("Dog-Truck:",
    cosine_similarity([dog], [truck])[0][0])

print(f"Number of dimensions of Dog:{len(dog)}")
print(f"Dimension of Dog: {dog}")
print(f"Number of dimensions of Truck:{len(truck)}")
print(f"Dimension of Truck: {truck}")

string = model.encode("Hello! I am Sarthak.")
print(len(string))
