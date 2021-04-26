import os
import sys

from keras.utils.data_utils import get_file

ORIGIN = "https://dataset.com/"

def check_NWUCLA_dataset():
    version = 'v0.3'
    try:
        NWUCLA_path = os.path.join(os.getcwd(), 'datasets/NW-UCLA/')
        annot_path = get_file(NWUCLA_path + 'annotations.mat',
                ORIGIN + version + '/NWUCLA_annotations.mat',
                md5_hash='b37a2e72c0ba308bd7ad476bc2aa4d33')
        bbox_path = get_file(NWUCLA_path + 'NWUCLA_pred_bboxes_16f.json',
                ORIGIN + version + '/NWUCLA_pred_bboxes_16f.json',
                md5_hash='30b124a919185cb031b928bc6154fa9b')

        if os.path.isdir(NWUCLA_path + 'frames') is False:
            raise Exception('NWUCLA dataset (frames) not found! '
                    'You must download it by yourself from '
                    'http://dreamdragon.github.io/NW-UCLA')

    except:
        sys.stderr.write('Error checking NW-UCLA dataset!\n')
        raise

