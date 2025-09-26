# 1. Introduction to unit testing

Please read the following guidance before you start to write unit test code.

## Unit testing in Python

**Unit testing** is a method of software testing that focuses on the smallest testable parts of a program, known as
**units**, typically individual functions or methods.

The goal of unit testing is to ensure that each part of the code works correctly and as intended, including helper
functions that may not be directly visible to the user.

Other types of testing, such as integration testing, were introduced in the lecture but are not covered in this tutorial
or the coursework. Integration testing will be explored further in COMP0034.

In Python, the built-in [unittest](https://docs.python.org/3/library/unittest.html) module provides basic tools for testing.

This tutorial focuses on [pytest](https://docs.pytest.org/en/stable/getting-started.html), a framework that builds on
unittest. Unlike `unittest`, `pytest` must be installed separately e.g. using `pip install pytest`.

We are using `pytest` here because you will also need it next term in COMP0034.

`pytest` is a testing framework. It provides tools to write and run tests, but it is not limited to unit testing.

Simply using pytest does not automatically make a test a unit test.

A test qualifies as a unit test if it meets the criteria for unit testing:

- It tests a small, isolated piece of code (usually a function or method).
- Each test should be short and focused on one behaviour, condition, or variation.
- Tests should not rely on external dependencies (e.g. databases, APIs). If such dependencies are needed, mocks are
  often used to simulate them.
- Tests should be independent of each other and runnable in any order. 
- Each test should be self-descriptive and easy to understand without needing extra explanation.

So, the type of test depends on what is being tested and how, not on the tool used to write it.

## Patterns for naming and writing tests

There are common patterns for testing. Following these make it easier for you to write and run the test code, and for
others to understand it.

- Test directory structure
- Test class, function and module names
- Patterns that help you to structure the test (**GIVEN–WHEN–THEN** and **ARRANGE–ACT–ASSERT**)

### Test directory structure

There are common patterns for organizing where tests should be placed in a project.

One widely used approach is to place all tests in a separate directory outside the main application code.

This separation helps keep the codebase clean and makes it easier to manage and run tests independently of the
application logic.

The pytest documentation
describes [two typical project layout patterns](https://docs.pytest.org/en/stable/explanation/goodpractices.html#choosing-a-test-layout):

1. Tests placed in directory at the same level as the source code

    ```text
    ├── pyproject.toml
    ├── src/
    │   ├──package/
    │   │   ├── __init__.py
    │   │   ├── my_module.py
    ├── tests/
    │   ├── test_my_module.py
    ```

2. Tests placed within the source code.

    ```text
    ├── pyproject.toml
    ├── src/
    │   ├── package/
    │   │   ├── __init__.py
    │   │   ├── my_module.py
    │   ├── tests/
    │   │   ├── __init__.py
    │   │   ├── test_my_module.py
    ```

The course activities all follow the first of these as it separates the packaging of the application code from the code
that tests it.

### Test naming

Packages such as pytest will detect test files that follow certain naming patterns.

The directory containing the tests is usually named 'tests' or 'test'.

The test modules file names are prefixed with `test_` such as `test_module.py` or suffixed with `_test` such as
`module_test.py`.

The test file name typically also refers to the module, package or feature being tested; though this does not affect
auto discovery of tests.

The tests cases within the modules may be written as classes or functions. The naming convention should make it clear
what they test, e.g. `class TestMyPackage` is a class containing test cases for the MyPackage package.
`test_redirect_success` tests that a call to a given url successfully redirects.

In general, you should have a pretty good idea what the test is testing for from its name. Given this, test names such
as `test_function_a_1`, `test_function_a_2` etc. are not considered a good style, while they relate to 'function a',
it is not clear what 1 and 2 refer to.

The way that Pytest discovers names
is [documented here](https://docs.pytest.org/en/stable/explanation/goodpractices.html#conventions-for-python-test-discovery).

### GIVEN-WHEN-THEN pattern

The **GIVEN–WHEN–THEN** pattern is a helpful way to think about the behaviour you want to test.

This pattern comes from an approach called Behaviour-Driven Development (BDD). You may come across guides that use
the[Gherkin](https://cucumber.io/docs/gherkin/) syntax to express this pattern.
You do not need to learn Gherkin syntax to use the GIVEN–WHEN–THEN structure effectively.

Here's an example:

```text
Test Scenario: Simple Google search
    Given the Google home page is displayed
    When the user searches for "Python pandas"
    Then the results page shows links related to "Python pandas"
```

In this course, I often use this pattern in test case documentation or docstrings to describe what the test is doing.

These elements also influence the structure of the test code, which is explained in the next section.

For a more detailed example, see [Pytest with eric](https://pytest-with-eric.com/bdd/pytest-bdd/).

### ARRANGE-ACT-ASSERT pattern

The **ARRANGE–ACT–ASSERT** pattern is a common structure for writing unit tests, and is referenced in the pytest
documentation.

It aligns closely with the **GIVEN–WHEN–THEN** pattern:

- Arrange ≈ Given
- Act ≈ When
- Assert ≈ Then

This pattern helps structure your test code clearly:

1. **Arrange**: Set up everything the test needs before running

   Examples: initialise objects, create test data, mock external services such as login to a web app.
2. **Act**: Perform the action being tested.

   For example: call a function.
3. **Assert**: Check that the result matches expectations. Assertions determine if the test passes or fails.

   This could be a simple value check or a more complex validation.

Here's an example using [Python's built-in absolute value function](https://www.w3schools.com/python/ref_func_abs.asp):

```python
def test_abs_for_a_negative_number():
    # Arrange: define a negative number to be tests
    negative = -6

    # Act: call the function to be tested and pass the negative number
    answer = abs(negative)

    # Assert: use a pytest assertion, in this case the 'correct' behaviour from the function 
    # when called on -6 is to return 6
    assert answer == 6
```

[Next activity](9-02-pytest-tests.md)