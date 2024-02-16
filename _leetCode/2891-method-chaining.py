#Method Chaining
#https://leetcode.com/problems/method-chaining/description/
import pandas

caseData = {
    "name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Tommy"],
    "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
    "age": [98, 50, 6, 45, 100, 26],
    "weight": [464, 41, 328, 463, 50, 349]
}

caseDataFrame = pandas.DataFrame(caseData)

if True:
    def findHeavyAnimals(animals):
        animals = animals[["name", "weight"]]
        heavy_animals = animals[animals["weight"] > 100]
        heavy_animals = heavy_animals.sort_values(by="weight", ascending=False)[["name"]]

        return heavy_animals
    
print(f"{findHeavyAnimals(caseDataFrame).to_markdown(index=False)}")