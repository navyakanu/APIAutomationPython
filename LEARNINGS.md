## API automation in Python

Use pytest as test framework
Use requests for api operations like GET,POST,PUT,DELETE

For serialising and deserialising - use jsonpickle

Convert response from requests to json()
Form expected data in a form of object
Convert object to class<str> using jsonpickle.encode()
then convert class<str> to class<dict> from json.loads()

Assert 2 dictionaries - Hard to find out which element in the dict is incorrect
Assert 2 elements in dict by retrieving each element in the dictionary - lot of attributes to iterate