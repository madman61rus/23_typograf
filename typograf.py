import re

def do_typograf(text):

    patterns = [
        # replace single and double quotes
        (re.compile(r'''("|')(.+)\1''', re.DOTALL), r'«\2»'),
        # replace hyphen to short dash between numbers
        (re.compile(r'(\d+)‐(\d+)'), r'\1 – \2'),
        # replace simple hyphen to non breaking hyphen between number and word
        (re.compile(r'(\d+)‐(\w+)'), r'\1&#8209;\2'),
        # remove extra spaces and extra new lines
        (re.compile(r'(\r\n|\n|\s){1}\1+'), r'\1'),
        # add non-breaking space between
        (re.compile(r'(\w{1,2}) (\w{3,})'), r'\1&nbsp;\2'),
        # replace hyphen to dash between spaces
        (re.compile(r'\s-\s'), r' ‒ '),
        #replace spaces
        (re.compile(r'/\s\s+/g'),r' '),
    ]

    for pattern, replacement in patterns:
        result_text = re.sub(pattern,replacement, text)

    return result_text