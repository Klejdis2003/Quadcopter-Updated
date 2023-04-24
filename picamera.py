from picamera import PiCamera
from time import sleep, time

camera = PiCamera()
class CameraFunctions:
    @staticmethod
    def preview(time):
        camera.start_preview()
        sleep(time)
        camera.stop_preview()
    @staticmethod
    def picture():
        camera.capture(f'Pictures/image{int(time())}.jpg')
    @staticmethod
    def video(time):
        camera.start_preview()
        camera.start_recording(f'Video/video{int(time())}.h264')
        sleep(time)
        camera.stop_recording()
        camera.stop_preview()