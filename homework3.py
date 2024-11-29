#homework 3
a_pair_of_trousers = 70.5
a_t_shirt = 20.89
a_vest = 100.3
print("****welcome to the checkout system ****")
a = int(input(" How many trousers have been bought?"))
b  = int(input("How many t-shirts have been bought?"))
c = int(input("How many vests have been bought?"))

total_cost = (a * a_pair_of_trousers) + (b * a_t_shirt) + (c * a_vest)

print( f" You have bought Trousers : {a} pair(s),"
       f"You have bought T-shirts : {b} piece(s)"
       f"You have bought Vests : {c}  piece(s)"
       f"Total: {total_cost} \n")