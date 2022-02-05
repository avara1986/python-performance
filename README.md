# python-performance

Installation

```shell
pip install poetry
poetry install
```


jupyter nbconvert performance.ipynb --to slides --post serve


ASV:

```
asv run --record-samples main..HEAD
asv publish
asv preview
```