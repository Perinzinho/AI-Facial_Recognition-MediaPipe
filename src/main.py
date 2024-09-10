#OBS:Precisa ser alterado o codigo para o mediapipe, editar também o readme
#para utilizar o mediapipe com o codigo é necessario que voce instale o git no pc
#abrir e colocar o codigo: pip installmediapipe opencv-python
import mediapipe as mp

import cv2
import mediapipe as mp

#inicialização das soluções do mediapipe
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils 
mp_drawing_styles = mp.solutions.drawing_styles

#configuração da webcam
cap = cv2.VideoCapture(0)

#Inicializa o facemesh
with mp_face_mesh.Facemash(
    max_num_faces=1, #detecta até 1 rosto(adicionar + se precisar)
    refine_landmarks=True, #Refinamento p/ olhos e labios
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:

    while cap.isOpened():
        sucess, image = cap.read()
        if not sucess:
            print("Não foi possivel capturar a imagem")
            break
