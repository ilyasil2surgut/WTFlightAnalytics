def Parsefile(filename: str)-> list:
    Lines=[]
    with open(filename,'r') as File:
        for line in File:
            Lines.append(line.split(",")[:-1])
    return Lines
def FilterOnly(names:list,parsedfile:list)->list:
    tokeep=[]
    for i,data in enumerate(parsedfile[0]):
        for name in names:
            if(name==data):tokeep.append(i)
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
    def pairs(self):
        return [(self.fields[i],self.data[i]) for i in range(len(self.data))]
    def __str__(self):
        return str(self.pairs())
class Data:
    datapoints=[]
    def __init__(self,filename:str):
        self.rawdata=Parsefile(filename)
        self.data=self.rawdata[1:]
        self.fieldnames=self.rawdata[0]
    def GenerateDataPoints(self):
        self.datapoints=[]
        for line in self.data:
            self.datapoints.append(Datapoint(self.fieldnames,line))
    def FilterNames(self,names:list):
        self.rawdata=FilterOnly(names,self.rawdata)
        self.data = self.rawdata[1:]
        self.fieldnames = self.rawdata[0]
