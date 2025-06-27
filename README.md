# Player-ID-Matcher-
Player Identity Matching using YOLO + CLIP
# 🏟️ Player Identity Matching using YOLO + CLIP

This project identifies and matches players across **multiple camera views** (broadcast and tacticam) using **YOLOv8 for detection** and **CLIP for feature matching**, and displays results via a clean **Streamlit interface**.

---

## 📌 Features

- 🎯 **Player detection** using YOLOv8
- 🧠 **Visual matching** using CLIP embeddings
- 📦 End-to-end pipeline in **Google Colab**
- 🖼️ View matched pairs via **Streamlit Web UI** in VS Code
- 📤 Export matches to CSV or side-by-side images

---

## 🛠️ Tech Stack

| Task         | Tool/Model         |
|--------------|--------------------|
| Object Detection | [Ultralytics YOLOv8](https://docs.ultralytics.com) |
| Visual Embeddings | OpenAI [CLIP](https://github.com/openai/CLIP) |
| UI            | [Streamlit](https://streamlit.io/) |
| Language      | Python 3.10+       |

---

## 📂 Folder Structure

player-id-matching/
- ├── final_results.pkl # Contains matched player IDs
- ├── player_id_streamlit_app.py # Streamlit frontend
- ├── output/
- │ ├── broadcast_crops/ # Cropped images from broadcast view
- │ └── tacticam_crops/ # Cropped images from tacticam view
- ├── exported_matches/ # (optional) Saved result images
- ├── matched_pairs.csv # (optional) CSV of matches
- └── README.md
## 🚀 Running the Pipeline (Colab)

Use the [Google Colab notebook](https://colab.research.google.com/) to:

1. Upload your videos
2. Run YOLO detection
3. Generate CLIP features
4. Match players
5. Save outputs to `final_results.pkl` and `output/` folder

Zip and download everything:

```python
!zip -r cropped_images.zip output/
from google.colab import files
files.download("cropped_images.zip")

## 💻 Running the UI (VS Code + Streamlit)

### ✅ Step 1: Setup

- Unzip `cropped_images.zip` into your VS Code project folder as a folder named `output/`.
- Place `final_results.pkl` in the same folder as `player_id_streamlit_app.py`.

Your folder should look like:

```
player-id-matching/
├── player_id_streamlit_app.py
├── final_results.pkl
├── output/
│   ├── broadcast_crops/
│   └── tacticam_crops/
```

---

### ✅ Step 2: Create & Activate Virtual Environment

<details>
<summary>Windows</summary>

```bash
python -m venv env
.\env\Scripts\activate
```

</details>

<details>
<summary>Mac/Linux</summary>

```bash
python3 -m venv env
source env/bin/activate
```

</details>

---

### ✅ Step 3: Install Dependencies

```bash
pip install streamlit pillow
```

Add others if needed (e.g., numpy, pandas).

---

### ✅ Step 4: Run Streamlit App

```bash
streamlit run player_id_streamlit_app.py
```

Open in your browser:  
📍 `http://localhost:8501`

---

## 📸 Output Examples

- ✅ Matched player pairs shown **side-by-side**
- 🎛️ Slider to **browse matches**
- 📤 Button to **export results**:
  - to CSV
  - to side-by-side image files

---

## 📝 TODO / Extensions

- 🔢 Add **jersey number OCR** for better ID verification
- 🛰️ Integrate **object tracking** to follow players over time
- 🧠 Show **similarity scores** for each match
- ☁️ Deploy on **Streamlit Cloud** or **Hugging Face Spaces**

---

## 🤝 Credits

- 🦾 YOLOv8 by [Ultralytics](https://github.com/ultralytics/ultralytics)
- 🎨 CLIP by [OpenAI](https://github.com/openai/CLIP)
- 🖼️ Streamlit for fast UI



