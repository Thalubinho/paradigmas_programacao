pai(fred, marcos). 
pai(ricardo, pedro). 
pai(pedro, paulo). 
pai(ricardo, fred).

% ----------------------------------------------------------------- %
% RULES ----------------------------------------------------------- %
% ----------------------------------------------------------------- %

avo(X,Y) :- pai(X, Z), pai(Z, Y). 
irmao(X,Y) :- pai(Z, X), pai(Z, Y), X \= Y.