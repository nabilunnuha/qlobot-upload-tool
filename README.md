# Qlobot-upload-tool

## Overview
tool to speed up manual to automatic qlobot uploads.

## Requirements
- [httpx](https://pypi.org/project/httpx/)
- [colorama](https://pypi.org/project/colorama/)
- [pydantic](https://pypi.org/project/pydantic/)

## How to Run

1. **Activate Virtual Environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

2. **Install Required Modules:**
    ```bash
    pip install -r requirements.txt
    ```
    
3. **Run the convert pdc collections to qlobot csv:**
    ```bash
    python shopee_upload.py
    ```
    ```bash
    python tokopedia_upload.py
    ```
    ```bash
    python refresh_via_delete.py
    ```

## Package Information

- **Author:** [Nabilunnuha](https://github.com/nabilunnuha)

## Notes
- Ensure that you have Python installed on your system before running the commands.
- The virtual environment is recommended for managing dependencies and preventing conflicts with other projects.
