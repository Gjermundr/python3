import os
import shutil
import datetime
import zipfile



root_path = os.getcwd()
print('Current root path: ', root_path)
old_dir_path = os.path.join(root_path, 'dir-1')  # set the copy-from dir
new_dir = input('Enter name of new directory: ')
new_dir_path = os.path.join(root_path, new_dir)
print('created new directory ...')


def Listcontents(path):
    l1 = []
    for root, dirs, files in os.walk(path):
        for name in files:
            l1.append(os.path.join(root, name))

        for name in dirs:
            l1.append(os.path.join(root, name))
    return l1

# copying contents to new folder
old_dir_contents = Listcontents(old_dir_path)
print('Copying contents of "dir-1" to new location ...\n')
shutil.copytree(old_dir_path, new_dir_path, copy_function=shutil.copy2)

# add mod_date to file name
list_new_dir = Listcontents(new_dir_path)
print('Modifying file names ...\n')
for file in list_new_dir:
    if file.find('.') != -1:
        file_stats = os.stat(file)
        file_mtime = datetime.datetime.fromtimestamp(file_stats.st_mtime)
        file_mtime2 = str(file_mtime)
        mdate = file_mtime2[:11]
        split_str = file.split('.')
        s1 = split_str[0]
        s2 = split_str[1]
        new_str = s1 +'_'+ mdate +'.'+ s2
        os.rename(file, new_str)

# display the new directory and content
print('\nContents of new directory!')
for current, subdirectories, files in os.walk(new_dir_path):
    print('Current directory:', current)

    for current_subdir in subdirectories:
        print('Subdirectory:', current_subdir)

    for current_file in files:
        print('File:', current_file)

    print()

print(new_dir_path)
print(os.getcwd())

zipfile.ZipFile(new_dir, 'r', )