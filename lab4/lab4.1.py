import argparse
import os
import struct

parser = argparse.ArgumentParser(description='Parser for first exercise (labwork 4)')
parser.add_argument('-d', type=bool, default=False)
my_parser = parser.parse_args()
path = os.getcwd()+'\\music'


class Sound(object):
    author = ""
    name = ""
    alb_name = ""
    teg = ""
    number = ""


class Ex1(object):
    tracklist = []

    def __init__(self, bit=16):
        self.__files = os.listdir(path=path)
        self.__bit = bit

    def decoding(self):

        for file in self.__files:
            with open(path+'\\'+file, 'rb') as f:
                f.seek(-128, 2)
                obj = f.read()
                sn = Sound()
                sn.teg, sn.name, sn.author, sn.alb_name, sn.number = struct.unpack('<3s30s30s30s35s', obj)
                self.tracklist.append(sn)
                del sn
        for track in self.tracklist:
            print('[ ' + track.author.decode('windows-1251') + " ]  -  [ " +
                  track.name.decode('windows-1251') + " ]  -  [ " +
                  track.alb_name.decode('windows-1251') + " ]")


if __name__ == '__main__':
    objec = Ex1()
    objec.decoding()