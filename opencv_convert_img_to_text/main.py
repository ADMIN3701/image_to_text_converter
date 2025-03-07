import cv2
def loading():
    img = cv2.imread("сюда ваше изображение", cv2.IMREAD_GRAYSCALE) # загрузите чб изображение
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i, j] == 255:
                print("⬛️", end='')
            else:
                print("⬜️", end='')
        print("")
loading()