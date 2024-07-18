import os 
import os.path as osp
import pandas as pd

train_csv_path = '/home/loki/tree_counting/from_kaggle/Palm-Counting-349images/train_labels.csv'
save_root = '/home/loki/tree_counting/data/labels/train'
df = pd.read_csv(train_csv_path)
print(df.head())

use = {'filename':0, 'width':1, 'height':2, 'class':3, 'xmin':4, 'ymin':5, 'xmax':6, 'ymax':7}

for index, row in df.iterrows():
    filename = row['filename']
    filename = filename.replace('.jpg', '.txt').replace('.JPG', '.txt').replace('.png', '.txt').replace('.PNG', '.txt')
    width = row['width']
    height = row['height']
    class_id = row['class']
    xmin = row['xmin']
    ymin = row['ymin']
    xmax = row['xmax']
    ymax = row['ymax']
    print(filename, width, height, class_id, xmin, ymin, xmax, ymax)

    file_path = osp.join(save_root, filename)

    if not osp.exists(file_path):
        file = open(file_path, 'w')
    else:
        file = open(file_path, 'a')
    
    file.write(f"0 {(xmax+xmin)/width/2} {(ymax+ymin)/height/2} {(xmax-xmin)/width} {(ymax-ymin)/height}\n")

    file.close()
    # break

    # save_path = os.path.join(save_root, filename)