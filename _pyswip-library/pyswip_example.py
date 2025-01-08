# $ pip install pyswip

from pyswip import Prolog

Prolog.assertz("father(michael,john)")
Prolog.assertz("father(michael,gina)")

list(Prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]

for soln in Prolog.query("father(X,Y)"):
    print(soln["X"], "is the father of", soln["Y"])

# michael is the father of john
# michael is the father of gina