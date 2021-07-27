import os
import argparse
import json

#parser initialize 

parser = argparse.ArgumentParser(description='Split file json into train and test')
parser.add_argument('-JFile', '--JFile', type = str, metavar = '', help= 'Json file needed to be split')
parser.add_argument('-testDir', '--testDir', type = str, metavar ='', help = ' Folder contain test images')
parser.add_argument('-trainDir', '--trainDir', type = str, metavar = '', help = 'Folder contain train images')
parser.add_argument('-out', '--out', type = str, metavar = '', help =' folder where to save')

args = parser.parse_args()
	


def split_json_file(flag,trainDir, testDir, outDir, JPath):
	if flag == 'train':
		path = testDir
	else:
		path = trainDir

	# Saving all the image names of train/test folder into an array
	names = []
	for file in os.listdir(path):
		if file.endswith('.png'):
			names.append(file)

	f = open(JPath)
	data = json.load(f)
	mul_images_id = []
	
	#Loaded ids of 'annotations'  by their by through the 'images' 
	for key in data:
		if key == 'images':
			try:
				for index in range(len(data[key])):
					if data[key][index]['file_name'] in names:
						mul_images_id.append(data[key][index]['id'])
			except:
				print('errors in loading ids in images section' )

	#removing ids  not in train/test in images section  	
	# if flag equal train then save the id of test images to remove
	for name in names:
			for index in range(len(data['images'])):
					if data['images'][index]['file_name'] == name:
						data['images'].pop(index)
						break 
	
	#removing ids not in train/test in annotations section 
	# if flag equal train then save the id of test images to remove
	for _id in mul_images_id:
			for index in range(len(data['annotations'])):
					if data['annotations'][index]['image_id'] == _id:
						data['annotations'].pop(index)
						break 
				
	f.close()	

	#saving to 'out' folder
	savedPath = os.path.join(outDir,  f'{flag}.json')
	with open(savedPath, "w") as jsonFile:
	    json.dump(data, jsonFile)
		

if __name__ =='__main__':
	for i in ['train', 'test']:
		split_json_file(i,args.trainDir, args.testDir,  args.out, args.JFile)	
