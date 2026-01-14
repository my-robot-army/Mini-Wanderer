## Getting started

- Install it with:

```bash
conda create -n dora_env python=3.11
conda activate dora_env
```

```bash
uv venv -p 3.11 --seed
uv pip install -e .
```

then

```bash
pip install -r requirements.txt
```

- Run it with:

```bash
dora run dataflow.yml
```

or

```bash
conda run -n dora_env dora build dataflow.yml
conda run -n dora_env dora run dataflow.yml
```

```bash
uv pip install ruff
uv run ruff check . --fix
```

## Contribution Guide

- Format with [ruff](https://docs.astral.sh/ruff/):

```bash
pip install ruff
ruff check . --fix
```

- Lint with ruff:

```bash
ruff check .
```

- Test with [pytest](https://github.com/pytest-dev/pytest)

```bash
pip install pytest
pytest . # Test
```

## YAML Specification

## Examples

## License

Node Name's code are released under the MIT License
