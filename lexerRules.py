lexerRules = [
    # Triple Quote
    (r'\"\"\"',         'TRIPLEQUOTE'),
    (r'\'\'\'',         'TRIPLEQUOTE'),
    
    # Number and float
    (r'\d+',            'NUMBER'),
    (r'\d+.+\d',        'FLOAT'),  
    # Mathematical Operators
    (r'\+',             'PLUS'),
    (r'\-',             'MINUS'),
    (r'\*\*',           'POWER'),
    (r'\*',             'MULTIPLY'),
    (r'\/',             'DIVIDE'),
    (r'\%',             'MOD'),
    # Punctuation
    (r'\[',             'LB'),
    (r'\]',             'RB'),
    (r'\(',             'LP'),
    (r'\)',             'RP'),
    (r',',              'COMA'),
    (r':',              'COLON'),
    (r';',              'SEMICOLON'),
    (r'\#.*',           'COMMENT'),

    # Comparison operators
    (r'==',             'DOUBLEEQUAL'),
    (r'!=',             'NOT_EQUAL'),
    (r'>',              'GREATER_THAN'),
    (r'<',              'LESS_THAN'),
    (r'>=',             'GREATER_OR_EQUAL_THAN'),
    (r'<=',             'LESS_OR_EQUAL_THAN'),
    
    # Assign value
    (r'=',              'EQUALS'),
    # Whitespace and newline
    (r'\n',             'NEWLINE'),
    (r'\s',             'WHITESPACE'),
    # string
    ('\".*\"',          'STRING'),
    ('\'.*\'',          'STRING'),

    # Python keywords yang harus terdaftar
    (r'False',          'FALSE'),
    (r'class\s',        'CLASS'),
    (r'is\s',           'IS'),
    (r'return\s',       'RETURN'),
    (r'None',           'NONE'),
    (r'continue\n',     'CONTINUE'),
    (r'for\s',          'FOR'),
    (r'True',           'TRUE'),
    (r'def\s',          'DEF'),
    (r'from\s',         'FROM'),
    (r'while',          'WHILE'),
    (r'and',            'AND'),
    (r'not',            'NOT'),
    (r'with\s',         'WITH'),
    (r'as\s',           'AS'),
    (r'elif',           'ELIF'),    
    (r'elif\(',         'ELIF LP'),
    (r'if\s',           ' IF'),
    (r'if\(',           ' IF LP'),
    (r'\sor\s',         'OR'),
    (r'else',           'ELSE'),
    (r'import\s',       'IMPORT'),
    (r'pass',           'PASS'),
    (r'break\n',        'BREAK NEWLINE'),
    (r'break\w',        'BREAK ERR'),
    (r'in\s',           'IN'),
    (r'raise\s',        'RAISE'),
    (r'\.',             'WITH_METHOD'),   
    # Tambahan
    (r'print',           'PRINT'),
    # Identifier (Variable, Function, class, object, module, dll)
    (r'[a-zA-Z_]+[\da-zA-Z_0-9]*','IDENTIFIER'),
    # random case
    (r'\w',             'NULL'),
]