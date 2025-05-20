from ultralytics import YOLO

# Load a model
model = YOLO(r"C:\Users\Pichau\ml-tumor-cerebral\runs\detect\train6\weights\best.pt")  # load a pretrained model (recommended for training)

# Train the model
#results = model.train(data="brain-tumor.yaml", epochs=100, imgsz=608)

results = model(r"C:\Users\Pichau\ml-tumor-cerebral\imagesTest\teste1.jpg")

# Exibe resultados
results[0].show()  # ou results.show()