class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:\


    # 1.iterate and sort every word.sorting string gives u result in []
    #2. turn that [] inot string again and put that into d 
    #3. if the next strings stored string alreasy exists in d, append it to d[sorted_string] else, create another group 
    #4. after loop ends, iterate through dic and store them into new list 


        d={}
        
        for i in strs:
            sorted_string="".join(sorted(i))
            if sorted_string in d:
                d[sorted_string].append(i)

            else:
                d[sorted_string]=[i]

            sorted_string=''

        print(d)

        final=[]

        for i in d:
            final.append(d[i])

        return final

            


        print(d)

      


        
     
           
        
        
        