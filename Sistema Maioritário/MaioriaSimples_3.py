listas={'listaA':123,'listaB':456,'listaC':345}
maximo=max(listas.values())
soma_votos=sum(listas.values())
lst_vencedores=(x for x in listas if(listas[x]==maximo))
print(lst_vencedores)
vencedor=next(lst_vencedores)
n_votos=listas[vencedor]
print("Ganhou o candidato %s com %.2f %%" % (vencedor,n_votos*100/soma_votos))
