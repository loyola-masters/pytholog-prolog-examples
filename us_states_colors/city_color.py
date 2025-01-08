import pytholog as pl
from prolog_converter import converter

prolog_file = 'city_color.pl'
pytholog_kb = converter.parse_prolog_file(prolog_file)
print(pytholog_kb)

city_color = pl.KnowledgeBase("city_color")
city_color(pytholog_kb)

answer = city_color.query(pl.Expr("coloring(Alabama, Mississippi, Georgia, Tennessee, Florida)"), cut = True)
print(answer)
