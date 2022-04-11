import os


def create_folder_tree(folders: dict, root_dir: str):
    name_dir = root_dir
    for folder in folders:
        name_dir = os.path.join(name_dir, folder)
        if folders[folder]:
            create_folder_tree(folders[folder], name_dir)
        if not os.path.exists(name_dir):
            os.makedirs(name_dir)
        name_dir = root_dir


root_name = 'my_project'

dir_names = {
    'settings': dict(),
    'mainapp': dict(),
    'adminapp': dict(),
    'authapp': dict()
}

cur_dir_path = os.path.curdir

root = os.path.join(cur_dir_path, root_name)

create_folder_tree(dir_names, root)