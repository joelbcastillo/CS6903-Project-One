"""Constants for Cipher Analysis CLI."""

import re

NUM_MOST_FREQ_LETTERS = 10
MAX_KEY_LENGTH = 24
DICTIONARY_LETTER_FREQUENCY_TEST_ONE = "eisraontlcdugmphybfvzkwjxq"
DICTIONARY_LETTER_FREQUENCY_TEST_TWO = "esirotnclaupdmhbywfvgzkxqj"
MESSAGE_SPACE = " abcdefghijklmnopqrstuvwxyz"
CIPHERTEXT_SPACE = MESSAGE_SPACE
KEY_SPACE = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
]

VALID_CHARACTERS_PATTERN = re.compile("[^ A-Z]")

PLAINTEXT_DICTIONARY_ONE = [
    "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch",
    "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago",
    "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci",
    "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s",
    "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis",
]

PLAINTEXT_DICTIONARY_TWO = [
    "awesomeness",
    "hearkened",
    "aloneness",
    "beheld",
    "courtship",
    "swoops",
    "memphis",
    "attentional",
    "pintsized",
    "rustics",
    "hermeneutics",
    "dismissive",
    "delimiting",
    "proposes",
    "between",
    "postilion",
    "repress",
    "racecourse",
    "matures",
    "directions",
    "pressed",
    "miserabilia",
    "indelicacy",
    "faultlessly",
    "chuted",
    "shorelines",
    "irony",
    "intuitiveness",
    "cadgy",
    "ferries",
    "catcher",
    "wobbly",
    "protruded",
    "combusting",
    "unconvertible",
    "successors",
    "footfalls",
    "bursary",
    "myrtle",
    "photocompose",
]

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTER_COUNT_DICT = {
    " ": 0,
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
}
