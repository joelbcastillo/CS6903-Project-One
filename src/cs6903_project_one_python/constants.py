"""Constants for Cipher Analysis CLI."""

import re

MESSAGE_SPACE = " abcdefghijklmnopqrstuvwxyz"
CIPHERTEXT_SPACE = MESSAGE_SPACE
KEY_SPACE = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]

VALID_CHARACTERS_PATTERN = re.compile('[^\sA-Z]')
