<div align="center">

<img width="128" height="128" src="./assets/icon.png">

<h1 align="center">ImageClassifierGUI</h1>

Image classification desktop application based on PySide6 and ONNX Runtime

**English** | [简体中文](README.md)

</div>

## Preview

![Preview](./assets/screenshot.png)

## Features

- MVC architecture
- No torch dependency
- Supports batch import of image files and model files
- Supports visualization of classification results
- Status bar support

## Quick Start

### 1. Clone

```bash
git clone https://github.com/huang2fire/ImageClassifierGUI.git
```

### 2. Environment

It is recommended to use [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
cd ImageClassifierGUI
uv sync
```

### 3. Run

```bash
uv run main.py
```

## Usage Guide

The application configuration file is located at [`config/app.toml`](config/app.toml), where you can customize UI style, font, and other parameters.

The content format of the JSON file for category label supported by the application is as follows

```json
{
    "0": "Class 0",
    "1": "Class 1",
    "2": "Class 2",
    "3": "Class 3",
    "4": "Class 4"
}
```

The image file formats supported by the application can be defined in the configuration file:

```toml
[load]
image_extensions = ["*.bmp", "*.jpg", "*.jpeg", "*.png", "*.tif", "*.tiff"]
```

The application only supports model files in ONNX format.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
