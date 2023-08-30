import random

from framework.render import Render
from framework.vectorclass import Vector

class Particle:
    def __init__(self):
        self.particles = []

    def renderParticle(self, particle):
        """Overwriteable"""


    def emit(self):
        for particle in self.particles:
            self.renderParticle(particle)

    def addParticles(self, *params: list, count=1):
        for _ in range(count):
            self.particles.append(*params)

    def deleteParticle(self, particle):
        self.particles.remove(particle)