import numpy
import numpy as np
numbers=np.arange(2.05, 97.85, 2.05)
print(numbers)
store_id = id(numbers)
print(f"{'':+^100}")
end_word:str = "/"
for i, num in enumerate(numbers):
    fix_price = str(f"{float(num):.2f}").split(".")
    if i == len(numbers) - 1:
        end_word = "\n"
    print(f"{fix_price[0]} рубасы {fix_price[1]} коп", end=end_word)
print(f"{'':-^100}")
print(f"id Перед {store_id}")
print(sorted(numbers))
print(f"id После {id(numbers)}")
print(f"{'':+^100}")
copy_of_list = numbers.copy()
print(sorted(copy_of_list,reverse=True))
print(store_id)
print(id(copy_of_list))
print(f"{'':+^100}")
print("Могу", numbers[-6:-1])