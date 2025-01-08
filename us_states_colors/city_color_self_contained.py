import pytholog as pl

## new knowledge base object
city_color = pl.KnowledgeBase("city_color")
city_color([
    "different(red, green)",
    "different(red, blue)",
    "different(green, red)", 
    "different(green, blue)",
    "different(blue, red)", 
    "different(blue, green)",
    "coloring(A, M, G, T, F) :- different(M, T),different(M, A),different(A, T),different(A, M),different(A, G),different(A, F),different(G,F),different(G, T)"])

## we will use [0] to return only one answer 
## as prolog will give all possible combinations and answers
answer = city_color.query(pl.Expr("coloring(Alabama, Mississippi, Georgia, Tennessee, Florida)") ) #, cut = True)

print (answer)
