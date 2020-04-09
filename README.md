# lambdata-axel

## installation

```python
pip install -i https://test.pypi.org/simple/ lambdata-axel
```

## usage

import

```python
from lambdata_axel.ds_tools import DSDataFrame
```

Initialize Dataframe

```python
data = {'numbers': [0, 1, 2, 3, 4, 5, 6, 7],
        "alphabet": ['a', 'b', 'c', 'd','e', 'f', 'g', 'h']}
df = DSDataFrame(data)
```

check for nulls in a dataframe

```python
df.check_nulls()
```

create a train, validate, and test set from a dataframe

```python
train, val, test = df.train_val_test_split(random_state=24)
```

## working with Docker environment

Build image from Dockerfile

```shell
docker build . -t lambdata_axel
```

Run image in container and initialize pipenv shell

```shell
docker run -it lambdata_axel pipenv shell
```
