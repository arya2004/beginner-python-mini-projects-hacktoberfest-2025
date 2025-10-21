import cv2 
import face_recognition

known_face_name=[]
known_face_encodings=[]

known_person1_image=face_recognition.load_image_file(r"images\PR1.jpg")
known_person2_image=face_recognition.load_image_file(r"images\PR2.jpg")
known_person3_image=face_recognition.load_image_file(r"images\PR3.jpg")

known_person1_encoding=face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding=face_recognition.face_encodings(known_person2_image)[0]
known_person3_encoding=face_recognition.face_encodings(known_person3_image)[0]

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)

known_face_name.append("Amit")
known_face_name.append("Rakesh")
known_face_name.append("Pratyaksh")

# intialize webcam
video_capture=cv2.VideoCapture(0)

while True:
    #Capture Frame by Frame
    ret,frame=video_capture.read()
    # ret=true if reade frame sucessfully and frame has a numpy array of frome data
    # find all face locations in current frame
    face_locations=face_recognition.face_locations(frame)
    # detect all the faces in fram and give tupple codinate top right left bottom
    face_encodings=face_recognition.face_encodings(frame,face_locations)
    # convert face into 128 dimensional array used to compare faces

    # loop through each face found in frame
    for (top,right,bottom,left), face_encoding in zip(face_locations,face_encodings):
        # zip pair each face wit its encoding
        #  check if face match any known face
        matches=face_recognition.compare_faces(known_face_encodings,face_encoding)
        # ccomapare features
        name="Unknown"
        # if face is not recognised by deafault value

        if True in matches:
            first_match_index=matches.index(True)
            # gives index of matched face
            name=known_face_name[first_match_index]
            # name of matched face
        
        # Draw a box around the face and label the name
        cv2.rectangle(frame, (left,top),(right,bottom),(0,0,255),2)
        cv2.putText(frame,name,(left,top - 10),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.9,(0,0,255),2)

    # dispaly resulting frame
    cv2.imshow("Video",frame)

    # break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # & oxFF checks compatibilty with different system
        break

#  release webcam and close opencv windows

video_capture.release()
cv2.destroyAllWindows