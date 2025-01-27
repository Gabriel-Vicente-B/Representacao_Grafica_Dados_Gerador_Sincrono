Diagrama Fasorial, Curva de Torque e Curva de Capacidade para Geradores e Motores

Este código realiza o cálculo e a plotagem de gráficos relacionados ao comportamento de geradores e motores elétricos, incluindo diagramas fasoriais, curvas de torque, curvas de capacidade, e análise de CAV (Curva Característica de Avarias). O código é desenvolvido para realizar a leitura de dados de um arquivo de texto, calcular parâmetros do gerador e da carga, e exibir os resultados graficamente.
Funcionalidades

    Leitura de Dados: O código lê informações de um arquivo de texto (Dados.txt), que contém parâmetros do gerador, carga e outros dados necessários para os cálculos.

    Cálculos:
        Parâmetros do Gerador: Calcula corrente, tensão, e outros parâmetros essenciais.
        Parâmetros da Carga: Calcula a corrente e outros parâmetros da carga conectada ao gerador.
        Torque de Operação: Calcula a curva de torque com base nos dados de entrada, incluindo o ângulo entre o campo elétrico e a tensão do gerador.
        CAV: Análise de corrente e tensão do estator.
        Curva de Capacidade: Exibe a relação entre a potência ativa e a potência reativa do sistema.

    Plotagem:
        Diagrama fasorial, mostrando as tensões e correntes.
        Curva de torque em função do ângulo.
        Curva de capacidade, exibindo a capacidade do gerador/motor em termos de potência e corrente.
        Gráfico da CAV (Curva Característica de Avarias), mostrando a corrente do estator e a tensão terminal.
