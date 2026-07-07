# MiniPydantic

A lightweight data validation framework built from scratch in pure Python using descriptors.

This project is inspired by the core ideas behind modern validation libraries. The goal is to understand how Python's descriptor protocol, object model, and data validation systems work internally.

---

## Overview

MiniPydantic provides a simple model system where classes can define validated fields.

Instead of manually validating every attribute assignment, validation logic is moved into reusable descriptor objects.

Example:

```python
class User(Model):
    name = String()
    age = Integer(min=18)
    balance = Float(default=0)


user = User(
    name="Matin",
    age=20
)

user.balance = 100.5
```

The framework automatically validates and manages the fields.

---

# Features

## Descriptor Based Validation

Each field is implemented using Python descriptors.

Supported operations:

* Custom `__get__`
* Custom `__set__`
* Automatic field name registration using `__set_name__`

---

## Supported Field Types

### Integer

Features:

* Type conversion
* Minimum value validation
* Maximum value validation
* Immutable fields support
* Default values

Example:

```python
age = Integer(
    min=18,
    max=100
)
```

---

### Float

Features:

* Float conversion
* Range validation
* Default values

Example:

```python
balance = Float(
    default=0
)
```

---

### String

Features:

* Automatic string conversion
* Minimum length validation
* Maximum length validation

Example:

```python
username = String(
    min_length=3,
    max_length=20
)
```

---

# Architecture

```
MiniPydantic

│
├── Model
│
│
└── Validation Descriptor
        │
        ├── Number
        │      │
        │      ├── Integer
        │      │
        │      └── Float
        │
        └── String
```

---

# How It Works

When creating a model:

```python
user = User(
    name="Matin",
    age=20
)
```

The process is:

```
Model.__init__()

        ↓

setattr()

        ↓

Descriptor.__set__()

        ↓

Validation

        ↓

Store value inside instance.__dict__
```

---

# Model Features

Every model supports:

## Dictionary conversion

```python
user.to_dict()
```

Output:

```python
{
    "name": "Matin",
    "age": 20,
    "balance": 0
}
```

---

## Representation

```python
print(user)
```

Example:

```
User({'name':'Matin','age':20})
```

---

## Iteration

Models can be iterated:

```python
for key,value in user:
    print(key,value)
```

---

## Comparison

Models can be compared:

```python
user1 == user2
```

Two models are equal when their type and data are identical.

---

# Design Decisions

## Why Descriptors?

Python descriptors are the same mechanism used by many frameworks internally.

They allow:

* Centralized validation logic
* Reusable fields
* Attribute control
* Automatic behavior on assignment

---

## Why Separate Model and Validation?

The Model class manages object behavior.

Validation classes manage data rules.

This separation keeps the architecture clean and extensible.

---

# Example

```python
class User(Model):

    name = String()

    age = Integer(
        min=18
    )

    balance = Float(
        default=0
    )


user = User(
    name="Matin",
    age=20
)


print(user.to_dict())
```

Output:

```python
{
    "name": "Matin",
    "age": 20,
    "balance": 0
}
```

---

# Future Improvements

Planned features:

* Nested models
* List fields
* Better inheritance support
* JSON serialization
* Schema generation
* Custom error system
* Field registry
* More advanced validators

---

# Learning Goals

This project focuses on understanding:

* Python Descriptor Protocol
* Object lifecycle
* Magic methods
* Data modeling patterns
* Validation architecture
* Framework design principles

---

## License

This project is created for educational purposes.
