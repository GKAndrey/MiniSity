from ..models.map.sity import Sity
import random, re

def create_map():
    size = input()
    if not size:
        size = (random.randint(25, 50), random.randint(25, 50))
    else:
        size = (int(re.match("^([0-9]+)\s([0-9]+)$", size).group(1)), int(re.match("^([0-9]+)\s([0-9]+)$", size).group(2)))
    sity = Sity(size,2)