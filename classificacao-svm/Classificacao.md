# Classificador de Cores

O trabalho foi dividido em 3 etapas: 
* Coleta;
* Treinamento;
* Classificação.

## Coleta

Utilizando o sensor TCS230 para coletar os dados de intensidade da luz que incide no sensor para cada filtro vermelho, verde e azul, isso nos retorna, respectivamente, um vetor de 3 caracteristicas para o classificador.

Para cada vetor dessas caracteristicas é associado um numero classificador para cor associada a leitura. Foram utilizada 4 cores a se classificar: Vermelho, verde, azul e amarelo.

## Treinamento


Baseado na lib SCIKIT LEARN para python, foi implementado um programa que fazer o treinamento SVM. Os dados coletados atravez do programa anterior é dividido entre dados de treino e de testes.

Foram criados 900 grupos de classificadores com diferentes parametros  de coeficiente Kernel e penalidade C. Ao final do treino de cada grupo, é buscado o grupo que possui o menor erro entre os as predições resultantes e os dados reais de testes.

Ao final, o rede de classificadores é salva em um arquivo que será porsteriormente utilizado pela etapa de classificação.

## Classificação em "tempo real"

Utilzando o melhor classificador do treinamento anterior, esta etapa, lê os valores do sensor novamente e faz a classificação da cor do objeto presente em frente ao sensor.

