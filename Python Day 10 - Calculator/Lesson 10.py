def format_name(first_name, last_name):
    """Take a first and last name and format it to return title case
    version of it."""
    formated_f_name = first_name.title()
    formated_l_name = last_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("AlEx", "FurtUnA")

def add(n1, n2):
    return n1+n2

my_favorite_operation = add

print(my_favorite_operation(2,3))
#prints out 5