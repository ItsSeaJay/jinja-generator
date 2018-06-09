import re # Regular Expresssions

# The following function is based on 'The Perfect PHP Clean URL Generator'
# by Matteo Spinelli
# http://cubiq.org/the-perfect-php-clean-url-generator

def generate(input_string):
    delimeter = "_"
    uri = input_string

    # Remove everything that isn't;
    #   - Alphabetic characters A-Z (in both upper and lower case)
    #   - Numeric digits 0-9
    #   - An underscore
    #   - A minus sign
    #   - White space
    uri = re.sub(r"[^a-zA-Z0-9\-_ ]", "", uri)
    # Convert the URI to lower case
    uri = uri.lower()
    # Replace all remaining symbols and whitespace with the delimeter
    uri = re.sub(r"[_ -]", delimeter, uri)

    return uri

# output: plus + slash /
