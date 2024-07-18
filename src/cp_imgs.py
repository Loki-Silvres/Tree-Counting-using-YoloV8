import os 
import os.path as osp
import shutil

root = '/home/loki/tree_counting/from_kaggle/Palm-Counting-349images/test'
new_root = '/home/loki/tree_counting/data/images/val'

for filename in os.listdir(root):
    if filename.endswith('.jpeg') or filename.endswith('.jpg'):
        path = osp.join(root, filename)
        new_path = osp.join(new_root, filename)
        shutil.copyfile(path, new_path)