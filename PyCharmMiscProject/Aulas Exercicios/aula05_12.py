import socket
import threading
import sys

PORTA = 5555


def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def obter_ip_local():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"


def receber_mensagens(conexao):
    while True:
        try:
            mensagem = conexao.recv(1024).decode('utf-8')
            if mensagem:
                print(f"\r{mensagem}")
                print("Você: ", end='', flush=True)
            else:
                print("\n[!] Conexão encerrada pelo outro usuário.")
                conexao.close()
                break
        except:
            print("\n[!] Conexão perdida!")
            conexao.close()
            break


def enviar_mensagens(conexao):
    while True:
        try:
            mensagem = input("Você: ")
            if mensagem.lower() == 'sair':
                conexao.send("[SAIU DO CHAT]".encode('utf-8'))
                conexao.close()
                print("[!] Você saiu do chat.")
                sys.exit(0)
            conexao.send(mensagem.encode('utf-8'))
        except:
            print("\n[!] Erro ao enviar mensagem.")
            conexao.close()
            break


def modo_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        servidor.bind(('0.0.0.0', PORTA))
        servidor.listen(1)

        print("\n" + "=" * 50)
        print(" SERVIDOR INICIADO")
        print("=" * 50)
        print(f" Seu IP: {obter_ip_local()}")
        print(f" Porta: {PORTA}")
        print("\n Aguardando conexão...")
        print("=" * 50 + "\n")

        conexao, endereco = servidor.accept()
        print(f" Cliente conectado: {endereco[0]}")
        print("\n Chat iniciado! Digite 'sair' para encerrar.\n")

        thread_receber = threading.Thread(target=receber_mensagens, args=(conexao,))
        thread_enviar = threading.Thread(target=enviar_mensagens, args=(conexao,))

        thread_receber.daemon = True
        thread_enviar.daemon = True

        thread_receber.start()
        thread_enviar.start()

        thread_enviar.join()

    except Exception as e:
        print(f" Erro no servidor: {e}")
    finally:
        servidor.close()


def modo_cliente():
    print("MODO CLIENTE")
    print("--------")

    ip_servidor = input("Digite o IP do servidor: ").strip()

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f"\nConectando a {ip_servidor}:{PORTA}...")
        cliente.connect((ip_servidor, PORTA))
        print(f"Conectado com sucesso!")
        print("\nChat iniciado! Digite 'sair' para encerrar.\n")

        # Iniciar threads
        thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,))
        thread_enviar = threading.Thread(target=enviar_mensagens, args=(cliente,))

        thread_receber.daemon = True
        thread_enviar.daemon = True

        thread_receber.start()
        thread_enviar.start()

        thread_enviar.join()

    except Exception as e:
        print(f"Erro ao conectar: {e}")
    finally:
        cliente.close()


def main():
    limpar_tela()

    print("=" * 50)
    print("CHAT P2P - PYTHON")
    print("=" * 50)
    print("\n Escolha o modo:")
    print("   [1] Servidor )")
    print("   [2] Cliente ")
    print("   [3] Sair")
    print("\n" + "--" * 50)

    escolha = input("\n Opção: ").strip()

    if escolha == '1':
        modo_servidor()
    elif escolha == '2':
        modo_cliente()
    elif escolha == '3':
        print("\n Até logo!")
        sys.exit(0)
    else:
        print("\n Opção inválida!")
        main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Chat encerrado!")
        sys.exit(0)