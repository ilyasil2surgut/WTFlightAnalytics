def Parsefile(filename:str)->list:
    Lines=[]
    with open(filename,'r') as File:
        for line in File:
            Lines.append(line.split(",")[:-1])
    return Lines
def FilterOnly(names:list,parsedfile:list)->list:
    tokeep=[]
    for i in range(len(parsedfile[0])):
        for name in names:
            if(name==parsedfile[0][i]):tokeep.append(i)
    out=[names]
    for name in names:
        for datapoint in parsedfile[1:]:
            out.append([datapoint[i] for i in range(len(datapoint)) if i in tokeep])
    return out
class Datapoint:
    def __init__(self,names:list,line:list):
        self.data=line
        self.fields=names
    def get(self,name:str)->float:
        return self.data[self.fields.index("name")]
