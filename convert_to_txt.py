import cv2
import glob
import pyocr

def main():
    doc_path = './docs/'
    document_files = read_file_list(doc_path)


def read_file_list(doc_path='./docs/'):
    return glob.glob(doc_path + '*.pdf')


if __name__ == '__main__':
    main()
