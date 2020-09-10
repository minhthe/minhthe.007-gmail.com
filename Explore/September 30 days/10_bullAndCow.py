class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        checking = [False for i in range(len(guess))]
        bull, cow = 0 , 0
        for i, e in enumerate(guess):
            if e == secret[i]: 
                bull += 1
                checking[i] = True
        # print('check', checking)
        
        for i, e in enumerate(guess):
            # print('guess', i ,e)
            # if checking[i]==True: continue
            if e == secret[i]: continue
            for j, ee in enumerate(secret):
                # print('--secret', j,ee)
                if i!=j and e== ee and checking[j]==False:
                    cow += 1
                    checking[j]= True
                    # print('fuck',checking)
                    break
        return "{}A{}B".format(bull,cow)