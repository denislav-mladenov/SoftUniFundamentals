class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, spicies, name):
        if spicies == "mammal":
            self.mammals.append(name)
        elif spicies == "fish":
            self.fishes.append(name)
        elif spicies == "bird":
            self.birds.append(name)
        Zoo._Zoo__animals += 1

    def get_info(self, spicies):
        info = ""
        if spicies == "mammal":
            info = f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif spicies == "fish":
            info = f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif spicies == "bird":
            info = f"Birds in {self.name}: {', '.join(self.birds)}"
        return f"{info}\nTotal animals: {Zoo._Zoo__animals}"

name = input()
rows = int(input())

zoo = Zoo(name)

for _ in range(rows):
    spicies, name = input().split()
    zoo.add_animal(spicies, name)

spicies = input()
print(zoo.get_info(spicies))
