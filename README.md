# Split_dataset_train

Usage: 

  -splitdataset.py
  
    This file is to take a proportion of train dataset to test dataset
    ├── train
    │   ├── class1
    │     ├── image1.png
    │     └── image2.png
    │     └── ...
    │     
    │   ├── class2
    │     ├── image1.png
    │     └── image2.png
    │     └── ...
    │
    │   ├──... 
    
    command to use: python splitdataset.py --data_path /path/to/train/dataset/ --test_data_path_to_save /path/to/save/test/dataset/ --train_ratio 0.7
  
  -createjsonfile.py
  
    This file is to split the original json file into train.json and test.json
        -Note: this file is only use after you already have a train and test dataset
    
    command to use: python createjsonfile.py --trainDir /path/to/train/dataset/ --testDir  /path/to/test/dataset/ -JFile /path/to/json/file --out /path/to/save/files 
    
Dataset:

  test.zip  - test datasets
  train.zip - train datasets

Json File: 

  train.json - train json for train dataset
  test.json  - test json  for test dataset
