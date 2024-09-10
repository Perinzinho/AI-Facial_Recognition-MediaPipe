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

