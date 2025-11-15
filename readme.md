# **Jogo da velha com IA (PySide6 + Minimax)**

Este projeto é uma implementação completa de um jogo da velha com interface gráfica usando **PySide6 (Qt for Python)** e uma IA construída com o algoritmo **Minimax**, garantindo que o computador **nunca perca**.

A organização foi feita para manter o código limpo, modular e fácil de expandir.

---

## **📁 Estrutura do Projeto**

```
JOGO-DA-VELHA/
│
├── src/
│   ├── main.py
│   ├── gui.py
│   ├── tictactoe.py
│   └── values.py
│
├── files/
│   └── icon.png
│
├──.gitignore
├──readme.md
└──requirements.txt
```

---

## **🧠 IA Invencível com Minimax**

O algoritmo Minimax garante decisões ótimas para jogos determinísticos como o jogo da velha.
A lógica implementada funciona assim:

1. Simula todas as jogadas possíveis.
2. A cada simulação, avalia se leva a vitória, derrota ou empate.
3. Propaga valores de pontuação para cima da recursão.
4. A IA escolhe sempre a jogada com maior pontuação.

Resultado:
**A IA empata no pior caso. Nunca perde.**

---

## **🚀 Como Executar o código**

1. Certifique-se de ter Python 3.9+ instalado.
2. Instale o PySide6:

```bash
pip install -r requirements.txt
```

3. Execute o projeto:

```bash
python src/main.py
```

---

## **✔️ Funcionalidades**

* Interface gráfica simples, limpa e responsiva
* Jogador sempre começa
* IA baseada em Minimax
* Nunca perde (apenas vence ou empata)
* Detecção automática de fim de jogo
* Reinício rápido do tabuleiro

---

## **📄 Licença**

Uso livre para fins acadêmicos e estudos.

---