'''
https://leetcode.com/problems/design-underground-system
'''
class UndergroundSystem:

    def __init__(self):
        self.a = {}
        self.b = {}
        return None

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.a:
            
            self.a[stationName] = {}
        self.a[stationName][id]  = t
        return None
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        if stationName not in self.b:
            self.b[stationName] = {}
        self.b[stationName][id] =t
        return None

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        cnt = 0 
        rst = 0
        for key in self.a[startStation]:
            if(key in self.b[endStation].keys()):
                cnt += 1 
                rst += abs(self.a[startStation][key] - self.b[endStation][key])
        return rst/cnt

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)