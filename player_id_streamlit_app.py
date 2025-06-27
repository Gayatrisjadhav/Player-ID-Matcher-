import streamlit as st
import pickle
import os
from PIL import Image

# === Paths ===
RESULTS_PATH = "final_results.pkl"
BROADCAST_DIR = "output/output/broadcast_crops"
TACTICAM_DIR = "output/output/tacticam_crops"

# === Load the matching results ===
@st.cache_data
def load_results():
    with open(RESULTS_PATH, "rb") as f:
        result = pickle.load(f)
    return result

# Load results
result = load_results()
matched_pairs = result["matched_pairs"]
broadcast_crop_paths = result["broadcast_crop_paths"]
tacticam_crop_paths = result["tacticam_crop_paths"]

# === Streamlit Page Config ===
st.set_page_config(page_title="🎯 Player ID Matcher", layout="wide")
st.title("🎯 Player Identity Matching Viewer")
st.markdown("Browse matched players from broadcast and tacticam views.")

# === Match Slider ===
match_index = st.slider("Select match index", 0, len(matched_pairs) - 1, 0)

b_id, t_id = matched_pairs[match_index]

b_img_path = os.path.join(BROADCAST_DIR, os.path.basename(broadcast_crop_paths[b_id]))
t_img_path = os.path.join(TACTICAM_DIR, os.path.basename(tacticam_crop_paths[t_id]))


col1, col2 = st.columns(2)

with col1:
    st.subheader(f"📺 Broadcast Player {b_id}")
    if os.path.exists(b_img_path):
        st.image(Image.open(b_img_path), caption=broadcast_crop_paths[b_id], use_column_width=True)
    else:
        st.warning(f"Image not found: {b_img_path}")

with col2:
    st.subheader(f"🎥 Tacticam Player {t_id}")
    if os.path.exists(t_img_path):
        st.image(Image.open(t_img_path), caption=tacticam_crop_paths[t_id], use_column_width=True)
    else:
        st.warning(f"Image not found: {t_img_path}")

# === Export CSV ===
if st.button("📤 Export Matches to CSV"):
    import pandas as pd
    df = pd.DataFrame(matched_pairs, columns=["broadcast_player_id", "tacticam_player_id"])
    df.to_csv("matched_pairs.csv", index=False)
    st.success("✅ Exported matched_pairs.csv")

# === Save current match as image ===
if st.button("💾 Save this match as side-by-side image"):
    from PIL import ImageOps

    if os.path.exists(b_img_path) and os.path.exists(t_img_path):
        b_img = Image.open(b_img_path)
        t_img = Image.open(t_img_path)

        # Pad to same size
        h = max(b_img.height, t_img.height)
        b_img = ImageOps.pad(b_img, (300, h))
        t_img = ImageOps.pad(t_img, (300, h))

        side_by_side = Image.new("RGB", (b_img.width + t_img.width, h))
        side_by_side.paste(b_img, (0, 0))
        side_by_side.paste(t_img, (b_img.width, 0))

        os.makedirs("exported_matches", exist_ok=True)
        save_path = f"exported_matches/match_{match_index}.jpg"
        side_by_side.save(save_path)

        st.success(f"✅ Saved to {save_path}")
    else:
        st.warning("❌ One or both images not found. Cannot save.")
