# Python Practice Projects

This repository contains Python projects I built while practicing programming fundamentals.

## Projects

### Calculator
- Basic arithmetic operations
- Input validation
- Division-by-zero handling

### Number Guessing Game
- High/low hints
- Attempt tracking
- Invalid input handling

### Student Grade Manager
- Stores student names and marks
- Sorts students by marks
- Assigns grades
- Calculates average, highest, and lowest marks

### CSV Student Report Manager
- Reads student data from a CSV file
- Uses `csv.DictReader`
- Assigns grades based on marks
- Calculates average, highest, and lowest marks
- Displays the total number of students

### CSV Contact Manager
- Displays saved contacts
- Adds new contacts to a CSV file
- Searches contacts by name
- Uses `csv.DictReader` and `csv.DictWriter`
- Stores contact data persistently in `contacts.csv`

### Password Generator
- Generates random passwords based on user-selected length
- Lets the user choose whether to include symbols
- Guarantees letters and numbers in every password
- Includes at least one symbol when symbols are enabled
- Shuffles characters before displaying the final password
- Validates user input

### File Search Tool
- Searches files by exact filename
- Searches by file extension
- Searches using keywords
- Supports regex-based searching
- Uses the `os` and `re` modules

### API Joke Fetcher
- Fetches a random joke from a public API
- Sends HTTP GET requests using `requests`
- Checks the response status code
- Parses JSON data from the API response
- Displays the joke setup and punchline
## Duck Typing + EAFP Practice

A small Python exercise demonstrating:

- Duck typing
- EAFP (Easier to Ask Forgiveness than Permission)
- `try/except`
- Handling `AttributeError`
- Using the same interface across different classes
### Employee Salary Report
- Stores employee data using `namedtuple`
- Filters employees based on a minimum salary
- Uses a generator with `yield` to produce matching employees
- Uses a decorator to display a report message
- Preserves function metadata with `functools.wraps`
- Handles invalid user input with `try/except`
### Bank Account OOP
- Models bank accounts using Python classes
- Uses properties and setters to validate account balance
- Supports deposits and withdrawals with validation
- Uses inheritance to create a `SavingsAccount`
- Applies interest to savings accounts
- Overrides methods in the child class
- Uses `super()` to reuse parent class behavior
- Implements `__str__` for readable object output


## Skills Practiced

- Loops
- Functions
- Lists and tuples
- Sorting with lambda
- Exception handling
- List comprehensions
- Input validation
- Reading CSV files
- Writing CSV files
- `csv.DictReader`
- `csv.DictWriter`
- Working with external data
- Searching stored records
- Menu-driven programs
- Persistent data storage
- Random password generation
- `random` and `string` modules
- Character set combination
- File system operations with `os`
- Regular expressions with `re`
- Working with APIs
- HTTP GET requests
- `requests` library
- JSON response handling
- Status code checking
- Virtual environments
- Managing dependencies with `requirements.txt`
- Breaking programs into functions
- Duck typing
- EAFP
- `namedtuple`
- Generators and `yield`
- Decorators
- `functools.wraps`
- `*args` and `**kwargs`
- Filtering data with functions
- Object-oriented programming
- Classes and objects
- Inheritance
- `super()`
- Properties and setters
- Method overriding
- `__str__`
- Data validation with exceptions
