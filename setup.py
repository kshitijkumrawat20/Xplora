## make a for loop that iterates over the list of files  and create __init__.py files in each directory
import os
def create_init_files(base_path):
    for root, dirs, files in os.walk(base_path):
        if '__init__.py' not in files:
            with open(os.path.join(root, '__init__.py'), 'w') as f:
                f.write('# This is an init file for the package\n')

# Example usage
if __name__ == "__main__":
    base_path = 'C:\code\Explora'  # Change this to your package path
    create_init_files(base_path)
    print("Init files created successfully.")