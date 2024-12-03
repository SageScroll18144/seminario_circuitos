import serial
import pygame
import sys

def main():
    # Configuração da porta serial
    porta = "/dev/ttyUSB0"  # Substitua pela sua porta correta
    baudrate = 9600

    try:
        ser = serial.Serial(porta, baudrate, timeout=5)
        print(f"Conectado à porta {porta} com baudrate {baudrate}")

        # Inicializa o pygame
        pygame.init()
        largura, altura = 800, 800
        tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Leitura Serial com Pygame")
        fonte = pygame.font.Font(None, 36)  # Fonte padrão, tamanho 36
        cor_texto = (25, 25, 25)

        # Carrega a imagem de fundo
        caminho_imagem = "background.png"  # Substitua pelo caminho correto da sua imagem
        try:
            fundo = pygame.image.load(caminho_imagem)
            fundo = pygame.transform.scale(fundo, (largura, altura))  # Redimensiona para caber na tela
        except pygame.error as e:
            print(f"Erro ao carregar imagem: {e}")
            sys.exit(1)

        rodando = True
        dado_serial = "Esperando dados..."

        while rodando:
            # Processa eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            # Lê dados da serial
            linha_raw = ser.readline()
            try:
                dado_serial = linha_raw.decode('utf-8', errors='ignore').strip()
            except Exception:
                dado_serial = "Erro na leitura dos dados"

            # Atualiza a tela
            tela.blit(fundo, (0, 0))  # Desenha a imagem de fundo
            texto = fonte.render(f"{dado_serial}", True, cor_texto)
            tela.blit(texto, (150, 70))  # Centraliza o texto horizontalmente
            pygame.display.flip()

    except serial.SerialException as e:
        print(f"Erro ao acessar a porta serial: {e}")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\nEncerrando leitura serial.")

    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Conexão serial encerrada.")
        pygame.quit()

if __name__ == "__main__":
    main()
