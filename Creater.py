from moviepy.editor import ImageSequenceClip
import os

def create_gif(gif_name, fps):
    image_folder = r"E:\Gif-Creater"  # Update to your image folder path using raw string (r"")

    image_files = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
    image_files.sort()  

    clip = ImageSequenceClip([os.path.join(image_folder, img) for img in image_files], fps=fps)
    clip.write_gif(gif_name, fps=fps)

def main():
    gif_name = "output.gif"
    fps = 10 

    create_gif(gif_name, fps)

if __name__ == "__main__":
    main()

