## Order Automation

A desktop application built with Python to automate purchase order recommendations based on stock information exported from an ERP system.

The application allows users to drag and drop a stock Excel file, process it automatically, and generate a new Excel file with an additional column indicating whether each item should be ordered, should not be ordered, or requires manual review.

---

## Features

The application currently performs the following tasks:

* Reads a stock Excel file exported from the ERP.
* Merges both files using the `CODIGO` column.
* Calculates a new column named `pedir`.
* Generates a new Excel file containing the processing results.
* Displays a summary including:

  * Number of items to order.
  * Number of items that do not need to be ordered.
  * Number of items that require manual review.

The decision is based on:

* Item status.
* Available stock.
* Incoming stock.
* Estimated demand.
* Business rules implemented in the application.

---

## Project Structure

```text
ERPAutomatizaciones/
│
├── assets/
│   └── icon.icns
│
└── code/
    ├── app.py
    ├── gui.py
    ├── processor.py
    ├── Configuracion.xlsx
    └── requirements.txt
```

---

## Requirements

* Python 3.14
* PySide6
* pandas
* openpyxl

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Run in Development Mode

From the `code` directory:

```bash
python app.py
```

A desktop window will open, allowing you to drag and drop a stock Excel file for processing.

---

## Build the macOS Application

From the `code` directory:

```bash
pyinstaller \
--name "OrderAutomation" \
--windowed \
--icon ../assets/icon.icns \
app.py
```

The generated application will be located at:

```text
dist/OrderAutomation.app
```

---

## Usage

1. Launch the application.
2. Drag and drop a stock Excel file into the window.
3. Wait for the processing to finish.
4. A new Excel file with the suffix `_Result.xlsx` will be generated in the same directory.
5. A processing summary will be displayed.

---

## Output

The generated Excel file contains all the original data plus an additional column:

| Column  | Description                                                                                     |
| ------- | ----------------------------------------------------------------------------------------------- |
| `pedir` | Indicates whether the item should be ordered, should not be ordered, or requires manual review. |

Possible values:

* `pedir` (Order)
* `no pedir` (Do not order)
* `revisar si pedir` (Review before ordering)
* `datos incompletos` (Incomplete data)

---

## Technologies

* Python
* PySide6
* pandas
* openpyxl
* PyInstaller

---
