## Versão simples de um sistema maioritário simples.
## Limitado a três listas e não verifica se há empate entre as listas mais votadas

# As listas e os respetivos votos
lista_A = 123 #votos
lista_B = 456 #votos
lista_C = 567 #votos

if(lista_A > lista_B):
  if(lista_A > lista_C):
    print("A lista vencedora é a lista A")
  else:
    print("A lista vencedora é a lista C")
else:
  if(lista_B > lista_C):
    print("A lista vencedora é a lista B")
  else:
    print("A lista vencedora é a lista C")
