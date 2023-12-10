
updated_names = ['main_dish_40', 'main_dish_40', 'main_dish_40', 'box', 'main_dish_30',
                'main_dish_30', 'main_dish_25', 'main_dish_25', 'brown rice', 'main_dish_25',
                'main_dish_25', 'main_dish_25', 'main_dish_25', 'main_dish_25', 'main_dish_25',
                'main_dish_25', 'main_dish_25', 'main_dish_25', 'main_dish_25', 'main_dish_25',
                'main_dish_25', 'main_dish_25', 'main_dish_25', 'main_dish_30', 'main_dish_25',
                'main_dish_25', 'main_dish_25', 'main_dish_25', 'main_dish_30', 'main_dish_25',
                'plate', 'main_dish_25', 'purple rice','main_dish_40', 'main_dish_25',
                'main_dish_25', 'main_dish_25', 'main_dish_25', 'main_dish_25', 'side dish',
                'main_dish_25', 'main_dish_25',  'main_dish_25',  'main_dish_25', 'main_dish_30',
                'main_dish_25', 'main_dish_25', 'main_dish_25', 'main_dish_25', 'main_dish_25',
                'white rice', 'main_dish_25']


list_in_yaml = ['plate', 'box', 'white rice', 'brown rice', 'purple rice', 'side dish', 'main_dish_25', 'main_dish_30', 'main_dish_40']

label_mapping = {
    'plate': 0,
    'box': 1,
    'white rice': 2,
    'brown rice': 3,
    'purple rice': 4,
    'side dish': 5,
    'main_dish_25': 6,
    'main_dish_30': 7,
    'main_dish_40': 8
}

import os
import yaml

def update_yaml_file(file_path, my_list):
    # Read the original YAML file
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    
    
    # Update the 'names' and 'nc' fields
    data['names'] = my_list
    data['nc'] = len(my_list)
    print(data)
    
    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        yaml.dump(data, file)
      
def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        parts = line.split()
        if parts:
            # Increment the first integer
            parts[0] = str(label_mapping[updated_names[int(parts[0])]])
            modified_line = ' '.join(parts)
            modified_lines.append(modified_line)

    with open(file_path, 'w') as file:
        file.write('\n'.join(modified_lines))

def process_directory(directory):
    labels_dir = os.path.join(directory, 'labels')
    if os.path.exists(labels_dir):
        for filename in os.listdir(labels_dir):
            if filename.endswith('.txt'):
                file_path = os.path.join(labels_dir, filename)
                process_file(file_path)

def main():
    directories = ['test', 'train', 'valid']
    for directory in directories:
        process_directory(directory)
    
main() #  modified labels
#update_yaml_file('data.yaml',list_in_yaml)#moified_yaml
        
        
        
        
        
        