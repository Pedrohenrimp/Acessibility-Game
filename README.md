# Jogo Sobre Acessibilidade

**Sobre:**

  Este jogo consiste em um trabalho da disciplina de Interface Humano-Computador, do curso de Ciência da Computação da Universidade Federal Fluminense (UFF) de Rio das Ostras, com o intuito de explicar conceitos básicos importantes de acessibilidade em UX/UI Design de forma descontraída e interativa.

*Importante ressaltar que este jogo não é direcionado para pessoas que necessitam de recursos de acessibilidade, mas sim para pessoas desenvolvedoras que projetam aplicativos e programas para uso público, para que elas possam aprender sobre conceitos básicos de acessibilidade e se inspirar para adicionarem estes tipos de recursos em seus projetos.*

A proposta do Jogo é começar em um cenário totalmente inacessível:
 - Com cores nem um pouco adaptadas para daltônicos;
 - Sem Feedback Visual;
 - Sem Feedback Auditivo e sonoro.


**Requisitos:**
- Ter o Python instalado na máquina.
- Ter o repositório do jogo disponível localmente.



**Como Jogar:**
 
  *Para rodar o jogo, baixe o repositório localmente e, da forma que preferir, execute o código main.py em sua márquina.*

   No jogo, você controla um pássaro, e deve coletar moedas para desbloquear novos recursos de acessibilidade.
<p align="center"><img src="/src/img/Exemplos/jogo_com_acessibilidade_para_daltonicos_e_surdos.png" alt="jogo com acessibilidade para daltonicos e surdos" width="350"/><p>
 
 
**Comandos:**
- Seta para cima: move o pássaro para cima;
- Seta para baixo: move o pássaro para baixo;
- Barra de espaço: interage com os menus e caixas de diálogo do jogo.
 

<p align="center"><img src="/src/img/Acessivel/instrucao_jogo.png" alt="instrucao jogo" width="300"/><p>
 <p align="center"><img src="/src/img/Acessivel/aperte_espaco.gif" alt="aperte espaco" width="200"/><p>

Conforme o jogador coleta deteminada quantidade de moedas, ele desbloqueia novos recursos de acessibilidade:
- 5 moedas: Desbloqueia o recurso de acessibilidade para daltônico, transformando a paleta de cores do game em uma paleta acessível para este tipo de público.
- 10 moedas: Desbloqueia o recurso de acessibilidade para surdos, passando a mostrar um feedback visual ilustrando os comandos do jogo.
- 15 moedas: Desbloqueia o recurso de acessibilidade para cegos e deficiêntes visuais, passando a reproduzir um feedback auditivo quando algum texto é mostrado na tela, e habilitando os recursos sonoros do jogo.


 A cada novo recurso desbloqueado, um breve texto é mostrado na tela, explicando um pouco sobre a importância de cada um dos recursos de acessibilidade.  

 O pássaro sofre influência de uma gravidade, então, com a ausência de um comando de movimentação, o pássaro cairá com aceleração.

 O jogo se encerra quando o pássaro colide com o limite superior ou inferior da tela.
 
**Imagens do Jogo:**

<p align="center"><img src="/src/img/Exemplos/jogo_sem_acessibilidade.png" alt="jogo sem acessibilidade" width="450"/><p>
 
<p align="center"><img src="/src/img/Exemplos/caixa_de_dialogo_daltonicos.png" alt="caixa de dialogo daltonicos" width="450"/><p>
  
<p align="center"><img src="/src/img/Exemplos/jogo_com_acessibilidade_para_daltonicos_e_surdos.png" alt="jogo com acessibilidade para daltonicos e surdos" width="450"/><p>
   
<p align="center"><img src="/src/img/Exemplos/caixa_de_dialogo_deficientes_visuais.png" alt="caixa de dialogo deficientes visuais e cegos" width="450"/><p>


