import random

nomeAluno1 = input('Qual o nome do primeiro aluno: ')
nomeAluno2 = input('Qual o nome do segundo aluno: ')
nomeAluno3 = input('Qual o nome do terceiro aluno: ')

alunosParticipantes = [nomeAluno1, nomeAluno2, nomeAluno3]

random.shuffle(alunosParticipantes)

print("Primeiro aluno a apresentar:", alunosParticipantes[0])
print("Segundo aluno a apresentar:", alunosParticipantes[1])
print("Terceiro aluno a apresentar:", alunosParticipantes[2])



