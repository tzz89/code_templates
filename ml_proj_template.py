# This is simple script to generate an ML-project
import os

if __name__ == '__main__':
    author = input("Author name: ")
    project_description = input("Project Description: ")
    license = input("license: ")

    misc_folders = [
        os.path.join('data', 'raw'),
        os.path.join('data', 'processed'),
        os.path.join('models'),
        'configs',
        'notebooks',
        'references',
        'figures',
    ]

    # this folders are based on
    # https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning

    src_folders = [
        'src',
        os.path.join('src', 'data_extraction'),
        os.path.join('src', 'data_validation'),
        os.path.join('src', 'data_preprocessing'),
        os.path.join('src', 'model_training'),
        os.path.join('src', 'model_validation'),
    ]

    files = [
        'requirements.txt',
        'README.md',
        os.path.join('configs', 'params.yaml'),
        os.path.join('configs', 'dvc.yaml')

    ]
# ****Do not leave any spaces in git_ignore or it might cause some problems with DVC

    git_ignores = '''# Jupyter NB Checkpoints
.ipynb_checkpoints/
# DotEnv configuration
.env
# Pycharm
.idea
'''

    setup_template = f'''from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='{project_description}',
    author='{author}',
    license='{license}',
    install_requires=[] 
)
    '''
    manifiest_doc = "include *.md *.txt LICENSE"

    for folder in misc_folders:
        os.makedirs(folder, exist_ok=True)

        # adding gitkeep to maintain structure
        with open(os.path.join(folder, ".gitkeep"), 'w') as f:
            pass

    for folder in src_folders:
        os.makedirs(folder, exist_ok=True)
        # with open(os.path.join(folder, '.gitkeep'), 'w') as f:
        #     pass
        with open(os.path.join(folder, '__init__.py'), 'w') as f:
            pass

    for file in files:
        with open(file, 'w') as f:
            pass

    with open('.gitignore', 'w') as f:
        f.write(git_ignores)

    with open('MANIFEST.in', 'w') as f:
        f.write(manifiest_doc)

    with open('setup.py', 'w') as f:
        f.write(setup_template)
