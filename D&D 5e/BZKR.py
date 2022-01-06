nvl=int(input('Qual o seu nível? '))
prof=2+(nvl-1)//4
frR=0
dxR=0
cnR=0
itR=0
sbR=0
crR=0
#Raças
raça=str(input('Qual a sua Raça? ')).title().strip()
if 'elfo' in raça.lower():
    dxR=2
    if 'alto' in raça.lower():
        itR=1
#Antecedentes
bg=str(input('Qual o seu Antecedente? ')).title().strip()
#Classes
cl1=str(input('Qual sua Classe? ')).title().strip()
#Habilidades
fr=int(input('Qual seu valor de Força? '))
dx=int(input('Qual seu valor de Destreza? '))
cn=int(input('Qual seu valor de Constituição '))
it=int(input('Qual o seu valor de Inteligência '))
sb=int(input('Qual seu valor de Sabedoria? '))
cr=int(input('Qual seu valor de Carisma? '))
frF=(fr+frR)
dxF=(dx+dxR)
cnF=(cn+cnR)
itF=(it+itR)
sbF=(sb+sbR)
crF=(cr+crR)
modf=(frF//2-5)
modd=(dxF//2-5)
modco=(cnF//2-5)
modi=(itF//2-5)
mods=(sbF//2-5)
modca=(crF//2-5)

nome=str(input('Qual o seu nome? ')).strip()
#Fim
print('\033[1;32m{}\033[m'.format(nome))
print('Raça: {}'.format(raça))
print('Antecedente: {}'.format(bg))
print('Classe: {}'.format(cl1))
print('Força {} ({:+})'.format(frF,modf))
print('Destreza {} ({:+})'.format(dxF,modd))
print('Constituição {} ({:+})'.format(cnF,modco))
print('Inteligência {} ({:+})'.format(itF,modi))
print('Sabedoria {} ({:+})'.format(sbF,mods))
print('Carisma {} ({:+})'.format(crF,modca))
print('Proficiência {:+}'.format(prof))