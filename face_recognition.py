import uuid

import cv2
import requests


def get_count_of_faces(image_url):
    """
    Returns count of faces in the image
    :param image_url:
    :return:
    """
    image_temp_path = str(uuid.uuid4())
    open(image_temp_path, 'wb+').write(requests.get(image_url).content)

    image = cv2.imread(image_temp_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('cv.xml')
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return len(faces)

