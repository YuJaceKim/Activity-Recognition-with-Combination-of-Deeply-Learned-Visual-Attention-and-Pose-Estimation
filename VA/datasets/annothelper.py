import os
import sys

from keras.utils.data_utils import get_file

ORIGIN = "https://dataset.com/"

def check_UCF11_dataset():
    version = 'v0.3'
    try:
        ucf11_path = os.path.join(os.getcwd(), 'datasets/UCF-11/')
        annot_path = get_file(ucf11_path + 'annotations.mat',
                ORIGIN + version + '/ucf11_annotations.mat',
                md5_hash='b37a2e72c0ba308bd7ad476bc2aa4d33')
        bbox_path = get_file(ucf11_path + 'ucf11_pred_bboxes_16f.json',
                ORIGIN + version + '/ucf11_pred_bboxes_16f.json',
                md5_hash='30b124a919185cb031b928bc6154fa9b')

        if os.path.isdir(ucf11_path + 'frames') is False:
            raise Exception('UCF11 dataset (frames) not found! '
                    'You must download it by yourself from '
                    'http://dreamdragon.github.io/UCF-11')

    except:
        sys.stderr.write('Error checking UCF-11 dataset!\n')
        raise

def check_HMDB51_dataset():
    try:
        HMDB51_path = os.path.join(os.getcwd(), 'datasets/HMDB-51/')

        if os.path.isdir(HMDB51_path + 'images-small') is False:
            raise Exception('HMDB51 dataset (images-small) not found! '
                    'You must download it by yourself from '
                    'http://rose1.HMDB51.edu.sg/Datasets/actionRecognition.asp '
                    'and extract the video files. A helper Python script is '
                    'given for that in '
                    'datasets/HMDB51/extract-resize-videos.py')

        if os.path.isdir(HMDB51_path + 'HMDB51rgb+d_numpy') is False:
            raise Exception('HMDB51 dataset (HMDB51rgb+d_numpy) not found! '
                    'Please download the annotations from '
                    'TODO [LINK] '
                    'and extract the file in datasets/HMDB-51')
    except:
        sys.stderr.write('Error checking HMDB-51 dataset!\n')
        raise

def check_Hollywood2_dataset():
    try:
        Hollywood2_path = os.path.join(os.getcwd(), 'datasets/Hollywood2/')

        if os.path.isdir(Hollywood2_path + 'images-small') is False:
            raise Exception('Hollywood2 dataset (images-small) not found! '
                    'You must download it by yourself from '
                    'http://rose1.Hollywood2.edu.sg/Datasets/actionRecognition.asp '
                    'and extract the video files. A helper Python script is '
                    'given for that in '
                    'datasets/Hollywood2/extract-resize-videos.py')

        if os.path.isdir(Hollywood2_path + 'Hollywood2rgb+d_numpy') is False:
            raise Exception('Hollywood2 dataset (Hollywood2rgb+d_numpy) not found! '
                    'Please download the annotations from '
                    'TODO [LINK] '
                    'and extract the file in datasets/Hollywood2')
    except:
        sys.stderr.write('Error checking Hollywood2 dataset!\n')
        raise
