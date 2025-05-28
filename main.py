#Script de treinamento do modelo

# Load a model
#model = YOLO(yolov8n.pt)  # load a pretrained model (recommended for training)

# Train the model
#results = model.train(data="brain-tumor.yaml", epochs=100, imgsz=608)

#results = model(r"C:\Users\Pichau\ml-tumor-cerebral\imagesTest\teste1.jpg")

# Exibe resultados
#results[0].show()  # ou results.show()



#Script de funcionamento do sistema
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from PIL import Image, ImageTk
from ultralytics import YOLO
import os
import shutil
from datetime import datetime

# Caminho do modelo YOLO
MODEL_PATH = r"runs\detect\train6\weights\best.pt"
model = YOLO(MODEL_PATH)

# Usuários (mock)
USERS = {"admin": "1234", "medico": "senha"}

# Pastas de destino
PASTA_TESTE = "analisadas/imagemTest"
PASTA_ERRO = "analisadas/imagemErro"
PASTA_RELATORIO = "relatorios"

os.makedirs(PASTA_TESTE, exist_ok=True)
os.makedirs(PASTA_ERRO, exist_ok=True)
os.makedirs(PASTA_RELATORIO, exist_ok=True)


def autenticar(usuario, senha, root):
    if USERS.get(usuario) == senha:
        root.destroy()
        abrir_dashboard()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")


def abrir_dashboard():
    janela = tk.Tk()
    janela.title("Detecção de Tumores Cerebrais")
    janela.geometry("1100x700")
    janela.resizable(False, False)

    paciente_info = {"nome": None, "imagem_analisada": None}

    # ---------- LAYOUT ----------
    tk.Label(janela, text="Sistema de Detecção de Tumores Cerebrais", font=("Arial", 16, "bold")).pack(pady=10)

    frm_topo = tk.Frame(janela)
    frm_topo.pack()

    tk.Label(frm_topo, text="Nome do paciente:").pack(side=tk.LEFT, padx=5)
    entry_nome = tk.Entry(frm_topo, width=30)
    entry_nome.pack(side=tk.LEFT, padx=5)

    frm_imgs = tk.Frame(janela)
    frm_imgs.pack()

    lbl_original = tk.Label(frm_imgs, text="Imagem Original", font=("Arial", 12))
    lbl_original.grid(row=0, column=0)
    img_original = tk.Label(frm_imgs)
    img_original.grid(row=1, column=0, padx=20)

    lbl_analisada = tk.Label(frm_imgs, text="Imagem Analisada", font=("Arial", 12))
    lbl_analisada.grid(row=0, column=1)
    img_analisada = tk.Label(frm_imgs)
    img_analisada.grid(row=1, column=1, padx=20)

    # ---------- FUNÇÕES ----------
    def selecionar_imagem():
        caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.png")])
        if not caminho:
            return

        nome = entry_nome.get().strip()
        if not nome:
            messagebox.showwarning("Atenção", "Digite o nome do paciente antes de selecionar a imagem.")
            return

        paciente_info["nome"] = nome

        # Mostrar imagem original
        exibir_imagem(img_original, caminho)

        # Fazer predição
        results = model(caminho)
        img_pred = results[0].save(filename=f"{nome}_predita.jpg")

        paciente_info["imagem_analisada"] = img_pred
        exibir_imagem(img_analisada, img_pred)

    def exibir_imagem(label, caminho):
        img = Image.open(caminho)
        img = img.resize((400, 400))
        tk_img = ImageTk.PhotoImage(img)
        label.config(image=tk_img)
        label.image = tk_img

    def gerar_relatorio(paciente_nome, resultado_predicao, observacoes, diretorio="relatorios"):
        os.makedirs(diretorio, exist_ok=True)
        data = datetime.now().strftime("%d-%m-%Y")

        nome_arquivo = f"{diretorio}/Relatorio_{paciente_nome}_{data}.txt"

        with open(nome_arquivo, "w", encoding="utf-8") as file:
            file.write("----------------------------------------------\n")
            file.write("   RELATÓRIO MÉDICO DE ANÁLISE - TUMOR CEREBRAL\n")
            file.write("----------------------------------------------\n\n")
            file.write(f"Paciente: {paciente_nome}\n")
            file.write(f"Data da Análise: {data}\n\n")
            file.write("------------------------------------------------\n")
            file.write("🔍 Dados da Análise:\n\n")
            file.write("O sistema de IA foi utilizado para realizar a análise.\n\n")
            file.write(f"Resultado da Análise: {resultado_predicao}\n\n")
            file.write("------------------------------------------------\n")
            file.write("📄 Observações do Médico:\n\n")
            file.write(f"{observacoes}\n\n")
            file.write("------------------------------------------------\n")
            file.write(f"Data: {data}\n\n")
            file.write("___________________________________________\n")
            file.write("Assinatura do Médico\n")
        print(f"Relatório gerado em: {nome_arquivo}")
        
    def avaliar_predicao(correta: bool):
        nome = paciente_info.get("nome")
        imagem = paciente_info.get("imagem_analisada")
        if not nome or not imagem:
            messagebox.showwarning("Aviso", "Nenhuma imagem foi analisada ainda.")
            return

        pasta_destino = PASTA_TESTE if correta else PASTA_ERRO
        data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        novo_nome = f"{nome}_{data}.jpg"
        shutil.copy(imagem, os.path.join(pasta_destino, novo_nome))
        messagebox.showinfo("Imagem salva", f"Imagem salva em: {pasta_destino}")

    # ---------- BOTÕES ----------
    frm_botoes = tk.Frame(janela)
    frm_botoes.pack(pady=20)

    tk.Button(frm_botoes, text="Selecionar Nova Imagem", font=("Arial", 12), command=selecionar_imagem).grid(row=0, column=0, padx=10)
    tk.Button(frm_botoes, text="Gerar Relatório TXT", font=("Arial", 12),
          command=lambda: gerar_relatorio(
              paciente_info.get("nome"),
              resultado_predicao="Tumor DETECTADO ou NÃO DETECTADO",
              observacoes=simpledialog.askstring("Relatório Médico", "Digite as observações para este paciente:")
          )).grid(row=0, column=4, padx=10)
    tk.Button(frm_botoes, text="Predição Correta ✔️", font=("Arial", 12), command=lambda: avaliar_predicao(True)).grid(row=0, column=2, padx=10)
    tk.Button(frm_botoes, text="Predição Incorreta ❌", font=("Arial", 12), command=lambda: avaliar_predicao(False)).grid(row=0, column=3, padx=10)

    janela.mainloop()


# ---------- LOGIN ----------
def main():
    root = tk.Tk()
    root.title("Login Médico")
    root.geometry("300x200")
    root.resizable(False, False)

    tk.Label(root, text="Usuário:", font=("Arial", 12)).pack(pady=5)
    entry_user = tk.Entry(root)
    entry_user.pack()

    tk.Label(root, text="Senha:", font=("Arial", 12)).pack(pady=5)
    entry_pass = tk.Entry(root, show="*")
    entry_pass.pack()

    btn_login = tk.Button(
        root,
        text="Entrar",
        font=("Arial", 12),
        command=lambda: autenticar(entry_user.get(), entry_pass.get(), root)
    )
    btn_login.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
