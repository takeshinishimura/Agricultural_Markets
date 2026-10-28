cd /fig

dot -Tsvg ./Graphviz/foodsystem1.gv -o foodsystem1.svg
dot -Tsvg ./Graphviz/foodsystem2.gv -o foodsystem2.svg
dot -Tsvg ./Graphviz/foodsystem3.gv -o foodsystem3.svg
dot -Tsvg ./Graphviz/foodsystem4.gv -o foodsystem4.svg

inkscape --export-filename=foodsystem1.pdf foodsystem1.svg
inkscape --export-filename=foodsystem2.pdf foodsystem2.svg
inkscape --export-filename=foodsystem3.pdf foodsystem3.svg
inkscape --export-filename=foodsystem4.pdf foodsystem4.svg

dot -Tsvg ./Graphviz/transaction1.gv -o transaction1.svg
dot -Tsvg ./Graphviz/transaction1-1.gv -o transaction1-1.svg
dot -Tsvg ./Graphviz/transaction1-2.gv -o transaction1-2.svg
dot -Tsvg ./Graphviz/transaction1-3.gv -o transaction1-3.svg
dot -Tsvg ./Graphviz/transaction1-4.gv -o transaction1-4.svg

inkscape --export-filename=transaction1.pdf transaction1.svg
inkscape --export-filename=transaction1-1.pdf transaction1-1.svg
inkscape --export-filename=transaction1-2.pdf transaction1-2.svg
inkscape --export-filename=transaction1-3.pdf transaction1-3.svg
inkscape --export-filename=transaction1-4.pdf transaction1-4.svg

dot -Tsvg ./Graphviz/transaction_wholesale1.gv -o transaction_wholesale1.svg
dot -Tsvg ./Graphviz/transaction_wholesale2.gv -o transaction_wholesale2.svg
dot -Tsvg ./Graphviz/transaction_wholesale3.gv -o transaction_wholesale3.svg

inkscape --export-filename=transaction_wholesale1.pdf transaction_wholesale1.svg
inkscape --export-filename=transaction_wholesale2.pdf transaction_wholesale2.svg
inkscape --export-filename=transaction_wholesale3.pdf transaction_wholesale3.svg
