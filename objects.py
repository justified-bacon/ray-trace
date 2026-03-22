import numpy as np

class Objects():
    def __init__(self, type, **kwargs):
        if type not in ['sphere', 'mesh', 'cylinder']:
            raise TypeError('type of object must be "sphere", "mesh" or "cylinder"')
        self.type = type

        if self.type == 'sphere':
            self.radius = kwargs.get('radius')
            self.position = kwargs.get('position')
    
