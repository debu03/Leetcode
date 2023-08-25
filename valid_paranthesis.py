class Solution:
    def isValid(self, s: str) -> bool:
        list=[]
        for i in s:
            if(i=="(" or i=="[" or i=="{"): 
                #if opening brackets then add to list
                list.append(i)
            else:
                if not list: 
                    #if not opening then false
                    return False
                ele=list.pop() 
                #pops last item and stores it into ele
                if i=="}": 
                    #chceks if all opening have its closing 
                    if(ele!="{"):
                        return False
                elif(i=="]"):
                    if(ele!="["):
                        return False
                else:
                    if(ele!="("):
                        return False
        if list:
            #if some ele still left means unused
            return False
        return True