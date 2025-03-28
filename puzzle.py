from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is a knight or a knave but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # If A is a knight his sentence is true:
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a knave his sentence is false:
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A and B can only be a knave or a knight, not both
    And(Or(AKnave, AKnight), Not(And(AKnight, AKnave))),
    And(Or(BKnave, BKnight), Not(And(BKnight, BKnave))),
    # If A is a knight, both are knaves (impossible)
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a knave then B can't be a knave
    Implication(AKnave, And(AKnave, BKnight))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A and B can only be a knave or a knight, not both
    And(Or(AKnave, AKnight), Not(And(AKnight, AKnave))),
    And(Or(BKnave, BKnight), Not(And(BKnight, BKnave))),
    # If A is a knight, both are
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a knave, statement needs to be false
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # If B is a knight, different
    Implication(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave))),
    # If B is a knave, lies
    Implication(BKnave, Not(Or(And(AKnave, BKnight), And(AKnight, BKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A, B, C can only be a knave or a knight, not both
    And(Or(AKnave, AKnight), Not(And(AKnight, AKnave))),
    And(Or(BKnave, BKnight), Not(And(BKnight, BKnave))),
    And(Or(CKnave, CKnight), Not(And(CKnight, CKnave))),
    # If B is a knight, C is a knave
    Implication(BKnight, CKnave),
    # If B is a knave then C is a knight
    Implication(BKnave, CKnight),
    # If C is a knight, then A is a Knight
    Implication(CKnight, AKnight),
    # If C is a knave, then A is a knave
    Implication(CKnave, AKnave),
    # If B is a knight, A is a knave
    Implication(BKnight, AKnave),
    # If B is a knave then message is a lie
    Implication(BKnave, AKnight),
    # A can be a knight or a knave
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
