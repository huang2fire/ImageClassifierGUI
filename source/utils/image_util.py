from pathlib import Path

import numpy as np
from PIL import Image


def preprocess_image(img_path: Path) -> np.ndarray:
    with Image.open(img_path) as img:
        # 1. ToImage
        img = img.convert("RGB")

        # 2. Resize
        img = img.resize((256, 256), Image.Resampling.BILINEAR)

        # 3. CenterCrop
        img = img.crop((16, 16, 240, 240))

        # 4. ToTensor
        img_np = np.array(img) / 255.0
        img_np = img_np.transpose((2, 0, 1))

        # 5. Normalize
        mean = np.array([0.485, 0.456, 0.406]).reshape(3, 1, 1)
        std = np.array([0.229, 0.224, 0.225]).reshape(3, 1, 1)
        img_np = (img_np - mean) / std

        # 6. ToBatch
        img_np = np.expand_dims(img_np, axis=0).astype(np.float32)

        return img_np
