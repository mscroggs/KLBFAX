# FAX
This repository contains Python code to run a CEEFAX style screen.

This branch contains EMFFAX, which will be displayed in the bar at [EMF2018](https://emfcamp.org).

Before running FAX, install the dependencies with:

```shell
pip install -r requirements.txt
```

FAX is launched in a linux or mac terminal with:

```shell
./run.py
```

or

```shell
python3 run.py
```

## Repository contents
The files that make up FAX are organised as follows:

| Directory    | Contents                                   |
| ------------ | ------------------------------------------ |
| `/`          | Config, repository info and main run files |
| `/ceefax`    | The main ceefax class                      |
| `/cupt`      | CuPT, the **Cu**rses **P**rinting **T**ool |
| `/error`     | Error logging functionality                |
| `/files`     | Data files needed by pages                 |
| `/fonts`     | Terminal block fonts                       |
| `/functions` | Functions used by multiple pages           |
| `/helpers`   | Url, tweet and file handling helpers       |
| `/page`      | The `Page` and `PageManager` classes       |
| `/pages`     | The actual pages shown on FAX              |
| `/printer`   | The `Printer` class that print fonts       |
| `/utils`     | Utility functions                          |

## Contributing to EMFFAX
### Adding a Page
The pages are stored in the `pages/` folder. A page file should have the following structure:

```python
from page import Page

class NameOfNewPage(Page):
    def __init__(self, args):
        super(NameOfNewPage, self).__init__(PAGENUMBER)
        pass

    def background(self);
        pass

    def generate_content(self);
        pass

page = NameOfNewPage(args)
```

The function `__init__` will the run when the page if first built. `background` will be run in the background every so often,
and should be used for code that takes a while to run. `generate_content` is run every time the page is loaded.

For a list of current pages, see `PAGES.md`.

### `contributors.txt`
Once you have contributed, add your name to `contributors.txt`, and add a pixel avatar to `pages/777.py`.
