"""
Why pay a fortune teller when you can just program your fortune yourself?

Write a function named tell_fortune that:
* takes 3 arguments: job title, partner's name, geographic location.
* returns a fortune of the form: 'You will be a {job_title} in {location} living with {partner}.
"""

def tell_fortune(job_title, location, partner):
    """
    >>> tell_fortune('bball player', 'Spain', 'Shaqira')
    'You will be a bball player in Spain living with Shaqira.'
    >>> tell_fortune('farmer', 'Kansas', 'C3PO')
    'You will be a farmer in Kansas living with C3PO.'
    >>> tell_fortune('Elvis Impersonator', 'Russia', 'Karl the Fog')
    'You will be a Elvis Impersonator in Russia living with Karl the Fog.'
    """
    return f'You will be a {job_title} in {location} living with {partner}.'


print(tell_fortune('bball player', 'Spain', 'Shaqira'))
