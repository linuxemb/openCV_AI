import cv2 as cv
import os
import numpy as np 

people = ['naying', 'zhaolei','zhangziyi']

DIR = r'C:\Users\lshi34\Pictures\actors' 
p = []
for i in os.listdir(r'C:\Users\lshi34\Pictures\actors'):
    p.append(i)
print(p)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

labels = []
features = []

def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)

            for(x,y,w,h ) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()

print ('Training done -----------------')


# Train the Recognizer on the featured list and the labels list

features = np.array(features, dtype = 'object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')

print(f'Length of the features = {len(features)}')
print(f'Length of the leabels = {len(labels)}')

np.save('feature.npy', features)
np.save('lables.npy' , labels)