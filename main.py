
from flask import Flask
from flask import render_template
import minizinc
import pymzn

app = Flask(__name__)


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

dataDict = {}
for key, value in thisDict.items():
    for index, val in enumerate(value) :
        if index in dataDict:
            arr = dataDict[index]
            arr.append(val)
            dataDict[index] = arr
        else:
            dataDict[index] = [val]

print(dataDict)

@app.route("/")
def index():
    return render_template('index.html', data=thisDict, dataDict=dataDict)