def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
  c = None
  while c != 0:
    figurinhas_da_maria = figurinhas_do_joao
    figurinhas_do_joao = c
    return figurinhas_da_maria 

  trocas = int(input())
  for i in range(trocas):
    numeros = [int(num) for num in input().strip().split(' ')]
    print(maximizar_troca_de_figurinhas(numeros[0], numeros[1]))  
    
   
  





if __name__ == '__main__':
  A, B = input().split(' ')
  figurinhas_da_maria = input().split(' ')
  figurinhas_da_joao = input().split(' ')
  maximizar_troca_de_figurinhas(figurinhas_da_maria, 
 figurinhas_da_joao)
