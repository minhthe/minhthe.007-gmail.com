class BrowserHistory:

    def __init__(self, homepage: str):
        self.his = [homepage]
        self.len = 1
        self.curr = 0
        return None

    def visit(self, url: str) -> None:
        if url != self.his[self.curr]:
            tmp = self.his[:self.curr+1]
            self.his = tmp + [url]
            self.curr +=1
            self.len = self.curr + 1
        return None

    def back(self, steps: int) -> str:
        if self.curr - steps <= 0:
            self.curr = 0
            return self.his[0]
        
        else:
            tmp = self.curr - steps
            self.curr = tmp
            return self.his[self.curr]
        
    def forward(self, steps: int) -> str:
        if self.curr + steps >= self.len:
            self.curr = self.len - 1
            return self.his[-1]
        else:
            self.curr = self.curr + steps
            
            return self.his[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)