import turtle
import level

ms = turtle.Screen()  # 创建窗口
ms.setup(900, 650, 300, 0)  # 屏幕长，高以及屏幕左上角距离电脑屏幕的距离
ms.register_shape('image/bc1.gif')
ms.register_shape('image/bc2.gif')
ms.register_shape('image/bc3.gif')
ms.register_shape('image/bc4.gif')
ms.register_shape('image/bc5.gif')
ms.bgpic('image/bc1.gif')
ms.title("推箱子小游戏")   # 窗口标题
ms.register_shape("image/wall.gif")  # 加载图片
ms.register_shape("image/o.gif")
ms.register_shape("image/p.gif")
ms.register_shape("image/box.gif")
ms.register_shape('image/boxc.gif')
ms.tracer(0) # 给出0游戏可以马上更新
levels = level.level_list()


class Pen(turtle.Turtle):  # 定义画笔
    def __init__(self, pic):
        super().__init__()  # 继承海龟类
        self.shape(pic)  # 传入形状也就是gif图片
        self.penup()   # 抬起画笔

    def move(self, x, y, px, py):
        gox, goy = x+px, y+py
        if (gox, goy) in go_space:
            self.goto(gox, goy)
        if (gox+px, goy+py) in go_space and (gox, goy) in box_space:
            for i in box_list:
                if i.pos() == (gox, goy):
                    go_space.append(i.pos())
                    box_space.remove(i.pos())
                    i.goto(gox+px, goy+py)
                    self.goto(gox, goy)
                    go_space.remove(i.pos())
                    box_space.append(i.pos())
                    if i.pos() in correct_box_space:
                        i.shape('image/boxc.gif')
                    else:
                        i.shape('image/box.gif')
                    if set(box_space) == set(correct_box_space):
                        text.show_win()

    def go_up(self):
        self.move(self.xcor(), self.ycor(), 0, 50)

    def go_down(self):
        self.move(self.xcor(), self.ycor(), 0, -50)

    def go_left(self):
        self.move(self.xcor(), self.ycor(), -50, 0)

    def go_right(self):
        self.move(self.xcor(), self.ycor(), 50, 0)


class Game(object):
    @staticmethod
    def paint():
        i_date = len(levels[num-1])
        j_date = len(levels[num-1][0])
        for i in range(i_date):
            for j in range(j_date):
                x = -j_date*25+25+j*50+225
                y = i_date*25-25-i*50
                if levels[num-1][i][j] == ' ':
                    player.goto(x, y)
                    go_space.append((x, y))
                if levels[num-1][i][j] == 'X':
                    wall.goto(x, y)
                    wall.stamp()  # 画上城墙的图片
                if levels[num-1][i][j] == 'O':
                    correct_box.goto(x, y)
                    correct_box.stamp()   # 在箱子的正确位置画上图片
                    go_space.append((x, y))
                    correct_box_space.append((x, y))
                if levels[num-1][i][j] == 'P':
                    player.goto(x, y)
                    go_space.append((x, y))
                if levels[num-1][i][j] == 'B':
                    box = Pen('image/box.gif')
                    box.goto(x, y)
                    box_list.append(box)
                    box_space.append((x, y))


class ShowMessage(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor('blue')
        self.hideturtle()

    def message(self):
        self.goto(0+sister_x, 290)
        self.write(f'第{num}关', align='center', font=('仿宋', 20, 'bold'))
        self.goto(0+sister_x, 270)
        self.write('重新开始本关请按回车键', align='center', font=('仿宋', 15, 'bold'))
        self.goto(0+sister_x, 250)
        self.write('选择关卡请按Q', align='center', font=('仿宋', 15, 'bold'))

    def show_win(self):
        global num
        if num == len(levels):
            num = 1
            self.goto(0, 0)
            self.write('你已经全部过关', align='center', font=('仿宋', 30, 'bold'))
            self.goto(0, -50)
            self.write('返回第一关请按空格键', align='center', font=('仿宋', 30, 'bold'))
        else:
            num = num + 1
            self.goto(0, 0)
            self.write('恭喜过关', align='center', font=('仿宋', 30, 'bold'))
            self.goto(0, -50)
            self.write('进入下一关请按空格键', align='center', font=('仿宋', 30, 'bold'))


def init():
    text.clear()
    wall.clear()
    correct_box.clear()
    for i in box_list:
        i.hideturtle()
        del(i)
    box_list.clear()
    box_space.clear()
    go_space.clear()
    correct_box_space.clear()
    game.paint()
    text.message()
    ms.bgpic(f'image/bc{num}.gif')


def choose():
    global num
    a = ms.numinput('选择关卡', '你的选择（请输入1-5）', 1)
    if a is None:
        a = num
    num = int(a)
    init()
    ms.listen()


sister_x = 225
num = 1
correct_box_space = []
box_list = []
box_space = []
go_space = []
wall = Pen('image/wall.gif')   # 初始化墙
correct_box = Pen('image/o.gif')  # 初始化箱子的正确位置
player = Pen('image/p.gif')  # 初始化玩家
game = Game()  # 实例化game对象
game.paint() # 画出游戏界面
text = ShowMessage()
text.message()
ms.listen()
ms.onkey(player.go_up, 'Up')
ms.onkey(player.go_down, "Down")
ms.onkey(player.go_left, 'Left')
ms.onkey(player.go_right, "Right")
ms.onkey(init, "Return")
ms.onkey(init, "space")
ms.onkey(choose, 'Q')
while True:
    ms.update()
ms.mainloop()
