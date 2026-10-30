# sets & arrays fruit basket orgsnizer
basket1 = {"apple","banana","mango","apple","grape"}
basket2 = {"mango","kiwi","banana","kiwi"}
print("basket 1:",basket1)
print("basket 2:",basket2)

basket1.add ("orange")
print("basket 1 after addin orange:", basket1)

common_fruits = basket1.intersection(basket1)
print("fruits in both basket:", common_fruits)

import array as arr
fruits_counts = arr.array('i', [3,5,2,4])
print("fruit count",fruits_counts)
fruits_counts.insert(0,4)
fruits_counts.append(6)
print(fruits_counts)
fruits_counts.reverse()
print(fruits_counts)