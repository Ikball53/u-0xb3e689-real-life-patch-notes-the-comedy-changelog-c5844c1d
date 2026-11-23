# Real-Life Patch Notes entry — writes one changelog line to /output/entry.txt
from pathlib import Path

patch_note = "v3.7.0 — Fixed: tongue no longer bites itself after 30 years of chewing practice. Known issue: pinky toe still finds every table leg in the dark."

out_path = Path("/output/entry.txt")
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(patch_note + "\n", encoding="utf-8")
