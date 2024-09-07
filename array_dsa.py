import array
array1=array.array('i',[1,2,3,4,5,])
array1.append(90)
array1.insert(2,22)
def value_find(array,index):
     for i in   range (len(array1),):
        if index==array[i]:
            return i
        

     return -1
print(array1.pop())       
print(value_find(array1,90))        
        
    

    