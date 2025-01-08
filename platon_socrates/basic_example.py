# $ pip install pytholog # Desde un terminal de Anaconda

import pytholog as pl
# Crear la base de conocimientos
base_conocimientos = pl.KnowledgeBase("base_conocimientos")
# Definir hechos
base_conocimientos([
"hombre(socrates)",
"mortal(X) :- hombre(X)"
])
# Consultar
print( '¿Es Sócrates un hombre?', base_conocimientos.query(pl.Expr("mortal(socrates)")) ) # Output: True
print( '¿Es Platón mortal?', base_conocimientos.query(pl.Expr("mortal(platon))")) ) # Output: False
