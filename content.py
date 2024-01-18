"""
This file contains game content:
3 category word lists,
title and a function that returns
an illustrated score from a score list
"""
spells = [
    "accio", "aguamenti", "alohomora", "aparecium",
    "ascendio", "bombardo", "confundo", "crucio",
    "engorgio", "expelliarmus", "imperio", "incendio",
    "legilimens", "levicorpus", "lumos", "obliviate",
    "protego", "reparo", "riddikulus", "stupefy"
]

beasts = [
    "acromantula", "basilisk", "centaur", "dragon",
    "grindylow", "hippogriff", "merpeople", "phoenix",
    "pixie", "troll", "unicorn", "goblin",
    "boggart", "dementor", "thestral", "bowtruckle",
    "kappa", "flobberworm", "elf"
]

darkArts = [
    "horcrux", "voldemort", "slytherin", "parseltongue",
    "azkaban", "dementor", "mudblood", "umbridge",
    "lestrange", "grindelwald", "sectumsempra", "nagini",
    "crutiatus", "basilisk", "boggart", "riddle", "curse",
    "malfoy", "imperius", "banshee", "grindylow"
]

title = r"""
   *           *                      *        *
         *              *        *         _
   |_|  /\  |O) |O)  \/   |O) / \ _/___/_ |_ |O) *
   | | /--\ | \ | \ _/    |   \_/  |   |  |_ | \
             *          __      *
   *     |_|  /\  |\ | | _  |\/|  /\  |\ |  *
         | | /--\ | \| \__| |  | /--\ | \|
       *            *                           *
    *                           *
"""


def nagini(tries):
    """
    This list takes too much space
    so it is linked to the main file,
    each try is one list element from score list
    """
    score = [
        r"""
             \     /    !
            (O)---(O)     !
             \_____/
                '-----<
               |vv|     /\
                \vv\____\v\
                 \v_v_v_v_v\
        """,
        r"""
            ^     ^     ?
           (O)---(O)  ?
            \_____/
              \vv\
               |vv|     /\
                \vv\____\v\
                 \v_v_v_v_v\
        """,
        r"""
            _     _  z
           (-)---(O)    z
            \_____/    z
              \vv\
               |vv|     /\
                \vv\____\v\
                 \v_v_v_v_v\
        """,
        r"""
            _     _   z
           (-)---(-)     z
            \_____/    z
              \vv\
               |vv|     /\
                \vv\____\v\
                 \v_v_v_v_v\
        """
    ]
    return score[tries]
