import cv2
import glob
import pyocr
from PIL import Image

def main():
    img_path = './imgs/'
    img_files = get_img_files(img_path)
    convert_to_txt(img_files)

def convert_to_txt(img_files):
    # get OCR tools you installed
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print('no tools')
        return
    # use Tesseract (first of tools list)
    tool = tools[0]
    for img_file in img_files:
        # read as grayscale image
        gray_img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
        # convert to binary image
        _, binary_img = cv2.threshold(gray_img, 220, 255, cv2.THRESH_BINARY)

        txt = tool.image_to_string(image=Image.fromarray(binary_img),
                                   lang='jpn',
                                   builder=pyocr.builders.TextBuilder(tesseract_layout=6))
        print(txt)
        break

def get_img_files(img_path='./imgs/'):
    return glob.glob(img_path+'*/*.png')


if __name__ == '__main__':
    main()
