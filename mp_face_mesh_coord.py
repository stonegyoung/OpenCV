import cv2
import mediapipe as mp

img = cv2.imread('data/karina.jpg')

mp_face_mesh = mp.solutions.face_mesh
# print(dir(mp_face_mesh))

mp_drawing = mp.solutions.drawing_utils
face_mesh = mp_face_mesh.FaceMesh()

results = face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

img_height, img_width, _ = img.shape

lip_index = set()
if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        for idx1, idx2 in (mp_face_mesh.FACEMESH_LIPS): # index
            lip_index.add(idx1)
            lip_index.add(idx2)
        for idx in lip_index:
            x = face_landmarks.landmark[idx].x
            y = face_landmarks.landmark[idx].y
            real_x = int(x * img_width)
            real_y = int(y * img_height)
            cv2.circle(img, (real_x, real_y), 1, (0,0,255), 2)
        # print(face_landmarks.landmark[mp_face_mesh.FACEMESH_LIPS])

cv2.imshow('', img)
cv2.waitKey()
cv2.destroyAllWindows()
