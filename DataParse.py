def Parsefile(filename: str)-> list:
    Lines=[]
    with open(filename,'r') as File:
        for line in File:
            if len(line)>1:Lines.append(line.split(",")[:-1])
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
        self.data=[float(x) for x in line]
        self.fields=[x.split("/",maxsplit=1)[0] for x in names]
        self.units=[x.split("/",maxsplit=1)[1] for x in names]
    def get(self,name:str)->float:
        return float(self.data[self.fields.index(name)])
    def set(self,name:str,value:float):
        self.data[self.fields.index(name)]=value
    def out(self)->list:
        return [(self.fields[i],self.data[i],self.units[i]) for i in range(len(self.data))]
    def __str__(self)->str:
        return str(["{}:{} {}".format(x[0],x[1],x[2]) for x in self.out()])
    def Selection(self,firststr:str,secondstr:str)->tuple:
        return (self.get(firststr),self.get(secondstr))
class Data:
    datapoints=[]
    def __init__(self,filename:str):
        self.rawdata=Parsefile(filename)
        self.data=self.rawdata[1:]
        self.fieldnames=self.rawdata[0]
        self.name="Someplane"
    def GenerateDataPoints(self):
        self.datapoints=[]
        for line in self.data:
            self.datapoints.append(Datapoint(self.fieldnames,line))
    def FilterNames(self,names:list):
        self.rawdata=FilterOnly(names,self.rawdata)
        self.data = self.rawdata[1:]
        self.fieldnames = self.rawdata[0]
    def NormalizeTime(self):
        starttime=self.datapoints[0].get("Time")
        for point in self.datapoints:
            point.set("Time",round(point.get("Time")-starttime,2))
    def FilterPoints(self,F):
        newpoints=[]
        for i,point in enumerate(self.datapoints):
            if F(point):newpoints.append(point)
        self.datapoints=newpoints
        self.NormalizeTime()
    def setname(self,string:str):
        self.name=string
    def FixFalseAlt(self,truevalue,falsevalue):
        for i, point in enumerate(self.datapoints):
            if point.get("Altitude") != falsevalue:
                break
            else:
                point.set("Altitude", truevalue)
    def plotClimbrate(self):
        import matplotlib.pyplot as plt
        plt.figure(figsize=(15, 9))
        plt.ylim(10, 35)
        plt.xlim(250,6000)
        plt.plot([x.get("Altitude") for x in self.datapoints], [x.get("Vario") for x in self.datapoints])
        plt.savefig(self.name+" Climb rate.png", bbox_inches="tight")
    def plotPowertoAlt(self):
        import matplotlib.pyplot as plt
        plt.figure(figsize=(15, 9))
        plt.ylim(100, max([x.get("Power") for x in self.datapoints]))
        plt.xlim(250,6000)
        plt.plot([x.get("Altitude") for x in self.datapoints], [x.get("Power") for x in self.datapoints])
        plt.savefig(self.name+" Power diagram.png", bbox_inches="tight")