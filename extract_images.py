import json
import base64
import os

nb = json.load(open('UTS_Data_Science_Kendaraan.ipynb', encoding='utf-8'))

os.makedirs('images', exist_ok=True)

img_count = 0
for i, c in enumerate(nb['cells']):
    for j, out in enumerate(c.get('outputs', [])):
        if out.get('output_type') == 'display_data':
            data = out.get('data', {})
            if 'image/png' in data:
                img_data = base64.b64decode(data['image/png'])
                filename = f"images/cell_{i}_out_{j}.png"
                with open(filename, 'wb') as img_f:
                    img_f.write(img_data)
                img_count += 1
                print(f"Saved {filename} ({len(img_data)} bytes) from cell {i}")

print(f"Total images saved: {img_count}")
