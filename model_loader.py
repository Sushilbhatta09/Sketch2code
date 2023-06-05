"""
    This module is used to extract the coordinate locations of the
    bouding box of html elements taking the raw image as input
"""

import os
import torch
from pathlib import Path


static_path = os.path.join(Path(__file__).parent, "static")


class ModelConverter:
    """
        This class is used to return the coordinates of the html elements
        present in the image.
    """
    def __init__(self):
        self.model = torch.hub.load(
            'yolov5', 'custom', path='model/best.pt', force_reload=True, source='local')

    def model_to_coordinates(self, image):
        """
            After the image is taken as an input, the file output.txt is saved where
            the coordinates of the html elements and their class name is saved
        """
        self.model.conf = 0.4
        result = self.model(image, size=640)
        df = result.pandas().xyxy[0]
        df['xmin']=df['xmin']+10
        df['ymin']=df['ymin']
        df['width'] = (df['xmax'] - df['xmin'])
        df['height'] = (df['ymax'] - df['ymin'])/2
        df.sort_values(by=['ymin'])
        df.drop(['xmax','ymax'], axis=1, inplace=True)
        cols = df.columns.tolist()
        cols.insert(2, cols.pop(cols.index('width')))
        cols.insert(3, cols.pop(cols.index('height')))
        df = df.reindex(columns=cols)
        print(df)
        df.to_csv(os.path.join(
            static_path, 'output.txt'), sep=' ', index=False)

