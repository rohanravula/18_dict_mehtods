# book={
# 1: "python programming", #if in dictinary there are multiple key value pair then (,) comma should be must.
# 2: "core python programming",  #before colon it is called "key" & after collon it is called "pair". 
# 3: "advance python programming", #that's why dictionary is called as key value pair.
# 5.8: "850",
# "p": "rohan"
# }
# print(book[3]) #advance python programming.   in dictionary if we enter the keys then the output gives the values.
# print(book[5.8]) #850
# print(book["p"]) #rohan
# print(book[10]) #keyError:10. if the key is not their in the dirct then if we are trying to find that key value then it shows as the "keyerror".


# "Iteams" #in iteams method instead of collan(:) we will get comma(,) in output.
# f={1:"rohan",2:6,3:4.7,5:[1,2]}
# print(f.items()) #([(1,'rohan'),(2,6),(3,4.7),(5,[1,2])])

"Clear" #the clear method is used to clear all the iteams in the dict.if use the clear in dict the output will be empty flower bracket {}.
# N={1:3,2:5.8,3:"rohan",4:{9,20},5:""}
# N.clear()
# print(N) #{}


"fromkeys" # it creats a new dictionary with keys by giving a new values.if we in sert a new value all the keys also get the same new value only.
# a=[1,2,3,4,5,6,7,8,9,10]
# print(dict.fromkeys(a,100)) #{1:100, 2:100, 3:100, 4:100, 5:100, 6:100, 7:100, 8:100, 9:100, 10:100} 

"get" #this is method is used to know what value is present in the key if their is any value it will print that value orelse if the key is not their in that dict it will print as "None"
# c={1:33,2:4.6,3:"ravula",4:{1,2},5:[33,55]}
# print(c.get(4)) #{1,2}
# print(c.get(5)) #[33,55]
# print(c.get(2)) #4.6
# print(c.get(10)) #None

"pop" #this method is used to remove (poped out) the vlaue form the key. in this method we need to menthon the key then it will gets poped out.
# r={1:33,2:4.6,3:"ravula",4:{1,2},5:[33,55]}
# r.pop(4) 
# print(r)  #{1:33,2:4.6, 3:'ravula',5:[33,55]}
# r.pop(33)
# print(r) #keyerror:33
# print(r.pop(3)) #'ravula'. by using this line we can know what is geting poped out.

"pop iteam" #this method is used to remove the last iteam form the dict.
# v={1:33,2:4.6,3:"ravula",4:{1,2},5:[33,55]}
# v.popitem()
# print(v) #{1:33,2:4.6,3:"ravula",4:{1,2}}

# "upadate" #this method is used to update the key with the new value and add the new key value pair in the dictionary.
# m={1:33,2:4.6,3:"ravula",4:{1,2}}
# m.update({4:"rohan"})
# print(m) #v={1:33,2:4.6,3:'ravula',4:'rohan'}.  in this case we have updated then new value.
# m.update({5:[2,3]})
# print(m) #{1:33,2:4.6,3:"ravula",4:{1,2},5:[2,3]}

"setdefault" #in this method if we trying to modify the already existing key vlaue it will not get modify. but we can insert the new key value in the dictionay by using the setdefault method.
m={1:33,2:4.6,3:"ravula",4:{1,2}}
m.setdefault(5, "rohan")
print(m)