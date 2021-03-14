"""Frequency Analysis for the Vigénere Cipher."""

from cs6903_project_one.constants import LETTERS, LETTER_COUNT_DICT

def get_item_at_index_zero(items: Any) -> Any:
    """Return the item at the specified index from the iterable.

    Used to sort lists.

    Args:
        items (Any): Iterable of items to parse.

    Returns:
        Any: the item at index one from the iterable
    """
    return items[0]

def get_letter_count(message: str) -> Dict[str, int]:
    for letter in message:
        if letter in LETTERS:
            LETTER_COUNT_DICT[letter] += 1

    return LETTER_COUNT_DICT

def get_frequency_order(message: str) -> str:
    """ Return a string of letters ordered by frequency of occurence in the message.

    Args:
        message (str): The message

    Returns:
        str: The string of letters ordered by frequency
    """
    # Create dictionary with key being letter and value being the frequency count
    letter_count_dict = get_letter_count(message)

    # Create dictionary with key being frequency count and value being letter
    frequency_count_dict = {}
    for letter in LETTERS:
        if letter_count_dict[letter] not in frequency_count_dict:
            frequency_count_dict[letter_count_dict[letter]] = [letter]
        else:
            frequency_count_dict[letter_count_dict[letter]].append(letter)

    # Sort list of letters in reverse "ETAOIN" order and convert into a string
    for frequency in frequency_count_dict:
        frequency_count_dict[frequency].sort(key=ETAOIN.find, reverse=True)
        frequency_count_dict[frequency] = ''.join(frequency_count_dict[frequency])

    # Convert the frequency_count_dict into a tuple and sort
    frequency_tuple = list(frequency_count_dict.items())
    frequency_tuple.sort(key=get_item_at_index_zero, reverse=True)

    # Store letters ordered by frequency into list
    ordered_frequency = []
    for ft in frequency_tuple:
        ordered_frequency.append(ft[1])

    return ''.join(ordered_frequency)

def frequency_match_score(message: str) -> int:
    """ Return an integer score for the number of matches in the letter frequency
    compared to the English letter frequency.

    Args:
        message (str): The message

    Returns:
        int: The string of letters ordered by frequency
    """
    frequency_ordered_string = get_frequency_order(message)

    score = 0
    for common_letter in ETAOIN[:6]:
        if common_letter in frequency_ordered_string[:6]:
            score += 1

    for least_common_letter in ETAOIN[-6:]:
        if least_common_letter in frequnecy_ordered_string[-6:]:
            score += 1

    return score