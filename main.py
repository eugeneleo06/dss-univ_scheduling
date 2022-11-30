import minizinc

# build .dzn file then use it in the model
# ................

# run the model with the expected .dzn file
model = minizinc.Model("Model.mzn")
gecode = minizinc.Solver.lookup("gecode")
instance = minizinc.Instance(gecode, model)
result = instance.solve()

# manipulate output
stringed = "{}".format(result)

arr = stringed.splitlines()

finalArr = []

for x in arr:
    if len(x)> 0 and x[0] == '1':
        finalArr.append(x)

thisDict = {
    "senin": [],
    "selasa": [],
    "rabu": [],
    "kamis": [],
    "jumat": []
}

for x in finalArr:
    if isinstance(x, str):
        y = x.split(" ")
        thisDict[y[3]].append(y[1] + " " + y[2])

for key, value in thisDict.items():
    val = ' | '.join(value)
    print(f'{key.capitalize(): <10}{val.title()}')