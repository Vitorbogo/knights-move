def posicao_valida(x, y, tabuleiro):
    """Verifica se uma posição é válida no tabuleiro"""
    return x >= 0 and x < 8 and y >= 0 and y < 8 and tabuleiro[x][y] == -1

def resolver_cavalo(x, y, movimento, tabuleiro, proximo_movimento):
    """Função principal que resolve o problema do passeio do cavalo"""
    
    if proximo_movimento == 64:
        return True
    
    for i in range(8):
        novo_x = x + movimento[i][0]
        novo_y = y + movimento[i][1]
        
        if posicao_valida(novo_x, novo_y, tabuleiro):
            tabuleiro[novo_x][novo_y] = proximo_movimento
            
            if resolver_cavalo(novo_x, novo_y, movimento, tabuleiro, proximo_movimento+1):
                return True
            
            # Se a chamada recursiva não levar a uma solução, remove o movimento atual
            tabuleiro[novo_x][novo_y] = -1
    
    return False

# Função principal que executa a resolução do problema
def resolver_tabuleiro_cavalo(x_inicial, y_inicial):
    """Função que resolve o problema do passeio do cavalo no tabuleiro"""
    
    # Inicializa o tabuleiro com todas as casas vazias
    tabuleiro = [[-1 for i in range(8)] for j in range(8)]
    
    # Define os movimentos possíveis do cavalo
    movimento = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
    
    # Define a posição inicial do cavalo
    tabuleiro[x_inicial][y_inicial] = 1
    
    # Tenta resolver o problema a partir da posição inicial informada pelo usuário
    if resolver_cavalo(x_inicial, y_inicial, movimento, tabuleiro, 2):
        # Se encontrou uma solução, imprime a sequência de números que representam as casas visitadas
        for i in range(8):
            for j in range(8):
                print(tabuleiro[i][j], end='\t')
            print()
        return True
    
    # Se não encontrou uma solução, retorna False
    return False

# Exemplo de uso da função principal
resolver_tabuleiro_cavalo(3, 3)
