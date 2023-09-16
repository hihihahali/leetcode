def romanToInt(self, str):
    self = 0
    symbols = [['I',1], ['V',5], ['X',10], ['L',50], ['C',100], ['D',500], ['M',1000]]
    i=0
    while i<len(str):
        for j in range(0, len(symbols)):
            if symbols[j][0]==str[i]:
                a = symbols[j][1]
        if i != len(str) -1 :
            for j in range(0, len(symbols)):
                if symbols[j][0]==str[i+1]:
                    b = symbols[j][1]
        else: b=0    
        if a>=b:
            self = self+a
            i=i+1
        else:
            self = self+b-a
            i= i+2
    return self   