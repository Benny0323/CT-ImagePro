# Common-CT-Images-Processing-Tools

This repository contains a collection of essential tools for processing CT (Computed Tomography) images. The tools are designed for efficient and accurate manipulation of medical imaging data, which is crucial for researchers, radiologists, and anyone working with CT scans. The code within this repository can be utilized for tasks such as converting PNG files to TIF format and generating sinograms for further processing and analysis.

## Key Features:

1. **Png2Tif**: A Python script designed to convert PNG images to the TIF format, which is commonly used for medical images. This conversion is useful for preprocessing images, ensuring compatibility with various CT image analysis tools.
2. **Sinogram_Generation**: This script generates sinograms from CT images, which are essential for image reconstruction in tomography. The tool helps in simulating projections from different angles, a crucial step in the inverse problem of CT imaging.

---

## Tools Overview

### 1. **Png2Tif**

- **Purpose**: This tool is designed to convert CT image files from PNG format to TIF format.
- **Key Functionality**:
  - **Batch Conversion**: It processes multiple images in one go, converting them into a desired format to ensure compatibility with CT image reconstruction tools.
  - **Preserving Image Quality**: The tool ensures no loss of image quality during conversion, maintaining the integrity of the CT scan data.
- **Use Case**: This tool is useful when dealing with image files in PNG format, especially for datasets or individual images that need to be converted into a format compatible with medical imaging software or databases that require TIF files.

### 2. **Sinogram_Generation**

- **Purpose**: This tool is designed to generate sinograms from CT images, a necessary step for CT reconstruction techniques such as filtered back-projection (FBP).
- **Key Functionality**:
  - **Sinogram Simulation**: It simulates CT projections at different angles and generates the corresponding sinogram.
  - **Customization Options**: The tool allows for adjustments in the parameters related to projections, angles, and image resolution, offering flexibility for different types of CT imaging scenarios.
- **Use Case**: This script is vital for anyone involved in CT image reconstruction and tomography, including professionals working with computed tomography systems or developing algorithms for 3D image reconstruction.

---

## Additional Features

- **Flexible Integration**: The tools provided can be integrated into existing workflows for CT image processing and analysis.
- **Comprehensive Support**: The repository supports various medical imaging formats and can be extended for additional features based on specific project requirements.

---

## Contribution Guidelines

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request. Please ensure that your contributions follow the style guidelines, and include tests where necessary. We acknowledge the contributions of the open-source community in developing tools for medical image processing. 
