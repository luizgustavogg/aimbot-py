import pyautogui #Importar a biblioteca PyAutoGui
image = "circle.PNG" #Caminho da imagme

while True: #Repetir o codigo 30 Vezes
    px = pyautogui.locateOnScreen(image,grayscale=True, confidence=0.8) #Procurar a imagem e retornar os (x,y) dela
    if str(px) != "None": #Ver se a imagem foi encontrada na tela
        pyautogui.click(px) #Clickar no (x,y) da imagem
    else:
        print("Alvo não encontrado")