'''
ALGORITMO SIMPLIFICA(C)
Entrada: Um conjunto C de cláusulas (quaisquer)
Saída: Um conjunto de cláusula C', C'≡ C, sem cláusulas unitárias.
C' := C
enquanto Existe uma cláusula unitária u ∈ C faça
    C' := C' - {c|u é literal em c}
    para toda cláusula c = ¬u V c' faça
        C' := C' U {c'} - c
    fim para
fim enquanto
retorne C'
'''

'''
ALGORITMO 2SAT
Entrada: Um conjunto C de 2-cláusulas
Saída: verdadeiro se C é satisfazível, ou falso, caso contrário.
C := Simplifica(C)
enquanto ⊥ ~∈~ C e C ~=~ ∅ faça          obs: ⊥ = { }, vazio
    Escolha um átomo p qualquer em C
    C' := Simplifica(C U {p})
    se ⊥ ∈ C' então
        C := Simplifica(C U {¬p})
    senão
        C := C'
    fim se
fim enquanto

se ⊥ ∈ C então
    retorne falso
senão
    retorne verdadeiro
fim se
'''