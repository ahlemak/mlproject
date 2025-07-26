from setuptools import setup, find_packages
# Function to read dependencies from a file
HYPEN_E_DOT = '-e .'
def read_dependencies(file_name):
    try:
        with open(file_name, 'r') as file:
            dependencies = [line.strip() for line in file if line.strip()]
            if HYPEN_E_DOT in dependencies:
                dependencies.remove(HYPEN_E_DOT)
        return dependencies
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Read dependencies from requirements.txt
setup(
    name='mlproject',  # Name of your project
    version='1.0.0',                # Version number
    author='Ahlem',             # Author name
    author_email='akal.ahlem@gmail.com',  # Author email
    description='A data science project for.',  # Short description # Project URL
    packages=find_packages(),       # Automatically find Python packages in your project
    # install_requires=['numpy','matplotlib']
    install_requires=read_dependencies('requirements.txt')
)