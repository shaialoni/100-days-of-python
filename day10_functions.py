#format names

def format_name(first_name, last_name):
    """Takes first name and last name and returns in title format"""
    # first_name = first_name.title()
    # last_name = last_name.title()

    return first_name.title() + ' ' + last_name.title()

print(format_name('shai', 'aloni'))