def missing_number(num_list):
    missed = []
    for i, j in enumerate(num_list):
        if i!= len(num_list)-1 and num_list[i+1] != num_list[i]+1:
            missed.append(num_list[i]+1)
    return missed

print([1, 2, 4, 6, 7, 9, 10],' and the missed values are :',missing_number([1, 2, 4, 6, 7, 9, 10])) 
print([10,11,12,14,15,16,17],' and the missed values are :',missing_number([10,11,12,14,15,16,17]))  
print([20,22,24,26],' and the missed values are :',missing_number([20,22,24,26]))  