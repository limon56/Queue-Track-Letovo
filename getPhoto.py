import os

def get():
    get_photo_cmd = "libcamera-jpeg -o test1.jpg"
    os.system(get_photo_cmd)

if __name__ == '__main__':
    get()