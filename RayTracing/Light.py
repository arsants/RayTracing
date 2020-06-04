import math
import random

from Geo.Disk import Disk
from Geo.Vector import Vector


class Light:
    def __init__(self, pos, intensity, color):
        self.pos = pos
        self.intensity = intensity
        self.color = color
        self.area = 1
        self.type = "Light"


class DiskLight(Light, Disk):
    def __init__(self, pos, radius, intensity=6, color=Vector(1, 1, 1), samples=8, normal=Vector(0, -1, 0),
                 isDoubleSided=False, visible=True):
        Disk.__init__(self, pos, radius, normal)
        Light.__init__(self, pos, intensity, color)
        self.type = "AreaLight_Disk"
        self.radius = radius
        self.samples = samples
        self.normal = normal
        self.isDoubleSided = isDoubleSided
        self.visible = visible
        self.area = math.pi * math.pow(radius, 2)

    def getRandomSample(self):
        theta = random.random() * 2 * math.pi  # range [0,2pi)
        u = random.random() + random.random()
        # Better sampling method
        if u > 1:
            multiplier = 2 - u
        else:
            multiplier = u

        return self.pos + Vector(math.cos(theta) * self.radius * multiplier, 0,
                                 math.sin(theta) * self.radius * multiplier)
