



def heapify(a,lenn,i):
     largest=i
     l=2*i+1
     r=2*i+2
     
     if l<lenn and a[l]>a[i]:
        largest=l
     if r<lenn and a[largest]<a[r]:
        largest=r
    
     if largest!=i:
       a[largest],a[i]=a[i],a[largest]
       heapify(a,lenn,largest)








def heap_sort(a):
    length=len(a)
    for i in range(length-1,-1,-1):
        print(a)
        heapify(a,length,i)
#    print(a)
    for i in range(len(a)-1,0,-1):
        a[i],a[0]=a[0],a[i]
        heapify(a,i,0)
#    print(a)







a=[23,1,43,12,67,]
heap_sort(a)

print(a)




