# cpExcel

A desktop GUI app for embedding images into Excel files.

## To do
- [] Make a visual placement for manual placement
- [] Better UI 
- [] Add a visual indicator off succesfull/unsuccesfull copy
- [] Test make build
- [] Add mamba/conda/pip env if needed


## Features

- Select individual image files (PNG, JPG, JPEG) or a whole folder
- **Auto mode** — images are inserted sequentially into a `Photos` sheet, one per row
- **Manual mode** — a placement window lets you set the sheet, row, and column for each image individually

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv)

## Installation

```bash
git clone https://github.com/VerebelyPaulloup/cpExcel.git
cd cpExcel
uv sync
```

## Usage

```bash
uv run python main.py
```

1. Choose an input mode: **Fichiers** (individual files) or **Dossier** (folder)
2. Choose a placement mode: **Auto** or **Manuel**
3. Click **Sélectionner les fichiers** to pick your images
4. Click **Lancer la copie** to select the destination `.xlsx` file and start the copy

## Development

```bash
make lint        # ruff lint check
make format      # ruff format check
make typecheck   # mypy
make complexity  # radon + xenon
make test        # pytest
make security    # bandit + pip-audit
make check       # run all of the above
make fix         # auto-fix lint and format issues
make build       # package with pyinstaller
```

## Dependencies

| Package | Purpose |
|---|---|
| `customtkinter` | GUI framework |
| `openpyxl` | Excel read/write |
| `pillow` | Image loading |

## License

See [LICENSE](LICENSE).
