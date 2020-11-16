import tkinter as tk
from tkinter import ttk
import UISettings
import tawamiCalculation as twmCal

# ラジオボタンを押した時のテキストボックスの切り替え
def whenSwitchedToKakuzai():
    diameterText.config(state="disable")
    sideText.config(state="normal")
    heightText.config(state="normal")

def whenSwitchedToMaruzai():
    diameterText.config(state="normal")
    sideText.config(state="disable")
    heightText.config(state="disable")

#画面作成
tki = tk.Tk()
tki.geometry(str(UISettings.windowWide) + "x" + str(UISettings.windowHeight))
tki.resizable(width=0,height=0)
tki.title('たわみ計算機')

# ラベル
Power = tk.Label(text='力:P')
Power.place(
    x=UISettings.Power['x'], y=UISettings.Power['y'])
length = tk.Label(text='長さ:L')
length.place(
    x=UISettings.length['x'], y=UISettings.length['y'])
yang = tk.Label(text='縦弾性係数:E')
yang.place(x=UISettings.yang['x'], y=UISettings.yang['y'])
diameter = tk.Label(text='丸材の直径:d')
diameter.place(x=UISettings.diameter['x'], y=UISettings.diameter['y'])
side = tk.Label(text='角材の横:b')
side.place(x=UISettings.side['x'], y=UISettings.side['y'])
height = tk.Label(text='角材の高さ:h')
height.place(x=UISettings.height['x'], y=UISettings.height['y'])
stress = tk.Label(text='応力:σ')
stress.place(
    x=UISettings.stress['x'], y=UISettings.stress['y'])
deflection = tk.Label(text='たわみ:δ')
deflection.place(
    x=UISettings.deflection['x'], y=UISettings.deflection['y'])

# テキストボックス
PowerText = tk.Entry(width=UISettings.PowerText['width'])
PowerText.place(x=UISettings.PowerText['x'], y=UISettings.PowerText['y'])
lengthText = tk.Entry(width=UISettings.lengthText['width'])
lengthText.place(
    x=UISettings.lengthText['x'], y=UISettings.lengthText['y'])
yangText = tk.Entry(width=UISettings.yangText['width'])
yangText.place(x=UISettings.yangText['x'], y=UISettings.yangText['y'])
diameterText = tk.Entry(width=UISettings.diameterText['width'])
diameterText.place(x=UISettings.diameterText['x'], y=UISettings.diameterText['y'])
sideText = tk.Entry(width=UISettings.sideText['width'])
sideText.place(x=UISettings.sideText['x'], y=UISettings.sideText['y'])
heightText = tk.Entry(width=UISettings.heightText['width'])
heightText.place(
    x=UISettings.heightText['x'], y=UISettings.heightText['y'])
stressText = tk.Entry(width=UISettings.stressText['width'])
stressText.place(x=UISettings.stressText['x'], y=UISettings.stressText['y'])
deflectionText = tk.Entry(width=UISettings.deflectionText['width'])
deflectionText.place(x=UISettings.deflectionText['x'], y=UISettings.deflectionText['y'])

# ボタン
calButton = tk.Button(
    tki, text='計算',
    command=lambda: twmCal.tawamiCalculation(
        stressText,
        deflectionText,
        diameterText,
        sideText,
        heightText,
        PowerText,
        lengthText,
        yangText,
        diameterText,
        sideText,
        heightText,
        switching.get(),
    ),
    height=UISettings.calButton['height'],
    width=UISettings.calButton['width']
)
calButton.place(x=UISettings.calButton['x'], y=UISettings.calButton['y'])

# 条件の選択
dopingDrug = tk.Label(text="条件の選択", font=("Helvetica", 16, "bold"))
dopingDrug.place(x=210, y=10)

# 式の選択
dopingDrug = tk.Label(text="式の選択", font=("Helvetica", 16, "bold"))
dopingDrug.place(x=220, y=80)
#ラジオボタン
switching = tk.IntVar()
switching.set(0)

#角材
kakuzaiButton = tk.Radiobutton(
    tki, value=0, variable=switching, text="角材", command=lambda: whenSwitchedToKakuzai())
kakuzaiButton.place(
    x=UISettings.kakuzaiButton['x'], y=UISettings.kakuzaiButton['y'])

#丸材
maruzaiButton = tk.Radiobutton(
    tki, value=1, variable=switching, text="丸材", command=lambda: whenSwitchedToMaruzai())
maruzaiButton.place(
    x=UISettings.maruzaiButton['x'], y=UISettings.maruzaiButton['y'])

#ラジオボタン
switchingsiki = tk.IntVar()
switchingsiki.set(0)

#等分布荷重
toubunpu8Button = tk.Radiobutton(
    tki, value=0, variable=switchingsiki, text="8EI")
toubunpu8Button.place(
    x=UISettings.toubunpu8Button['x'], y=UISettings.toubunpu8Button['y'])

#等分布荷重
toubunpu6Button = tk.Radiobutton(
    tki, value=1, variable=switchingsiki, text="6EI")
toubunpu6Button.place(
    x=UISettings.toubunpu6Button['x'], y=UISettings.toubunpu6Button['y'])

#集中荷重
syutyu3Button = tk.Radiobutton(
    tki, value=2, variable=switchingsiki, text="3EI")
syutyu3Button.place(
    x=UISettings.syutyu3Button['x'], y=UISettings.syutyu3Button['y'])

#集中荷重
syutyu2Button = tk.Radiobutton(
    tki, value=3, variable=switchingsiki, text="2EI")
syutyu2Button.place(
    x=UISettings.syutyu2Button['x'], y=UISettings.syutyu2Button['y'])

#モーメントの荷重
moment2Button = tk.Radiobutton(
    tki, value=4, variable=switchingsiki, text="2EI")
moment2Button.place(
    x=UISettings.moment2Button['x'], y=UISettings.moment2Button['y'])

#モーメントの荷重
moment1Button = tk.Radiobutton(
    tki, value=5, variable=switchingsiki, text="1EI")
moment1Button.place(
    x=UISettings.moment1Button['x'], y=UISettings.moment1Button['y'])

whenSwitchedToKakuzai()
#画面をそのまま表示
tki.mainloop()

