lexerRules = [
    # Number and float
    (r'\d+',             'NUMBER'),
    (r'\d+.+\d',         'FLOAT'),
    # Identifier (Variable, Function, class, object, module, dll)
    (r'[a-zA-Z_]+[\da-zA-Z_0-9]',    'IDENTIFIER'),
    # Mathematical Operators
    (r'\+',              'PLUS'),
    (r'\-',              'MINUS'),
    (r'\*',              'MULTIPLY'),
    (r'\/',              'DIVIDE'),
    (r'\*\*',            'POWER'),
    (r'\%',              'MOD'),
    # Punctuation
    (r'\(',              'LP'),
    (r'\)',              'RP'),
    (r'\[',              'LB'),
    (r'\]',              'RB'),
    (r',',               'COMA'),
    (r':',               'COLON'),
    (r';',               'SEMICOLON'),
    (r'\#.*',            'COMMENT'),

    # Assign value
    (r'=',               'EQUALS'),
    # Comparison operators
    (r'==',              'DOUBLEEQUAL'),
    (r'!=',              'NOT_EQUAL'),
    (r'>',               'GREATER_THAN'),
    (r'<',               'LESS_THAN'),
    (r'>=',              'GREATER_OR_EQUAL_THAN'),
    (r'<=',              'LESS_OR_EQUAL_THAN'),
    # Whitespace and newline
    (r'\s',              'WHITESPACE'),
    (r'\n',              'NEWLINE'),
    # String
    ('\".*\"',           'STRING'),
    ('\'.*\'',           'STRING'),

    # Python keywords yang harus terdaftar
    (r'False',           'FALSE'),
    (r'class\s',         'CLASS'),
    (r'is\s',            'IS'),
    (r'return\s',        'RETURN'),
    (r'None',            'NONE'),
    (r'continue\n',      'CONTINUE'),
    (r'for\s',           'FOR'),
    (r'True',            'TRUE'),
    (r'def\s',           'DEF'),
    (r'from\s',          'FROM'),
    (r'while',           'WHILE'),
    (r'and',             'AND'),
    (r'not',             'NOT'),
    (r'with\s',          'WITH'),
    (r'as\s',            'AS'),
    (r'elif',            'ELIF'),
    (r'elif\(',          'ELIF LP'),
    (r'if\s',            'IF'),
    (r'if\(',            'IF LP'),
    (r'\sor\s',          'OR'),
    (r'else',            'ELSE'),
    (r'import\s',        'IMPORT'),
    (r'pass',            'PASS'),
    (r'break\n',         'BREAK NEWLINE'),
    (r'break\w',         'BREAK ERR'),
    (r'in\s',            'IN'),
    (r'raise\s',         'RAISE'),
    # Tambahan
    (r'print',           'PRINT'),
    # Triple Quote 
    (r'\"\"\"',          'TRIPLEQUOTE'),
    (r'\'\'\'',          'TRIPLEQUOTE'),
]