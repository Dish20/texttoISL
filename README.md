# texttoISL
# ISL Sign Language Translator (Image Viewer)

This project is a simple **Indian Sign Language (ISL) phrase viewer**.  
It allows you to type an English word/phrase and displays the corresponding ISL sign image (if available in your dataset).

---

## 📂 Project Structure

isl_dataset/
│
├── hello/
│ ├── 1.png
│ ├── 2.jpg
│
├── thank_you/
│ ├── 1.png
│ ├── 2.jpg


- Each folder inside `isl_dataset` is named after an **English phrase** (e.g., `hello`, `thank_you`).
- Inside each folder are one or more **image files** (`.png`, `.jpg`, `.jpeg`, `.gif`) showing the ISL sign for that phrase.

---



## 📝 Features

Maps English phrases → ISL sign images.

Supports multiple image formats: .png, .jpg, .jpeg, .gif.

Case-insensitive phrase matching (Hello, hello, HELLO all work).

Displays the first matching image (can be extended to randomize).

## 🚀 Future Improvements

Randomize which image is shown when multiple images exist.

Support for animated GIFs (continuous playback).

Extend dataset with more ISL phrases.

Build a GUI using Tkinter or Streamlit.
