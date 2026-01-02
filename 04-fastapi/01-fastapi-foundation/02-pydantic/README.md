### What is Pydantic?


#### Why Pydantic?
- To handle the type of the data.
- To validate the data

Let's consider this example:
```
def insert_data(name, age):
    print(name)
    print(age)
    print("Data Inserted")


insert_data()
```
- In this there is no validation of the data and user can enter of any type because python is a dynamic programming language. 

Now one of the way to resolve this situation
```
def insert_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be negative") #here we resolve another issue manually

            print(name)
            print(age)
            print("Data Inserted")
    else:
        raise TypeError("Incorrect DataType")

insert_data("moiz", 22)
```
So it solves the issue but again this not the optimized or correct way to do it, what if I want to update the data so we write again the same logic to my other function, Like this

```
def insert_data(name: str, age: int):
    if type(name) == str and type(age) == int:

        print(name)
        print(age)
        print("Data Inserted")
    else:
        raise TypeError("Incorrect DataType)

insert_data("moiz", 22)


def update_data(name: str, age: int):
    if type(name) == str and type(age) == int:

        print(name)
        print(age)
        print("Updated Data")
    else:
        raise TypeError("Incorrect DataType)

update_data()
```
Here you see this, that's why we use pydantic.

### How to use Pydantic?

1. Define a pydantic model(class) that represents the ideal schema of the data
    - This includes the expected fields, their types, and any validation constraints (e.g., gt = 0 for positive numbers)

2. Instantiate the model with raw input data (usually a dictionary or JSON-like structure).
    - Pydantic will automatically validate the data and coerce it into the correct python types (if possible).
    - If the data doesn't meet the model's requirements, pydantic raises a ValidationError.

3. Pass the validated model object to functions or use it throughout our codebase.
    - This ensures that every part of our program works with clean, type-safe, and logically valid data.

Pydantic not only do data/type validation it is smart enough that if you provide "22" in a string format it automatically converts it into integer.