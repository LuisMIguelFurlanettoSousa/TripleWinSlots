Este é um jogo simples de caça-níquel (slot machine) implementado em Python. Ele simula a experiência de jogar em uma máquina de caça-níquel, com animações de rolos girando, verificação de vitórias e cálculo de saldo do jogador.

Funcionalidades
Simulação de caça-níquel: O jogo possui rolos que giram e mostram combinações de símbolos aleatórios.
Níveis de dificuldade: Com a configuração do nível, a probabilidade de combinações de símbolos idênticos aumenta.
Animações: Há uma animação dos rolos girando antes do resultado final ser exibido.
Atualização de saldo: O saldo do jogador é atualizado após cada jogada, baseado no resultado (vitória ou derrota).
Pré-requisitos
Antes de rodar o jogo, você precisará ter o Python instalado no seu sistema.

Como jogar
Clone o repositório:

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
Navegue até o diretório:

cd SEU_REPOSITORIO
Execute o jogo:

python app.py
Durante o jogo:

O jogador pode fazer uma aposta (definida no código como 10 unidades).
Os rolos giram e mostram símbolos aleatórios.
Se todos os símbolos forem iguais, o jogador ganha 3 vezes o valor apostado. Caso contrário, ele perde o valor da aposta.
Exemplo de execução
Ao rodar o jogo, você verá algo semelhante a isto no terminal:

💰 💰 💰
❄️ 👽 ❤️
🔥 💥 💰
---------------
Você venceu e recebeu: 30

Estrutura do código
Player: Representa o jogador com um saldo inicial.
CassaNiquel: A classe principal que controla a geração de símbolos, o giro dos rolos, as animações, e a atualização do saldo do jogador.
Personalização
Você pode alterar os símbolos usados na máquina e a lógica de recompensa alterando o dicionário SIMBOLOS e ajustando o método de cálculo dos prêmios.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

Licença
Este projeto está licenciado sob a MIT License.
