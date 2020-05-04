import glob
import os
import pdf2image

def main():
    doc_path = './docs/'
    document_files = read_file_list(doc_path)
    convert_to_image(document_files)


def convert_to_image(document_files, image_path='./imgs/'):
    for file in document_files:
        out_base = file[file.rfind('/')+1:file.rfind('.')]
        os.makedirs(image_path+out_base, exist_ok=True)
        images = pdf2image.convert_from_path(file, grayscale=True, dpi=300)
        for i, image in enumerate(images, start=1):
            image.save('{0}{1}/{1}_{2}.png'.format(image_path, out_base, i),
                       'png')


def read_file_list(doc_path='./docs/'):
    return glob.glob(doc_path + '*.pdf')


if __name__ == '__main__':
    main()
