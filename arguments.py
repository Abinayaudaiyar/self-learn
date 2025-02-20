# POSITIONAL ARGUMENTS:
# The values passed in the function call will be taken by the arguments positionally
def me(name,age):
    print(f"Name:{name},Age:{age}")
me("Abinaya",21)   #Order must be same

# In the above example ,if we change the order of values passed during function call,we may get unexpected error.
# to overcome this problem ,we use keyword arguments.

# KEYWORD ARGUMENTS:
me(age=21,name="abinaya")

# DEFAULT ARGUMENTS:
# These are the arguments ,that are assigned with a value initially in the function definition.
def you(name="stranger"):
    print(f"you are a {name}")
you()
