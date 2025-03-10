"""
Write a function named assign_grade that:
* takes 1 argument, an integer representing the score.
* returns a grade for the score, either "A" (90-100), "B" (80-89), "C" (70-79), "D" (65-69), or "F" (0-64).

Call that function for a few different scores and log the result to make sure it works.
"""
def assign_grade(grade):
    """
    >>> assign_grade(95)
    'A'
    >>> assign_grade(90)
    'A'
    >>> assign_grade(85)
    'B'
    >>> assign_grade(80)
    'B'
    >>> assign_grade(77)
    'C'
    >>> assign_grade(70)
    'C'
    >>> assign_grade(68)
    'D'
    >>> assign_grade(65)
    'D'
    >>> assign_grade(64)
    'F'
    >>> assign_grade(0)
    'F'
    """
    if grade>=90 and grade<=100:
        return "A"
    elif grade>=80 and grade<=89:
        return "B"
    elif grade>=70 and grade<=79:
        return "C"
    elif grade>=65 and grade<=69:
        return "D"
    elif grade>=0 and grade<=64:
        return "F"
print(assign_grade(90))
