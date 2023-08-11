import pandas as pd
import math


def termproject(text_path, library_path):
    global conductor_name, Nbundle, GMR, Dbundle, number, Vbase, Sbase, y1, y2, x2, x1, L, C, Rac, R_total, X_L, B_C, length, Req, x3, y3, diameter, GMRbundle
    student_id = 2304434

    with open(text_path) as txt:
        lines = txt.readlines()
    conductor_name = lines[13].strip()
    Sbase = float(lines[1]) * 1e6
    Vbase = float(lines[3]) * 1e3
    number = int(lines[5])
    Nbundle = float(lines[7])
    Dbundle = float(lines[9])
    length = float(lines[11]) * 1e3
    x1 = float(lines[18])
    y1 = float(lines[19])
    x2 = float(lines[21])
    y2 = float(lines[22])
    x3 = float(lines[15])
    y3 = float(lines[16])

    df = pd.read_csv(library_path)
    cond_names = df.iloc[:, 0]
    for x in range(len(cond_names)):
        if cond_names[x] == conductor_name:
            diameter = df.iloc[x, 4] * 0.0254
            Rac = df.iloc[x, 6]*0.000621371192
            GMR = df.iloc[x, 7]*0.3048

    if Nbundle == 1:
        Req = diameter / 2
        GMRbundle = GMR
    elif Nbundle == 2:
        Req = math.sqrt(Dbundle * diameter / 2)
        GMRbundle = math.sqrt(GMR * Dbundle)
    elif Nbundle == 3:
        Req = ((Dbundle ** 2) * diameter / 2) ** (1 / 3)
        GMRbundle = (GMR*Dbundle*Dbundle)**(1/3)
    elif Nbundle == 4:
        Req = (((Dbundle ** 3) * diameter / 2) ** (1 / 4)) * 1.0905
        GMRbundle = (((Dbundle ** 3) * GMR) ** (1 / 4)) * 1.0905
    elif Nbundle == 5:
        Req = (((Dbundle ** 4) * diameter / 2) ** (1 / 5)) * 1.21225
        GMRbundle = ((((Dbundle) ** 4) * GMR) ** (1 / 5)) * 1.21225
    elif Nbundle == 6:
        Req = (((Dbundle ** 5) * diameter / 2) ** (1 / 6)) * 1.34800
        GMRbundle = (((Dbundle ** 5) * GMR) ** (1 / 6)) * 1.34800
    elif Nbundle == 7:
        Req = (((Dbundle ** 6) * diameter / 2) ** (1 / 7)) * 1.49116
        GMRbundle = (((Dbundle ** 6) * GMR) ** (1 / 7)) * 1.49116
    elif Nbundle == 8:
        Req = (((Dbundle ** 7) * diameter / 2) ** (1 / 8)) * 1.638703
        GMRbundle = (((Dbundle ** 7) * GMR) ** (1 / 8)) * 1.638703


    #distance, gmd, L, C for single cct
    Dab = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    Dbc = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
    Dac = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    GMD = (Dab * Dbc * Dac) ** (1 / 3)
    L = (2 * (10 ** -7)) * (math.log10(GMD / GMR)) * length
    C = ((2 * math.pi * 8.85418782 * (10 ** -12)) / math.log(GMD / Req)) * length


    #MAIN PART
    frequency = 50
    X_L = 2 * math.pi * frequency * L
    B_C = 2 * math.pi * frequency * C
    R_total = Rac * length / (Nbundle * number)
    #per unit
    Sbase = Sbase/1000
    Vbase = Vbase/1000
    R_pu = (R_total*Sbase)/((Vbase**2)*1000)
    X_pu = (X_L*Sbase)/((Vbase**2)*1000)
    B_pu = (B_C*((Vbase**2)*1000))/Sbase

    return [student_id, R_pu, X_pu, B_pu]


print(termproject("Input_file_example.txt", "library.csv"))

