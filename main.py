import minizinc
import pymzn

# build .dzn file then use it in the model
dosen = {'john', 'budi', 'joni', 'rani', 'dono'}
matkul = {'web','spk','bio','web2','algo'}
hari = {'senin', 'selasa', 'rabu', 'kamis', 'jumat'}
dosen_matkul = [
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 1, 1]
]

dosen_hari = [
        [1, 1, 1, 0, 0],
        [1, 0, 1, 0, 1], 
        [1, 0, 0, 1, 0], 
        [1, 1, 1, 1, 1], 
        [1, 0, 0, 1, 0], 
]

data = {
    'dosen': dosen,
    'matkul': matkul,
    'hari': hari,
    'dosen_matkul': dosen_matkul,
    'dosen_hari': dosen_hari,
}

pymzn.dict2dzn(data, fout = 'data_source.dzn')


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