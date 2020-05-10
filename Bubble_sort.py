def bubble_sort(a):
    
    n=len(a)
    for i in range(n):
        ar=True
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
            ar=False
        if ar:
            break
    return a          
    
        
    
a=[23,43,0,1,356,90]    
    
print(bubble_sort(a))


#0(n)2
#average case o(n)