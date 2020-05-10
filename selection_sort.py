def insertion_sort(s):
    
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            if s[i]>s[j]:
                s[i],s[j]=s[j],s[i]
                
                
    return s
    
    
        
a=[90,1,0,34,54]
print(insertion_sort(a)






