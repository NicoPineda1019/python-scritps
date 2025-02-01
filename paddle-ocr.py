import os
from paddleocr import PaddleOCR
import psutil


def ocr_on_images_paddle(folder_path):
    results = {}
    for img_file in sorted(os.listdir(folder_path)):
        img_path = os.path.join(folder_path, img_file)
        result = ocrPaddle.ocr(img_path, cls=True)
        results[img_file] = result
    return results

print("Start program")
for i in range(0,100):
    print(f'iteration -> {i}')
    print("Start Ram MB: ", round(psutil.virtual_memory().used / 1000000))
    print("Start Ram%: ", psutil.virtual_memory().percent)

    ocrPaddle = PaddleOCR(use_angle_cls=True, lang="es")
    result = ocrPaddle.ocr('Cedula_David_Martinez_page-0001.jpg', cls=True)
    
    print("Finish Ram MB: ", round(psutil.virtual_memory().used / 1000000))
    print("Finish Ram%: ", psutil.virtual_memory().percent)
print("Finish program")
