import moviepy
from moviepy.editor import *
import pygame

clip = VideoFileClip('video.mp4')
clip.preview()

pygame.quit()