# AirBnB clone - The console

The AirBnB clone is part of the Holberton School learning program.
During this project, we have learned some concepts listed below:

-   How to create a Python package
-   How to create a command interpreter in Python using the `cmd` module
-   What is Unit testing and how to implement it in a large project
-   How to serialize and deserialize a Class
-   How to write and read a JSON file
-   How to manage `datetime`
-   What is an `UUID`
-   What is `*args` and how to use it
-   What is `**kwargs` and how to use it
-   How to handle named arguments in a function

## Description
 
The goal of this project is to write a command interpreter to manage the AirBnB objects that we will use later in the project.  
We use the parent class BaseModel to create every instance of every classes that we will use.  

### Why and how to use the console ? 
To execute the console, type `./console`.  
We use the console to easily manipulate our objects.  
We defined a few methods to do that :  

#### do_create : 
Creates an instance of an object using `"create <class name>"` and stores it in a json file, then prints the id of the created object. 

Example :  
```
$ create BaseModel  
$ de2f7b22-a5bf-4132-80b0-d365d495dd27
```

#### do_show : 
Prints the string representation defined in the __str__ function of an object using `"show <class name> <id>"`  

Example :  
```
$ show BaseModel de2f7b22-a5bf-4132-80b0-d365d495dd27  
$ [BaseModel] (de2f7b22-a5bf-4132-80b0-d365d495dd27) {'id': 'de2f7b22-a5bf-4132-80b0-d365d495dd27', 'created_at': datetime.datetime(2023, 2, 23, 1, 19, 1, 714103), 'updated_at': datetime.datetime(2023, 2, 23, 1, 19, 1, 714133)}
```

#### do_destroy : 
Deletes an object using `"destroy <class name> <id>"` 

Example :  
```
$ destroy BaseModel de2f7b22-a5bf-4132-80b0-d365d495dd27  
$  
```

#### do_all :
Prints all string representations of all objects created, using either `all` or `all <class name>` to display only instances of BaseModel  

Example :
```
$ create BaseModel  
$ 63507666-8f75-4d28-b4c9-20fd5e67466c  
$ create User  
$ 3fa79693-c6ee-4416-9e34-c5328ecb0c00  
$ create BaseModel  
$ 87090431-8aa1-424f-a2ea-18abacb670c3 
```

```
$ all  
$ ["[BaseModel] (63507666-8f75-4d28-b4c9-20fd5e67466c) {'id': '63507666-8f75-4d28-b4c9-20fd5e67466c', 'created_at': datetime.datetime(2023, 2, 23, 1, 30, 26, 603266), 'updated_at': datetime.datetime(2023, 2, 23, 1, 30, 26, 603298)}", "[User] (3fa79693-c6ee-4416-9e34-c5328ecb0c00) {'id': '3fa79693-c6ee-4416-9e34-c5328ecb0c00', 'created_at': datetime.datetime(2023, 2, 23, 1, 30, 55, 4429), 'updated_at': datetime.datetime(2023, 2, 23, 1, 30, 55, 4444)}", "[BaseModel] (87090431-8aa1-424f-a2ea-18abacb670c3) {'id': '87090431-8aa1-424f-a2ea-18abacb670c3', 'created_at': datetime.datetime(2023, 2, 23, 1, 31, 12, 731361), 'updated_at': datetime.datetime(2023, 2, 23, 1, 31, 12, 731375)}"]  
```

```
$ all BaseModel  
$ ["[BaseModel] (63507666-8f75-4d28-b4c9-20fd5e67466c) {'id': '63507666-8f75-4d28-b4c9-20fd5e67466c', 'created_at': datetime.datetime(2023, 2, 23, 1, 30, 26, 603266), 'updated_at': datetime.datetime(2023, 2, 23, 1, 30, 26, 603298)}", "[BaseModel] (87090431-8aa1-424f-a2ea-18abacb670c3) {'id': '87090431-8aa1-424f-a2ea-18abacb670c3', 'created_at': datetime.datetime(2023, 2, 23, 1, 31, 12, 731361), 'updated_at': datetime.datetime(2023, 2, 23, 1, 31, 12, 731375)}"]  
```
 
#### do_update : 
Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) using `"update <class name> <id> <attribute> <new value>`  

Example :  
```
$ update User 3fa79693-c6ee-4416-9e34-c5328ecb0c00 first_name "Leo"  
$ show User 3fa79693-c6ee-4416-9e34-c5328ecb0c00  
$ [User] (3fa79693-c6ee-4416-9e34-c5328ecb0c00) {'id': '3fa79693-c6ee-4416-9e34-c5328ecb0c00', 'created_at': datetime.datetime(2023, 2, 23, 1, 30, 55, 4429), 'updated_at': datetime.datetime(2023, 2, 23, 1, 30, 55, 4444), 'first_name': '"Leo"'
```

You can type `help` to see all commands available, and `help <command>` to see a description of the specified command.  
Then to exit the console, you can either type `quit` or use `Ctrl+D`

## Testing

All tests files are inside a folder `tests`.

There are three ways to excecute tests:
- Test all files:
```
python3 -m unittest discover tests
```

- Test all files in non-interactive mode:
```
echo "python3 -m unittest discover tests" | bash
```

- Test file by file:
```
python3 -m unittest tests/test_models/test_base_model.py
```

## Authors

-   Marc-Antoine Vannier <[Marcantoine4581](https://github.com/Marcantoine4581)>
-   Thomas Borde <[thomasborde94](https://github.com/thomasborde94)>
