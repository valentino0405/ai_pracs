male(valentino).
male(vincent).
male(benjamin).
male(sydney).
male(anthony).
male(caleb).
male(romeo).

female(jessica).
female(jacqueline).
female(elizabeth).
female(suzana).
female(bharti).
female(victoria).

father(vincent, valentino).
father(vincent, jessica).
father(benjamin, vincent).
father(anthony, caleb).
father(benjamin, anthony).
father(benjamin, victoria).
father(sydney, jacqueline).
father(sydney, romeo).

mother(jacqueline, valentino).
mother(jacqueline, jessica).
mother(elizabeth, vincent).
mother(suzana, jacqueline).
mother(suzana, romeo).
mother(elizabeth, anthony).
mother(elizabeth, victoria).
mother(bharti, caleb).

parent(F, M, C) :- father(F, C), mother(M, C).

grandfather(GF, C) :-
    father(GF, F), father(F, C);
    father(GF, M), mother(M, C).

grandmother(GM, C) :-
    mother(GM, P), (father(P, C); mother(P, C)).

siblings(X, Y) :-
    father(F, X), father(F, Y),
    mother(M, X), mother(M, Y),
    X \= Y.

brother(X, Y) :-
    male(X), siblings(X, Y).

sister(X, Y) :-
    female(X), siblings(X, Y).

uncle(U, C) :-
    male(U), siblings(U, P),
    (father(P, C); mother(P, C)).

aunt(A, C) :-
    female(A), siblings(A, P),
    (father(P, C); mother(P, C)).

cousin(X, Y) :-
    (father(P1, X); mother(P1, X)),
    (father(P2, Y); mother(P2, Y)),
    siblings(P1, P2).