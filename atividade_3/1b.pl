cursa(alessia, pp).
cursa(carol, pp).
cursa(arthur, pp).
cursa(clara_djeovanna, pp).
cursa(eric, pp).
cursa(felipe, pp).
cursa(giovanna, pp).
cursa(guilherme, pp).
cursa(jasmine, pp).
cursa(jp_bandeira, pp).
cursa(jp_dantas, pp).
cursa(israel, pp).
cursa(ronaldo, pp).
cursa(julia, pp).
cursa(lais, pp).
cursa(laryssa, pp).
cursa(lucas, pp).
cursa(lucca, pp).
cursa(ludmila, pp).
cursa(manoel, pp).
cursa(maria_clara, pp).
cursa(pablo, pp).
cursa(sinddy, pp).
cursa(sonally, pp).
cursa(thales, pp).
cursa(vitor, pp).
cursa(werlys, pp).
cursa(alessia, aps).
cursa(arthur, aps).
cursa(clara_djeovanna, aps).
cursa(jasmine, aps).
cursa(ronaldo, aps).
cursa(julia, aps).
cursa(manoel, aps).
cursa(sinddy, aps).
cursa(sonally, aps).
cursa(vitor, aps).
cursa(carol, tec).
cursa(eric, tec).
cursa(felipe, tec).
cursa(jp_bandeira, tec).
cursa(jp_dantas, tec).
cursa(israel, tec).
cursa(laryssa, tec).
cursa(lucas, tec).
cursa(lucca, tec).
cursa(ludmila, tec).
cursa(pablo, tec).
cursa(thales, tec).
cursa(zayon, tec).
cursa(giovanna, tebd).
cursa(guilherme, tebd).
cursa(lais, tebd).
cursa(maria_clara, tebd).
cursa(sinddy, tebd).
cursa(vitor, tebd).
cursa(werlys, tebd).
disciplina_obrigatoria(pp).
disciplina_obrigatoria(aps).
disciplina_eletiva(tec).
disciplina_eletiva(tebd).
leciona(janderson, pp).
leciona(scherer, aps).
leciona(janderson, tec).
leciona(sabrina, tebd).

% ----------------------------------------------------------------- %
% RULES ----------------------------------------------------------- %
% ----------------------------------------------------------------- %

professor_de(X,Y) :- leciona(X, Z), cursa(Y, Z).






