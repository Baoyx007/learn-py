__author__ = 'haven'
import sys, struct


def check_bmp(pic_meta):
    if len(pic_meta) < 30:
        return [False, ]
    else:
        bmp_info = struct.unpack('<ccIIIIIIHH', pic_meta)
        if bmp_info[0] == b'B' and (bmp_info[1] == b'M' or bmp_info[1] == b'1'):
            return [False, bmp_info[2], bmp_info[9]]
        else:
            return [False, ]


if __name__ == '__main_':
    with open(sys.argv[1], 'rb') as f:
        meta = f.read(30)
        info = check_bmp(meta)
        if info[0]:
            print('%s is a bmp file,size is %d,%dbit clolr' % (sys.argv[1], info[1], info[2]))
        else:
            print('not a bmp file')
