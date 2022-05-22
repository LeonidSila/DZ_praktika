import os
import yaml

my_values = ['settings','mainapp','adminapp','authapp']
my_keys = 'my_project'
my_dict = {my_keys : my_values}

dir_path = [os.makedirs(os.path.join(my_keys,i)) for i in my_values if not os.path.exists(os.path.join(my_keys,i))]

print(os.path.join(os.path.abspath(os.getcwd()), my_keys))
my_path=os.path.join(os.path.abspath(os.getcwd()), my_keys)
for i in my_values:
    print(os.path.join(my_path,i))

with open ('Lesson_7_1_config.yaml','w') as f:
    yaml.dump(my_path, f)
    for i in my_values:
        yaml.dump(os.path.join(my_path, i),f)
    pass