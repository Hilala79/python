liste =[(3,4),(10,3),(5,6),(1,9)]
res_list = [i[0] for i in liste]
res_list1 = [i[1] for i in liste]

print(list(map(lambda x,y:x*y, res_list,res_list1)))
