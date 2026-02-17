#!/usr/bin/env python3

import os, time, threading
from PIL import Image
import cozmo
from cozmo.exceptions import RobotBusy, ConnectionAborted
import pygame

FRAMES_DIR = "frames_32x32"
FPS = 40
AUDIO_FILE = "/badapple.mp3"

def prep(robot):
    robot.drive_off_charger_on_connect = False

def load_frames():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    files = sorted(os.listdir(os.path.join(cur_dir, FRAMES_DIR)))
    frames = []
    for f in files:
        img = Image.open(os.path.join(cur_dir, FRAMES_DIR, f)).convert("RGB")
        img = img.resize(cozmo.oled_face.dimensions(), Image.NEAREST)
        frames.append(cozmo.oled_face.convert_image_to_screen_data(img, invert_image=True))
    return frames

def turn_off_backpack(robot: cozmo.robot.Robot):
    # Set the backpack LED to black (off)
    robot.set_backpack_lights(cozmo.lights.off_light)


def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load(AUDIO_FILE)
    pygame.mixer.music.play()

def play_loop(robot, frames):
    delay = 1.0 / FPS
    while True:
        for face in frames:
            try:
                robot.display_oled_face_image(face, int(delay * 1000))
                time.sleep(delay)
            except RobotBusy:
                pass
            except Exception:
                pass

def run(robot):
    prep(robot)
    frames = load_frames()
    threading.Thread(target=play_audio, daemon=True).start()

    while True:
        try:
            play_loop(robot, frames)
        except ConnectionAborted:
            print("Lost connection, retrying in 2s...")
            time.sleep(2)
        except Exception:
            # Silently ignore other errors (like delocalization)
            time.sleep(0.01)

cozmo.run_program(run)
