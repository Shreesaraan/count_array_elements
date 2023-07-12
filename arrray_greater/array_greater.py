array=list(map(int,input("Enter array elements: ").split()))
max_element=float('-inf')
max_element_count=0
for i in range(len(array)):
    if array[i]>max_element:
        max_element=array[i]
for i in range(len(array)):
    if array[i]==max_element:
        max_element_count+=1
print("Count of elements having atleast one element greater than itself is: ",len(array)-max_element_count)