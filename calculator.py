from decimal import Decimal


def calculate():
    U = int(input('Введите напряжение в Вольтах: '))
    L_cable = float(input('Введите длину кабеля: '))
    L_cable1 = L_cable * 2
    L_ribbon = float(input('Введите длину ленты: '))
    p1_meter = int(input('Введите p1метр: '))
    P = p1_meter * L_ribbon
    permissible_fall_voltage = 0.05
    I = P / U
    dU = U * permissible_fall_voltage
    R = dU / I
    S = Decimal(float(0.0175))
    result = U - dU

    print(f'================================================================')
    print(f'Суммарная мощность ленты: {p1_meter * L_ribbon}')
    print(f'Допустимое падение напряжения (5%): {p1_meter * L_ribbon}')
    print(f'I (ампер): {P / U}')
    print(f'dU (вольт): {dU}')
    print(f'R (Ом): {dU / I}')
    print(f'S (сечение мм2): {0.0175 * L_cable1 / R}')
    print(f'U итог: {U - (U * permissible_fall_voltage)}')
    print(f'================================================================')
    print()
    print(input('Нажмите ENTER чтобы продолжить ...'))
    calculate()


calculate()