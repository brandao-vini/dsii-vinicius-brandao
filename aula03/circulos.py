import turtle
import colorsys

def desenhar_padroes():
    tela = turtle.Screen()
    tela.bgcolor("black")
    tartaruga = turtle.Turtle()
    tartaruga.speed(0)
    tartaruga.width(2)
    tartaruga.hideturtle()

    n = 36  # número de círculos
    hues = [x/n for x in range(n)]  # para colorir em arco-íris

    for i in range(n):
        cor = colorsys.hsv_to_rgb(hues[i], 1, 1)
        tartaruga.color(cor)
        tartaruga.circle(100)
        tartaruga.right(360 / n)

    tela.mainloop()

if __name__ == "__main__":
    desenhar_padroes()
