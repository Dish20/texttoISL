import os
from PIL import Image

# Path to your ISL dataset folder
BASE_DIR = "C:\\Users\\dksr3\\myfolderd\\isl_dataset"

# Build dictionary: phrase → list of image paths
phrase_to_images = {}

for phrase_folder in os.listdir(BASE_DIR):
    folder_path = os.path.join(BASE_DIR, phrase_folder)
    if os.path.isdir(folder_path):
        images = [os.path.join(folder_path, img) for img in os.listdir(folder_path) if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        phrase_to_images[phrase_folder.lower()] = images

def show_sign(phrase):
    phrase = phrase.lower().strip()
    if phrase in phrase_to_images:
        image_path = phrase_to_images[phrase][0]  # You can randomize or pick more later
        print(f"Showing ISL sign for: '{phrase}'")
        img = Image.open(image_path)
        img.show()
    else:
        print(f"❌ No ISL sign found for: '{phrase}'")

# Main loop
while True:
    user_input = input("\nType an English phrase (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    show_sign(user_input)
