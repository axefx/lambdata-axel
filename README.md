# lambdata-axel

## installation

```python
pip install -i https://test.pypi.org/simple/ lambdata-axel
```

## usage

import

```python
from lambdata_axel.ds_tools import DSDataFrameTools
```

check for nulls in a dataframe

```python
DSDataFrameTools(df).check_nulls_df()
```

create a train, validate, and test set from a dataframe

```python
train, val, test = DSDataFrameTools(df).train_val_test_split(random_state=24)
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
