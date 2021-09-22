class HashTable:
    def __init__(self):
        self.capacity = 7
        self.vals = [None] * self.capacity
        self.keys = [None] * self.capacity


    def Put(self, k, v):
        ind = self.__hash(k)
        overwritted_vals = []
        forKey = []
        if self.keys[ind] == None:
            self.keys[ind] = k
            self.vals[ind] = v

        elif self.keys[ind] == k:
            if self.vals[ind] != None:
                overwritted_vals.append(self.vals[ind])
                self.vals[ind] = v
                return "overwritted value",overwritted_vals[0]
        else:
            forKey.append(self.vals[ind])
            self.vals[ind] = v
            if self.keys[ind] != k:
                self.keys[ind] = k
            return f"overwritted  Value {forKey[0]}"



    def Get(self, k):
        if k in self.keys:
            keys = self.__hash(k)
            GetValue = self.vals[keys]
            if keys != None:
                return GetValue
            else:
                return None


    def __hash(self, key):
        return  key % self.capacity

    def Keys(self):
        tot_keys=[]
        for i in self.keys:
            if i!= None:
                tot_keys.append(i)
        return tot_keys

    def Values(self):
        tot_values=[]
        for i in self.vals:
            if i!= None:
                tot_values.append(i)
        return  tot_values

    def Entries(self):
        a=self.Keys()
        b=self.Values()
        entries=list(zip(a,b))
        return entries

    def Remove(self, k):
        removed_Value = []
        if k in self.Keys():
            ind = self.__hash(k)
            if self.keys[ind] != None:
                self.keys[ind] = None
                removed_Value.append(self.vals[ind])
                self.vals[ind] = None
                return removed_Value[0]

        else:
            return "Not Present"

    def Size(self):
        return len(self.Values())

    def IsEmpty(self):
        if len(self.Values())== None:
            return True
        else:
            return False

    def ReSize(self):
        if len(self.Values())==self.capacity:

            self.capacity=self.capacity*2

            for i in range(self.capacity):

                self.vals.append(None)

                self.keys.append(None)





class FrequencyTable:
    # constructor
    def __init__(self):
        self.hashtable = HashTable()	
        self.c=0


    def Add(self, e):
        if None in self.hashtable.vals:

            if (self.hashtable.vals[self.c] != None):

                self.c += 1

                self.hashtable.Put(self.c, e)

            if (self.hashtable.vals[self.c] == None):

                self.hashtable.Put(self.c, e)

                self.c = 1


        else:
            self.hashtable.ReSize()

            self.c += 1

            self.hashtable.Put(self.c, e)

        return self.c


    def Remove(self, e):
        if e in self.hashtable.vals:
            find=self.hashtable.vals.index(e)
            self.hashtable.vals[find] = None
            self.c-=1
        return self.c


    def Count(self):
        lst=[]
        for i in self.hashtable.Values():
            if i not in lst:
                lst.append(i)
        return len(lst)


    def Frequency(self):

            lst=[]
            freq = {}
            for item in self.hashtable.Values():
                if (item in freq):
                    freq[item] += 1
                else:
                    freq[item] = 1

            for key, value in freq.items():
                tup=(key, value)
                lst.append(tup)
            return lst


class FrequencyUtility:

    def __init__(self, entrancefile, exitfile):
        self.entrance = entrancefile
        self.exit = exitfile
        # table to store data
        self.freqTable = FrequencyTable()


    def Process(self):
        self.__ProcessEntrance()
        self.__ProcessExit()
        return self.freqTable.Frequency()


    def __ProcessEntrance(self):
        f = open(self.entrance, "r")
        allLines = f.read().split('\n')
        f.close()

        for aLine in allLines:
            if len(aLine) > 0:
                self.freqTable.Add(int(aLine))


    def __ProcessExit(self):
        f = open(self.exit, "r")
        allLines = f.read().split('\n')
        f.close()

        for aLine in allLines:
            if len(aLine) > 0:
                self.freqTable.Remove(int(aLine))


def Test():
    d = FrequencyUtility("entrance.txt", "exit.txt")
    print(d.Process())

Test()