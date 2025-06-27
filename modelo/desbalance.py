import os
import shutil
import random

origen = "./redimension_categorias"
destino = "./redimension_categorias_balanceado"
limite = 500

os.makedirs(destino, exist_ok=True)

for clase in os.listdir(origen):
    ruta_origen = os.path.join(origen, clase)
    ruta_destino = os.path.join(destino, clase)
    os.makedirs(ruta_destino, exist_ok=True)

    imagenes = os.listdir(ruta_origen)
    random.shuffle(imagenes)
    
    seleccionadas = imagenes[:min(len(imagenes), limite)]

    for imagen in seleccionadas:
        shutil.copy(os.path.join(ruta_origen, imagen), os.path.join(ruta_destino, imagen))

print("✅ Dataset balanceado creado en:", destino)
