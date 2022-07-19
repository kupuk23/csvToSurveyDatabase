def dom1_toSS(dom_data, array_num):# Agreeableness -- Faset 1,2,3

    if 45 <= dom_data[array_num] <= 48:
        dom_data[array_num] = 9
    elif 43 <= dom_data[array_num] <= 44:
        dom_data[array_num] = 8
    elif 41 <= dom_data[array_num] <= 42:
        dom_data[array_num] = 7
    elif 39 <= dom_data[array_num] <= 40:
        dom_data[array_num] = 6
    elif 37 <= dom_data[array_num] <= 38:
        dom_data[array_num] = 5
    elif 35 <= dom_data[array_num] <= 36:
        dom_data[array_num] = 4
    elif dom_data[array_num] == 34:
        dom_data[array_num] = 3
    elif 32 <= dom_data[array_num] <= 33:
        dom_data[array_num] = 2
    elif 12 <= dom_data[array_num] <= 31:
        dom_data[array_num] = 1
    elif dom_data[array_num] < 12:
        dom_data[array_num] = 0


def dom2_toSS(dom_data, array_num):  # Conscientiousness -- Faset 4,5,6

    if dom_data[array_num] == 48:
        dom_data[array_num] = 9
    elif 46 <= dom_data[array_num] <= 47:
        dom_data[array_num] = 8
    elif 44 <= dom_data[array_num] <= 45:
        dom_data[array_num] = 7
    elif 41 <= dom_data[array_num] <= 43:
        dom_data[array_num] = 6
    elif 38 <= dom_data[array_num] <= 40:
        dom_data[array_num] = 5
    elif 36 <= dom_data[array_num] <= 37:
        dom_data[array_num] = 4
    elif dom_data[array_num] == 35:
        dom_data[array_num] = 3
    elif 33 <= dom_data[array_num] <= 34:
        dom_data[array_num] = 2
    elif 12 <= dom_data[array_num] <= 32:
        dom_data[array_num] = 1
    elif dom_data[array_num] < 12:
        dom_data[array_num] = 0


def dom3_toSS(dom_data, array_num): # Emotional Stability -- Faset 7,8,9

    if dom_data[array_num] == 48:
        dom_data[array_num] = 9
    elif 45 <= dom_data[array_num] <= 47:
        dom_data[array_num] = 8
    elif 42 <= dom_data[array_num] <= 44:
        dom_data[array_num] = 7
    elif 39 <= dom_data[array_num] <= 41:
        dom_data[array_num] = 6
    elif 36 <= dom_data[array_num] <= 38:
        dom_data[array_num] = 5
    elif 34 <= dom_data[array_num] <= 35:
        dom_data[array_num] = 4
    elif 31 <= dom_data[array_num] <= 33:
        dom_data[array_num] = 3
    elif 27 <= dom_data[array_num] <= 30:
        dom_data[array_num] = 2
    elif 12 <= dom_data[array_num] <= 26:
        dom_data[array_num] = 1
    elif dom_data[array_num] < 12:
        dom_data[array_num] = 0


def dom4_toSS(dom_data, array_num): # Extraversion -- Faset 10,11,12

    if 46 <= dom_data[array_num] <= 48:
        dom_data[array_num] = 9
    elif 42 <= dom_data[array_num] <= 45:
        dom_data[array_num] = 8
    elif 39 <= dom_data[array_num] <= 41:
        dom_data[array_num] = 7
    elif 37 <= dom_data[array_num] <= 38:
        dom_data[array_num] = 6
    elif 35 <= dom_data[array_num] <= 36:
        dom_data[array_num] = 5
    elif 32 <= dom_data[array_num] <= 34:
        dom_data[array_num] = 4
    elif 29 <= dom_data[array_num] <= 31:
        dom_data[array_num] = 3
    elif 26 <= dom_data[array_num] <= 28:
        dom_data[array_num] = 2
    elif 12 <= dom_data[array_num] <= 25:
        dom_data[array_num] = 1
    elif dom_data[array_num] < 12:
        dom_data[array_num] = 0


def dom5_toSS(dom_data, array_num): # Open Mindedness -- Faset 13,14,15
    if 42 <= dom_data[array_num] <= 48:
        dom_data[array_num] = 9
    elif 40 <= dom_data[array_num] <= 41:
        dom_data[array_num] = 8
    elif 37 <= dom_data[array_num] <= 39:
        dom_data[array_num] = 7
    elif 35 <= dom_data[array_num] <= 36:
        dom_data[array_num] = 6
    elif 33 <= dom_data[array_num] <= 34:
        dom_data[array_num] = 5
    elif 31 <= dom_data[array_num] <= 32:
        dom_data[array_num] = 4
    elif 29 <= dom_data[array_num] <= 30:
        dom_data[array_num] = 3
    elif 26 <= dom_data[array_num] <= 28:
        dom_data[array_num] = 2
    elif 12 <= dom_data[array_num] <= 25:
        dom_data[array_num] = 1
    elif dom_data[array_num] < 12:
        dom_data[array_num] = 0
