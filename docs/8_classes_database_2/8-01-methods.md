from activities.starter.starter_class import ParalympicEvent

# Activity 1: Adding methods to classes

## Python classes

A method is a function defined inside a class that operates on instances of that class (objects). It usually takes self
as its first parameter, which refers to the instance calling the method.

You can add as many methods as you like.

An example of a method (`register_athlete`):

```python
class ParalympicEvent:
    def __init__(self, name, sport, classification):
        self.name = name
        self.sport = sport
        self.athletes = []

    def register_athlete(self, athlete_name):
        """ Register the athlete with the event

        Args:
            athlete_name: A string representing the name of the athlete
        """
        self.athletes.append(athlete_name)
```

To use the method on an instance of the class:

```python
ev = ParalympicEvent(name="Boccia Pairs", sport="Boccia", classification="BC4")
ev.register_athlete(athlete_name="Alison Levine")
```

### Static and class methods

#### Class methods

Class methods are used to access or modify class-level data.

Class methods start with the decorator `@classmethod`.

Their first parameter is `cls`. This refers to the class itself.

For example:

```python
class ParalympicEvent:
    def __init__(self, name, sport, classification):
        self.name = name
        self.sport = sport
        self.classification = classification
        self.athletes = []

    @classmethod
    def from_dict(cls, data):
        """Creates an event from a dictionary"""
        return cls(data['name'], data['sport'], data['classification'])
```

#### Static methods

Static methods are utility functions that don't need access to class or instance data.

They use the decorator `@staticmethod`.

They do not require either `self` or `cls` as a parameter.

For example:

```python
class ParalympicEvent:
    def __init__(self, name, sport, classification):
        self.name = name
        self.sport = sport
        self.classification = classification
        self.athletes = []

    @staticmethod
    def is_valid_classification(classification):
        """Checks if the classification is within a valid range"""
        return 1 <= classification <= 10
```

### Dunder, double underscore, methods

Dunder methods are special methods in Python that begin and end with double underscores ```__`. They let you define how
your objects behave with built-in Python operations like printing, addition, iteration, and more.

Common dunder methods and their uses

- `__init__`  Object initialization `obj = MyClass()`
- `__str__`  String representation (for print)    `print(obj)`
- `__repr__`  Official string representation `repr(obj)`
- `__len__`  Length of object `len(obj)`
- `__getitem__`  Indexing `obj[key]`
- `__setitem__`  Item assignment `obj[key] = value`
- `__eq__, __lt__,`  Comparisons (==, , etc.)    `obj1 == obj2`
- `__iter__, __next__`  Iteration `for x in obj:`
  `__call__`  Callable objects `obj()`
  `__enter__, __exit__`  Context managers (with)    `with obj:`

You saw examples of the `__init__`  in week 5. You may have spotted examples of `__str__` or `__repr__` too where custom
code has been used to override the default implementation.

For example:

```python
class ParalympicEvent:
    """ Represents a Paralympic event """

    def __init__(self, name, sport, classification):
        self.name = name
        self.sport = sport
        self.classification = classification
        self.athletes = []

    def __str__(self):
        """User-friendly string representation"""
        return f"{self.name} ({self.sport}, Class {self.classification}) with {len(self.athletes)} athlete(s)"

    def __repr__(self):
        """Unambiguous representation for debugging"""
        return (f"ParalympicEvent(name='{self.name}', sport={self.sport}, "
                f"classification={self.classification}, athletes={self.athletes})")
```

To use:

```python
ev = ParalympicEvent(name="Boccia Pairs", sport="Boccia", classification="BC4")
ev.register_athlete(athlete_name="Alison Levine")
repr(ev)
print(ev)
```

## SQLModel classes
The SQLModel tutorial only shows models with attributes. In most cases SQLModel is being used to map to database tables.

However, this is still a Python class so all the above method types can be applied.

When you inherit SQLModel in the class, you inherit its methods:

SQLModel inherits from Pydantic's BaseModel giving:
- `.dict()` – Convert model to dictionary
- `.json()` – Convert model to JSON string
- `.parse_obj()` – Create model from a dictionary
- `.copy()` – Create a copy of the model
- `.validate()` – Validate data against the model

## Activity: Add a method to a class in week 3

1. Open one of your SQLModel `models.py` classes from week 5.
2. Try adding a `__repr__` and a method of your choice to the class.
3. Create an instance of the class then call the methods on that object.

[Next activity](8-02-insert.md)