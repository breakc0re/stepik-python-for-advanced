from string import *

LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))


print(LETTER)