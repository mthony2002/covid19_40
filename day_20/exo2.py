names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")

clean = [ e.title() for e in [ *filter(lambda elem: len(elem) < 8 , names)]]

print(clean)