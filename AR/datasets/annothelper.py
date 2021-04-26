import os
import sys

from keras.utils.data_utils import get_file

ORIGIN = "https://dataset.com/"

def check_pennaction_dataset():
    version = 'v0.3'
    try:
        penn_path = os.path.join(os.getcwd(), 'datasets/PennAction/')
        annot_path = get_file(penn_path + 'annotations.mat',
                ORIGIN + version + '/penn_annotations.mat',
                md5_hash='b37a2e72c0ba308bd7ad476bc2aa4d33')
        bbox_path = get_file(penn_path + 'penn_pred_bboxes_16f.json',
                ORIGIN + version + '/penn_pred_bboxes_16f.json',
                md5_hash='30b124a919185cb031b928bc6154fa9b')

        if os.path.isdir(penn_path + 'frames') is False:
            raise Exception('PennAction dataset (frames) not found! '
                    'You must download it by yourself from '
                    'http://dreamdragon.github.io/PennAction')

    except:
        sys.stderr.write('Error checking PennAction dataset!\n')
        raise

def check_ntu_dataset():
    try:
        ntu_path = os.path.join(os.getcwd(), 'datasets/NTU/')

        if os.path.isdir(ntu_path + 'images-small') is False:
            raise Exception('NTU dataset (images-small) not found! '
                    'You must download it by yourself from '
                    'http://rose1.ntu.edu.sg/Datasets/actionRecognition.asp '
                    'and extract the video files. A helper Python script is '
                    'given for that in '
                    'datasets/NTU/extract-resize-videos.py')

        if os.path.isdir(ntu_path + 'nturgb+d_numpy') is False:
            raise Exception('NTU dataset (nturgb+d_numpy) not found! '
                    'Please download the annotations from '
                    'TODO [LINK] '
                    'and extract the file in datasets/NTU')
    except:
        sys.stderr.write('Error checking NTU dataset!\n')
        raise

