# Immutable JSON Config

A lightweight Python library that loads a JSON configuration file and provides **dot notation access**, **read-only objects**, and **nested attribute traversal**.

## Features

* ✅ Read JSON configuration files.
* ✅ Access nested values using dot notation.
* ✅ Read-only configuration (immutable objects).
* ✅ Supports dictionary and list traversal.
* ✅ Supports numeric or invalid Python identifiers using `_name_` syntax.
* ✅ Implements common Python protocols:

  * `__getitem__`
  * `__iter__`
  * `__contains__`
  * `__len__`
  * `__repr__`
  * `__str__`
  * `__hash__`
  * `__eq__`

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/immutable-json-config.git
```

No external dependencies are required.

---

## Example JSON

```json
{
    "database": {
        "host": "localhost",
        "port": 5432
    },
    "logging": {
        "save_every": [
            {
                "100": true
            }
        ]
    }
}
```

---

## Usage

```python
from config import Config

config = Config("config.json")
```

### Access nested values

```python
print(config.database.host)

print(config.database.port)
```

---

### Access list elements

```python
print(config.logging.save_every[0])
```

---

### Access numeric keys

JSON keys that are not valid Python identifiers can be accessed using surrounding underscores.

```json
{
    "100": true
}
```

```python
print(config._100_)
```

---

### Dictionary-style access

```python
print(config["database"])
print(config.database["host"])
```

---

### Iteration

```python
for key in config:
    print(key)
```

---

### Membership

```python
if "database" in config:
    print("Found")
```

---

### Length

```python
print(len(config))
```

---

## Immutability

Configuration objects are immutable.

The following operations are **not allowed**:

```python
config.database.host = "127.0.0.1"
```

```python
del config.database
```

Both operations raise an `AttributeError`.

---

## Design

The project consists of two classes.

### Config

Responsible for:

* Loading JSON files
* Creating the root configuration object
* Providing the public API

### Item

Responsible for:

* Recursive traversal of nested dictionaries
* List handling
* Immutable access
* Dot notation

---

## Limitations

* Only JSON files are supported.
* Configuration is read-only.
* `__dir__` is currently **not implemented**, so IDE auto-completion for dynamic attributes is limited.
* Hashing may not work correctly if nested mutable JSON values are present.

---

## Future Improvements

* YAML support
* TOML support
* `reload()` method
* Environment variable overrides
* `__dir__` implementation
* Better IDE auto-completion
* Full type annotations
* Cached nested objects for improved performance

---

## License

MIT License
