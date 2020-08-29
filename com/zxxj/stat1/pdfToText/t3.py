from pdf2image import convert_from_path,convert_from_bytes
import tempfile
import os
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import cv2 #导入opencv库
read_path = "I:/cache/年报/年报/"



if __name__ == "__main__":

    pdfPath = read_path + "12-09.pdf"
    imagePath = read_path + "image/"
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path(pdfPath, output_folder=path, dpi=300,thread_count=4,
                                             first_page = 167)
        for image in images_from_path:
            if not os.path.exists(imagePath):
                os.makedirs(imagePath)
            image.save(imagePath + '/' + 'psReport_%s.png' % images_from_path.index(image), 'PNG')
        print(images_from_path)