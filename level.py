def level_list():  # X代表墙的位置，O代表应该去到的正确位置
    level_1 = [   # B代表现在箱子所处的位置，P代表玩家所处的位置
        'CCXXXCCC',  # 空白就是代表空白，每个方块长50像素
        'CCXOXCCC', # turtle模块是以屏幕的正中心为坐标原点
        'CCX XXXX',
        'XXXB BOX',
        'XO BPXXX',
        'XXXXBXCC',
        'CCCXOXCC',
        'CCCXXXCC']
    level_2 = [
        'CXXXXCCC',
        'CX OXXXX',
        'XXO    X',
        'XOO XX X',
        'X B  B X',
        'XX BBXXX',
        'CXP  XCC',
        'CXXXXXCC']
    level_3 = [
        'CCXXXXXXCC',
        'CCX    XXX',
        'CCX B    X',
        'XXX B XX X',
        'XOOO B   X',
        'XOOOBXB XX',
        'XXXX X B X',
        'CCCX  P  X',
        'CCCXXXXXXX']
    level_4 = [
        'CCCXXXXXX',
        'XXXXO  PX',
        'X  BBB  X',
        'XOXXOXXOX',
        'X   B   X',
        'X  BOX XX',
        'XXXX   XC',
        'CCCXXXXXC']
    level_5 = [
        'CXXXXXXXC',
        'XX     XX',
        'X  BOB  X',
        'X BXOXB X',
        'XXOOPOO X',
        'X BXOXB X',
        'X  BOB  X',
        'X   X  XX',
        'XXXXXXXXC']
    levels = [level_1, level_2, level_3, level_4, level_5]
    return levels
