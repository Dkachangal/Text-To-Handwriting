from plyer import camera

def take_photo(filename="captured.jpg"):
    camera.take_picture(filename, on_complete=process_image)
