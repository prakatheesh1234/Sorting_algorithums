def insertion_sort(s):
    
    for i in range(1,len(s)):
        j=i-1
        while s[j]>s[j-1] and j>=0:
            s[j],s[j+1]=s[j+1],s[j]
            j=j-1
        
            
                
                
    return s
    
        
a=[90,1,0,34,54]
print(insertion_sort(a))






