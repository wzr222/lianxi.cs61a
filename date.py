'1'
chinese = ['coin','string','myriad']
suites = chinese
suites.pop()
suites.remove('string')
suites.append('cup')
suites.extend(['sword','club'])
suites[2] = 'spade'
'''
Sharing adn Identity
    because we have beenn changing a single list rather than creating new lists,
    the object bound to the name chinese has also changed, because it it the same list 
    object that was bount to suits!
'''
'2'
nest = list(suites)
nest[0] = suites
print(nest,suites)
'''
listes can be copied using the list constructor function.changes to one list don't affect
another, unless they share construct.
https://pythontutor.com/cp/composingprograms.html#code=suits+%3D+%5B'heart',+'diamond',+'spade',+'club'%5D%0Anest+%3D+list(suits)%0Anest%5B0%5D+%3D+suits%0Asuits.insert(2,+'Joker')%0Ajoke+%3D+nest%5B0%5D.pop(2)
'''