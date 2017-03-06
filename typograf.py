import re

def do_typograf(text):

    patterns = [
        # replace single and double quotes
        (re.compile(r"""(['"])(.*)(\1)"""), r'«\2»'),
        # replace hyphen to short dash between numbers
        (re.compile(r'(\d+)‐(\d+)'), r'\1 – \2'),
        # replace hyphen on dash after punctuation
        (re.compile(r'(\.{3}\s*|[!?\.,]\s*|^\s*)(-)'), r'\1—'),
        # replace hyphen on dash between two words
        (re.compile(r'([\w]\s+)(-)(\s+[\w])'), r'\1—\3'),
        # replace simple hyphen to non breaking hyphen between number and word
        (re.compile(r'(\d+)‐(\w+)'), r'\1&#8209;\2'),
        # remove extra spaces
        (re.compile(r'([\s])\1+'), r'\1'),
        # replace hyphen to dash between spaces
        (re.compile(r'\s-\s'), r' ‒ '),
        # remove spaces and line breaks
        (re.compile(r'([\s])\1+'), r'\1'),
    ]

    for pattern, replacement in patterns:
        text = re.sub(pattern,replacement, text)

    return text