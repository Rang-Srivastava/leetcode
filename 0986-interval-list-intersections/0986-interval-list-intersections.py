class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        n=len(firstList)
        m=len(secondList)
        res=[]
        while i<n and j<m:
            start1=firstList[i][0]
            end1=firstList[i][1]
            start2=secondList[j][0]
            end2=secondList[j][1]
            if start1<start2:
                if end1 >=start2:
                    s=max(start1,start2)
                    e=min(end1,end2)
                    res.append([s,e])
                    if end1<=end2:
                        i+=1
                        
                    else: 
                       j+=1
                else:

                    i+=1
            elif start1==start2:
                if end1<end2:
                    res.append([start1, end1])
                    i+=1
                elif end1==end2:
                    res.append([start1, end1])
                    i+=1
                    
                else:
                    res.append([start2, end2])
                    j+=1
            else:
                    if end2 >= start1:
                        s=max(start1,start2)
                        e=min(end1,end2)
                        res.append([s,e])
                        if end1<=end2:
                          i+=1
                        
                        else:
                         j+=1
                    else:
                        j+=1
        
        return res
        