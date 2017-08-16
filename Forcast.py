class Forcast:
    def __init__(self,Forcast_mode):
        self.mode = Forcast_mode
        self.weekly_forcast= {'Mon':56,'Tue':76,'Wed':69,'Thu':98,'Fri':90, 'Sat':82, 'Sun':71}
    def __F2C__(self,n):
        return 5/9.0*(n-32)

    def __F2K__(self,n):
        return 5.0/9*(n-32)+273.15

    def setMode(self, new_mode):
        if new_mode == "C" or new_mode == "F" or new_mode == "K" :
            self.mode = new_mode
    def getMonTemp(self):
        r= self.weekly_forcast['Mon']
        if self.mode == 'C':
            return self.__F2C__(r)
        elif self.mode=='K' :
            return self.__F2K__ (r)
        else:
            return (r)
    def getTueTemp(self):
        r= self.weekly_forcast['Tue']
        if self.mode == 'C':
            return self.__F2C__(r)
        elif self.mode=='K' :
            return self.__F2K__ (r)
        else:
            return (r)
    def getWedTemp(self):
        r= self.weekly_forcast['Wed']
        if self.mode == 'C':
            return self.__F2C__(r)
        elif self.mode=='K' :
            return self.__F2K__ (r)
        else:
            return (r)
    def getThuTemp(self):
        r= self.weekly_forcast['Thu']
        if self.mode == 'C':
            return self.__F2C__(r)
        elif self.mode=='K' :
            return self.__F2K__ (r)
        else:
            return (r)
    def getFriTemp(self):
        r= self.weekly_forcast['Fri']
        if self.mode == 'C':
            return self.__F2C__(r)
        elif self.mode=='K' :
            return self.__F2K__ (r)
        else:
            return (r)
    def getSatTemp(self):
        r= self.weekly_forcast['Sat']
        if self.mode == 'C':
            return self.__F2C__(r)
        elif self.mode=='K' :
            return self.__F2K__ (r)
        else:
            return (r)
    def getSunTemp(self):
        r= self.weekly_forcast['Sun']
        if self.mode == 'C':
            return self.__F2C__(r)
        elif self.mode=='K' :
            return self.__F2K__ (r)
        else:
            return (r)

F1 = Forcast("C")

def weekforcast (fc):
    abb = "Sun:" + str(round(fc.getSunTemp(),2))
    abb = abb + ";Mon:" + str(round(fc.getMonTemp(),2))
    abb = abb + ";Tue"  + str(round(fc.getTueTemp(),2))
    abb = abb + ";Wed" +  str(round(fc.getWedTemp(),2))
    abb = abb + ";Thu"  + str(round(fc.getThuTemp(),2))
    abb = abb + ";Fri" +  str(round(fc.getFriTemp(),2))
    abb = abb + ";Sat"   + str(round(fc.getSatTemp(),2))
    if fc.mode =="F":
        abb= abb+'\nfahrenheit'
    elif fc.mode== "C":
        abb= abb+'\nCelsius'
    else:
        abb=abb+'\nkelvin'
    return abb

abb = Forcast("F")
print weekforcast(abb)
