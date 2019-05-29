import os

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
os.environ['PATH'] = os.environ['PATH'] + os.sep + DIR_PATH
os.environ['PYTHONPATH'] = os.environ['PYTHONPATH'] + os.sep + DIR_PATH
