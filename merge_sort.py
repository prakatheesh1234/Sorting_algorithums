
def merge(left,right):
    
    if len(left)==0:
        return right
    if len(right)==0:
        return left
    left_index=right_index=0
    result=[]
    
    
    while len(result)<len(left)+len(right):
         if left[left_index]<=right[right_index]:
             result.append(left[left_index])
             left_index=left_index+1
         else:
             result.append(right[right_index])
             right_index=right_index+1
         if left_index==len(left):
             result=result+right[right_index:]
             break
         
         if right_index==len(right):
             result=result+left[left_index:]
             break
         
    return result        
             

def merge_sort(a):
    if len(a)<2:
        return a
    mid=len(a)//2
    
    return merge(left=merge_sort(a[:mid]),right=merge_sort(a[mid:]))

a=[3,2,1,5,6,7,8,2]
print(merge_sort(a))