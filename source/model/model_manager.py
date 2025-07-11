from pathlib import Path
from typing import List

import numpy as np
import onnxruntime as ort

from source.utils.folder_util import load_paths
from source.utils.image_util import preprocess_image
from source.utils.math_util import softmax


class ModelManager:
    def __init__(self, extensions: List[str]) -> None:
        self.model_paths: List[Path] = []
        self.ort_session: ort.InferenceSession | None = None
        self._extensions = extensions

    def load_models_from_dir(self, dir_path: str) -> bool:
        self.model_paths = load_paths(dir_path, self._extensions)

        if self.model_paths:
            return True

        self.model_paths = []
        self.ort_session = None

        return False

    def set_active(self, index: int) -> bool:
        if not (0 <= index < len(self.model_paths)):
            return False

        self.ort_session = ort.InferenceSession(self.model_paths[index])

        return True

    def predict(self, image_path: Path) -> np.ndarray | None:
        if not self.ort_session:
            return None

        input_value = preprocess_image(image_path)
        input_name = self.ort_session.get_inputs()[0].name
        output_name = self.ort_session.get_outputs()[0].name

        output = self.ort_session.run([output_name], {input_name: input_value})[0]
        output = np.array(output)[0]

        probs = softmax(output)

        return probs

    @property
    def is_loaded(self) -> bool:
        return self.ort_session is not None

    @property
    def count(self) -> int:
        return len(self.model_paths)

    @property
    def model_names(self) -> List[str]:
        return [path.name for path in self.model_paths]
