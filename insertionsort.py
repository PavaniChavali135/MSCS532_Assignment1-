example = [4,3,6,2,7,2,1]

for i in range(1,len(example)):
    curr = example[i]
    prev =i-1
    while prev>=0 and example[prev]<curr:
        example[prev+1] = example[prev]
        prev = prev-1   
    example[prev+1] = curr
print(example)


    
        
        
        
        

