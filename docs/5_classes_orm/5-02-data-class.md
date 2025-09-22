# 2. Python data class

A Python data class is a special type of class introduced in Python 3.7 with the `@dataclass` decorator that makes it
easier to create classes that are mainly used to store data. Data classes automatically generate common methods such as
`__init__` and `__repr__` for you.

In the last activity you created an Athlete class with a string method.

This could have been created as a data class, for example:

```python
from dataclasses import dataclass


@dataclass
class Athlete:
    first_name: str
    last_name: str
    team_code: str
    disability_class: str
```

You could then create and print an instance like this:

```python
athlete1 = Athlete(
    first_name="Wei",
    last_name="Wang",
    team_code="CHN",
    disability_class="T54"
)
print(athlete1)
```

Methods can be also added to a dataclass even though none are shown in this example.

## Activity: create a Medal class

1. Create a medal data class. A medal has the attributes: 
    - type (str) e.g. gold, silver, bronze
    - designer (str) - each Paralmpics has its own medal design, this is the name of the designer
    - date_designed (date) - date that the medal was designed

[Next activity](5-03-inheritance-composition.md)