import os
from paddleocr import PaddleOCR



def ocr_on_images_paddle(folder_path):
    results = {}
    for img_file in sorted(os.listdir(folder_path)):
        img_path = os.path.join(folder_path, img_file)
        result = ocrPaddle.ocr(img_path, cls=True)
        results[img_file] = result
    return results

for i in range(0,100):
    ocrPaddle = PaddleOCR(use_angle_cls=True, lang="es")
    result = ocrPaddle.ocr('Cedula_David_Martinez_page-0001.jpg', cls=True)