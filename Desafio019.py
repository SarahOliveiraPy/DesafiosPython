import random

nomeAluno = input('Qual o nome do primeiro aluno: ')
nomeAluno2 = input('Qual o nome do segundo aluno: ')
nomeAluno3 = input('Qual o nome do terceiro aluno: ')

alunosParticipantes = [nomeAluno, nomeAluno2, nomeAluno3]

sorteio = random.choice(alunosParticipantes)
print("O nome sorteado é:", sorteio)
