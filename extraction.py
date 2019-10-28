import os
import json
import shutil

#This code extracts 'bdd100k_labels_images_train.json' file and constructs a file named 'data.json'
#path = os.path.join('train')

annot_file = os.path.join('bdd100k_labels_images_train.json')

#imgs = os.path.join('imgs')
x = True

with open('data.json', 'w+') as out:
  car = 0
  person = 0
  truck = 0
  traffic_light = 0
  traffic_sign = 0
  bike = 0 
  with open(annot_file, 'r') as f:
    json_data = json.load(f)
    for image in json_data:
      filename = image['name']
      data = {}  
      data['image'] = []  
      data['image'].append({  
            'name': filename
      }) 
      for label in image['labels']:
        if 'box2d' in label:
          class_name = label['category']
          if class_name == "car":
            if car == 10000:
              x = False
            else:
              car += 1
          elif class_name == "person":
            if person == 5000:
              x = False
            else:  
              person += 1
          elif class_name == "truck":
            if truck == 5000:
              x = False
            else:
              truck += 1
          elif class_name == "traffic light":
            if traffic_light == 5000:
              x = False
            else:
              traffic_light += 1
          elif class_name == "traffic sign":
            if traffic_sign == 5000:
              x = False
            else:  
              traffic_sign += 1
          elif class_name == "bike":
            if bike == 5000:
              x = False
            else:  
              bike += 1
          if(class_name == "car" or class_name == "person" or class_name == "truck" or class_name == "traffic light" or class_name == "traffic sign" or class_name == "bike"):
            print(class_name)
            print(x)
            if x:  
              coor = label['box2d']
              x1 = coor['x1']
              x2 = coor['x2']
              y1 = coor['y1']
              y2 = coor['y2']
              data['image'].append({'class name': class_name,
              'x1': x1,
              'x2': x2,
              'y1': y1,
              'y2': y2})
            x = True
      #print(data)
      if len(data['image']) > 1:
        json.dump(data, out)
        out.write(',')
        out.write('\n')
      if(car == 10000 and person == 5000 and truck == 5000 and traffic_light == 5000 and traffic_sign == 5000 and bike == 5000):
        break
