Este projeto aplica técnicas de Aprendizado de Máquina para a detecção de tumores cerebrais em imagens de ressonância magnética (RM) utilizando o framework Ultralytics YOLO. O objetivo é desenvolver um modelo eficiente e acessível para auxiliar profissionais da saúde na identificação e segmentação de tumores cerebrais.


📖 Descrição

O modelo YOLO foi treinado com um dataset especializado de imagens médicas para detectar padrões característicos de tumores cerebrais. A abordagem adotada permite:
✅ Classificação entre imagens com e sem tumores.
✅ Segmentação das áreas afetadas para melhor análise clínica.
✅ Automação do processo diagnóstico para apoio médico.
O projeto foi desenvolvido com Python e utiliza bibliotecas de IA e visão computacional, incluindo:

Ultralytics YOLO
OpenCV
TensorFlow/Keras
NumPy/Pandas
tkinter



📊 Resultados

O modelo foi avaliado em um dataset de 1.116 imagens, atingindo os seguintes resultados:
📌 Acurácia: 95.2%
📌 Sensibilidade: 93.5%
📌 Especificidade: 96.1%
📌 Precisão: 94.3%
📌 F1-Score: 94.8%


🛠️ Tecnologias Utilizadas



Linguagem: Python 🐍


Framework de Detecção: Ultralytics YOLO

Manipulação de Imagens: OpenCV

Treinamento e IA: TensorFlow, Keras, PyTorch

Ambiente de Desenvolvimento: Vscode

Interface: tkinter


📌 Próximos Passos

📌 Melhorar o dataset com mais imagens para reduzir viés.
📌 Ajustar hiperparâmetros para otimizar detecção em tumores raros.
📌 Criar uma API para integrar o modelo a sistemas clínicos.


🤝 Contribuição

Fique à vontade para contribuir com este projeto! Para isso:

Faça um fork do repositório.
Crie uma branch com sua funcionalidade (git checkout -b minha-feature).
Faça um commit das suas alterações (git commit -m 'Minha nova feature').
Envie para o repositório (git push origin minha-feature).
Abra um pull request.


📌 Autores:
👤 Gabriel Gonçalves da Silva
👤 Johnathan Araujo Nunes
👤 Mateus Fonseca da Silva



@software{yolov8_ultralytics,
  author = {Glenn Jocher and Ayush Chaurasia and Jing Qiu},
  title = {Ultralytics YOLOv8},
  version = {8.0.0},
  year = {2023},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}
