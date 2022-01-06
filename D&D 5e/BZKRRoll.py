import random
import time
cd=int(input('Digite a CD do teste: '))
mod=int(input('Digite o valor da rolagem: +'))
modano=int(input('Modificador de Habilidade do Ataque: +'))
roll=random.randint(1,20)
res=mod+roll
hit=int(100-(cd-mod)*5)
if hit>=95:
    print('95% de chance se sucesso...')
elif hit<5:
    print('Sucesso somente com 20 natural, 5% chance')
else:
    print('{}% chance de sucesso...'.format(hit))
print('Rolando...')
time.sleep(2)
if roll==20:
    print('CRÍTICO!!! {} natural!!!'.format(roll))
    dado = int(input('DANO! Quantos dados? '))
    tipo = int(input('de que tipo? d'))
    rodacrit1 = random.randint(dado, tipo * dado)
    rodacrit2= random.randint(dado,tipo*dado)
    print('Rolando dano CRÍTICO ({}-{})!'.format(dado*2+modano,tipo*dado*2+modano))
    time.sleep(2)
    print('{} DE DANO! ({} e {} no dado +{} de Habilidade)'.format(rodacrit1+rodacrit2+modano,rodacrit1,rodacrit2,modano))
elif roll==1:
    print('FALHA CRÍTICA!!! {} natural'.format(roll))
elif res>=cd:
    print('SUCESSO! {} contra CD {}!'.format(res,cd))
    dado = int(input('DANO! Quantos dados? '))
    tipo = int(input('de que tipo? d'))
    rodano=random.randint(dado,tipo*dado)
    print('Rolando dano ({}-{}):'.format(dado + modano, tipo * dado + modano))
    time.sleep(2)
    print('{} de dano ({} no dado +{} de Habilidade)'.format(rodano + modano,rodano, modano))
else:
    print('FALHA! {} contra CD {}!'.format(res,cd))
#dado=int(input('DANO! Quantos dados? '))
#tipo=int(input('de que tipo? d'))


