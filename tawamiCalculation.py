import math

def tawamiCalculation(stressText,deflectionText,diameterText,sideText,heightText,Power,length,yang,diameter,side,height,switching):
    Power = float(Power.get())
    length = float(length.get())
    yang = float(yang.get())*10**9
    



    if switching == 0:
        side = float(side.get())*10**(-3)
        height = float(height.get())*10**(-3)
        yheight=0.5*height
        intertia=((side*height**3)/12)
    
    else:
        diameter = float(diameter.get())*10**(-3)
        yheight=0.5*diameter
        intertia=((math.pi*diameter**4)/64)

    result = round(float(((Power*length*yheight)/(intertia))/1000000),2)

    # 計算する時に前回の値の初期化
    stressText.delete(0, 'end')
    stressText.insert(0, result)

    result = round(float(((Power*length**3)/(3*yang*intertia))*1000),2)

    deflectionText.delete(0, 'end')
    deflectionText.insert(0, result)