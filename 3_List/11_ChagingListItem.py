# To change the item value specify the index number
list3 = ["car", "bike", "lorry"]
list3[1] = "bus"
print (list3)

"""
To change the value of items within a specific range, 
specify the range of index numbers where you want to insert the new values
"""
list4 = ["car", "bike", "lorry", "train", "truck"]
list4[1:3] = ["cycle", "bus"]
print (list4)

"""
If you insert more items than you replace, 
the new items will be inserted where you specified, 
and the remaining items will move accordingly
"""
list5 = ["car", "bike",  "train"]
list5[1:2] = ["cycle", "bus"]
print (list5)