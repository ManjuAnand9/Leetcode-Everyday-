class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #1. iterate through two stings, store in dics
        #2. if d1==d2: its anagram else its not


        d1= {}
        d2={}

        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1

        for i in t:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]= 1

        
        #compare dictionaries

        if d1==d2:
            return True 
        else:
            return False
    

     

            
        

        