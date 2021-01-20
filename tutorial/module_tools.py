import random

feet_in_mile = 5280
m_in_km = 1000
arr = [1,2,3,4,5]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(n):
    return random.randint(1, n)