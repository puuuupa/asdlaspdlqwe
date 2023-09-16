from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle,randint




app = QApplication([])

window = QWidget()

window.setWindowTitle('Memory Card')
window.resize(300,300)

b = QPushButton('Ответить')
q = QLabel('Какой национальности не существует?')

rgb = QGroupBox('Варианты ответов')

b1 = QRadioButton('Энцы')
b2 = QRadioButton('Смурфы')
b3 = QRadioButton('Чулымцы')
b4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)

l1 = QHBoxLayout()
l2 = QVBoxLayout()
l3 = QVBoxLayout()

l2.addWidget(b1)
l2.addWidget(b2)
l3.addWidget(b3)
l3.addWidget(b4)

l1.addLayout(l2)
l1.addLayout(l3)

rgb.setLayout(l1)

voprosi = [b1,b2,b3,b4]

window.score = 0
window.total = 0

answgb = QGroupBox('Результат теста')
lbr = QLabel('Правильно/Неправильно')
lbc = QLabel('Правильный ответ')
lr = QVBoxLayout()
lr.addWidget(lbr, alignment=(Qt.AlignLeft | Qt.AlignTop))
lr.addWidget(lbc, alignment=Qt.AlignHCenter)

answgb.setLayout(lr)

ll1 = QHBoxLayout()
ll2 = QHBoxLayout()
ll3 = QHBoxLayout()

ll1.addWidget(q, alignment=Qt.AlignCenter)
ll2.addWidget(rgb)
ll2.addWidget(answgb)
ll3.addWidget(b)
rgb.hide()
lc = QVBoxLayout()

lc.addLayout(ll1,stretch=2)
lc.addLayout(ll2,stretch=8)
lc.addLayout(ll3)

def show_result():
    rgb.hide()
    answgb.show()
    b.setText('Следующий вопрос')

def show_quest():
    rgb.show()
    answgb.hide()
    b.setText('Ответить')
    RadioGroup.setExclusive(False)
    b1.setChecked(False)
    b2.setChecked(False)
    b3.setChecked(False)
    b4.setChecked(False)
    RadioGroup.setExclusive(True)
class Question():
    def __init__(self,q,right_,ne1,ne2,ne3):
        self.q = q
        self.right_ = right_
        self.ne1 = ne1
        self.ne2 = ne2
        self.ne3 = ne3
           

def ask(a):
    shuffle(voprosi)
    voprosi[0].setText(a.right_)
    voprosi[1].setText(a.ne1)
    voprosi[2].setText(a.ne2)
    voprosi[3].setText(a.ne3)
    q.setText(a.q)
    lbc.setText(a.right_)
    show_quest()
def correct(res):
    lbr.setText(res)
    show_result()
def chk_answ():
    if voprosi[0].isChecked():
        correct('Правильно')
        window.score += 1
        print('-Всего вопросов:',window.total)
        print('-Правильных ответов:',window.score)
        print('Рейтинг:',window.score/window.total*100)
    else:
        if voprosi[1].isChecked() or voprosi[2].isChecked() or voprosi[3].isChecked():
            correct('Неверно!')
            print('Рейтинг:',window.score/window.total*100)

list_s_voprosami = [Question('Какой язык программирования мы изучаем?','Python','pascalCBA','H++','javeya script'),
Question('Не имей 100 рублей,а имей...','100 друзей','150 друзей','дверь','батарею'),
Question('Сколько дней осталось до нового года?(примерно)','180 дней','250 дней','50 дней','3 дня'),
Question('Как переводится слово "Palabra" (испанский)','слово','лист','дерево','стол'),
Question('100$ в российских рублях приблизительно равно','8500','5000','9999','150'),
Question('Как вывести "Hello world" в Python"e','print("Hello World")','console.log("Hello World")','print("hi world")','write("Hello World")'),
Question('Когда появилась первая батарея','1799 год','1500 год','2011 год','2050 год'),
Question('Самая продаваемая игра в мире','minecraft','tetris','csgo','dota 2'),
Question('Самая большая скорость на машине','408','256','398','326'),
Question('Сколько лет самому старому человеку в мире','116','253','89','323')]

def next_q():
    window.total += 1
    print('-Всего вопросов:',window.total)
    print('-Правильных ответов:',window.score)
    cr = randint(0 , len(list_s_voprosami)-1)
    q = list_s_voprosami[cr]
    ask(q)

def click_ok():
    if b.text() == 'Ответить':
        chk_answ()
    else:
        next_q()
next_q()

b.clicked.connect(click_ok)
window.setLayout(lc)

window.show()
app.exec()
