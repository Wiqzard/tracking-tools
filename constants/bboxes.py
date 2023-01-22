




relative_bboxes_rack_3 = {}



"""
1. Given only rack box (x,y), get all boxes.
1.1 For each rack: w, h are constants
1.2 For each box, w,h are constants
2. Given only xy (center), we can get all the other boxes
3. x_rack - x_box, y_rack - y_box


class_id, x, y, w, h
3 0.239734375 0.5228611111111111 0.1548984375 0.5709305555555555
0 0.1968515625 0.23484722222222223 0.056203125 0.05304166666666666
0 0.250421875 0.23961111111111114 0.0538359375 0.051444444444444445
0 0.2570703125 0.4043611111111111 0.059296875000000006 0.03929166666666666
0 0.2006015625 0.405 0.0527734375 0.04611111111111112
0 0.208875 0.5975416666666666 0.052117187499999995 0.04506944444444445
0 0.26301562500000003 0.5968611111111112 0.05728124999999999 0.04651388888888889
"""

def subtract_col_first_val(data):
    new_data = []
    for i in range(len(data)):
        new_row = [data[i][0]]
        for j in range(1,len(data[i])-2):
            if i == 0:
                new_row.append(round(float(data[i][j]), 4))
            else:
                new_row.append(round(float(data[i][j] - data[0][j]), 4))
        new_row.extend((data[i][-2], data[i][-1]))
        new_data.append(new_row)
    return new_data

def get_relative():
    for i in range(1, 5):
        with open(f"{i}.txt", "r") as f:
            lines = f.readlines()
            raw_data = [[round(float(x), 4) for x in line.strip().split()] for line in lines]
            #raw_data = [line.strip().split() for line in lines]
            #raw_data = [[int(x) for x in sublist] for sublist in raw_data]
            relative_data = subtract_col_first_val(raw_data)
            print(i)
            print(relative_data)

#get_relative()




RACK_1_RELATIVE= [[1.0, 0.3061, 0.4972, 0.5169, 0.6723],[0.0, -0.0733, -0.1296, 0.0562, 0.0518],
                   [0.0, -0.133, -0.1304, 0.0603, 0.0531],[0.0, -0.1948, -0.1321, 0.0663, 0.0497],
                   [0.0, -0.1677, -0.1959, 0.0596, 0.0498],[0.0, -0.0607, -0.1978, 0.0565, 0.0544],
                   [0.0, -0.1121, -0.1977, 0.0458, 0.0462], [0.0, -0.0655, -0.2746, 0.0655, 0.0536],
                   [0.0, -0.0448, -0.3004, 0.0554, 0.0409],[0.0, -0.1044, -0.3001, 0.0612, 0.0442],
                   [0.0, -0.1318, -0.2703, 0.0671, 0.0517], [0.0, -0.2022, -0.2731, 0.0656, 0.0566], 
                   [0.0, -0.1672, -0.298, 0.0567, 0.0514], [0.0, -0.1901, -0.0034, 0.0586, 0.053], 
                   [0.0, -0.1715, -0.0644, 0.0472, 0.0422],[0.0, -0.1279, -0.005, 0.0546, 0.0517], 
                   [0.0, -0.1158, -0.0614, 0.0585, 0.0438], [0.0, -0.0672, -0.0065, 0.0581, 0.0547], 
                   [0.0, -0.0604, -0.0632, 0.0616, 0.0347], [0.0, 0.0896, -0.132, 0.0664, 0.0558], 
                   [0.0, 0.0967, -0.1881, 0.06, 0.0377],[0.0, 0.1578, -0.1279, 0.0645, 0.053],
                   [0.0, 0.2192, -0.1307, 0.0587, 0.0504], [0.0, 0.216, -0.1808, 0.0543, 0.044], 
                   [0.0, 0.153, -0.1792, 0.0552, 0.0359],[0.0, 0.0881, -0.2762, 0.0616, 0.0524],
                   [0.0, 0.0969, -0.3072, 0.0545, 0.0412],[0.0, 0.1512, -0.2715, 0.0589, 0.0513],
                   [0.0, 0.1544, -0.3049, 0.0601, 0.0429], [0.0, 0.2136, -0.3035, 0.0565, 0.0401], 
                   [0.0, 0.2132, -0.2764, 0.0646, 0.0501], [0.0, 0.2147, -0.0049, 0.06, 0.0543], 
                   [0.0, 0.2154, -0.0603, 0.057, 0.0433],  [0.0, 0.159, -0.0667, 0.0521, 0.0359],
                   [0.0, 0.1567, -0.0098, 0.0511, 0.0585],[0.0, 0.091, -0.0036, 0.0543, 0.0545],
                   [0.0, 0.0938, -0.0509, 0.0529, 0.0538], [0.0, -0.1258, 0.1004, 0.0597, 0.0437], 
                   [0.0, -0.0639, 0.0946, 0.0546, 0.058], [0.0, -0.189, 0.0976, 0.0642, 0.0494],
                   [0.0, -0.1705, 0.0565, 0.0539, 0.0352], [0.0, -0.1171, 0.0546, 0.0502, 0.0298], 
                   [0.0, -0.0571, 0.0511, 0.0521, 0.0229], [0.0, 0.0959, 0.1023, 0.0585, 0.0455],
                   [0.0, 0.0955, 0.0423, 0.0545, 0.0346], [0.0, 0.1558, 0.055, 0.0527, 0.0376],
                   [0.0, 0.1519, 0.0977, 0.0699, 0.0463],[0.0, 0.2146, 0.1007, 0.057, 0.0542], 
                   [0.0, 0.2147, 0.0548, 0.0557, 0.0373]]

RACK_2_RELATIVE = [[2.0, 0.2989, 0.5183, 0.2116, 0.62], [0.0, 0.0564, -0.2225, 0.0513, 0.0417],
                   [0.0, 0.0043, -0.2233, 0.058, 0.0456], [0.0, -0.0587, -0.2294, 0.0663, 0.0472],
                   [0.0, -0.0525, -0.2521, 0.0585, 0.0379], [0.0, 0.0099, -0.2481, 0.0551, 0.0432],
                   [0.0, 0.0622, -0.2471, 0.0498, 0.0414], [0.0, 0.0691, -0.2683, 0.0516, 0.0417],
                   [0.0, 0.0159, -0.266, 0.0437, 0.0407], [0.0, -0.0377, -0.2625, 0.0567, 0.0422],
                   [0.0, -0.0659, -0.0309, 0.0582, 0.0475], [0.0, -0.0036, -0.0326, 0.0548, 0.0492], 
                   [0.0, 0.061, -0.033, 0.0588, 0.0512], [0.0, 0.0681, -0.0833, 0.0574, 0.0422], 
                   [0.0, 0.0114, -0.0799, 0.0503, 0.0491], [0.0, -0.0564, -0.0766, 0.0646, 0.039],
                   [0.0, 0.0761, -0.1239, 0.0593, 0.0416], [0.0, 0.0154, -0.1219, 0.0552, 0.0372],
                   [0.0, -0.049, -0.1183, 0.0763, 0.0307], [0.0, -0.0568, 0.0999, 0.0639, 0.0558], 
                   [0.0, 0.0088, 0.0975, 0.0622, 0.051], [0.0, 0.0739, 0.0968, 0.0581, 0.0607],
                   [0.0, 0.0774, 0.0545, 0.0542, 0.0318], [0.0, 0.0812, 0.0195, 0.0539, 0.0394], 
                   [0.0, 0.0214, 0.0506, 0.0594, 0.0377], [0.0, 0.0276, 0.017, 0.0451, 0.0373], 
                   [0.0, -0.0467, 0.0512, 0.0642, 0.0395], [0.0, -0.0621, 0.2249, 0.0564, 0.0475],
                   [0.0, -0.0536, 0.172, 0.0484, 0.0473], [0.0, -0.041, 0.1135, 0.0424, 0.0442], 
                   [0.0, -0.0323, 0.0674, 0.0378, 0.0352], [0.0, -0.0051, 0.2264, 0.053, 0.0579], 
                   [0.0, 0.0046, 0.171, 0.0523, 0.048], [0.0, 0.0578, 0.2253, 0.0508, 0.0517], 
                   [0.0, 0.0664, 0.1699, 0.0572, 0.0485], [0.0, 0.0075, 0.1154, 0.0456, 0.0451], 
                   [0.0, 0.0636, 0.1204, 0.0532, 0.0499], [0.0, 0.02, 0.0699, 0.0361, 0.0319],
                   [0.0, 0.0762, 0.0751, 0.0425, 0.0425]]

RACK_3_RELATIVE = [[3.0, 0.2397, 0.5229, 0.1549, 0.5709], [0.0, -0.0428, -0.2881, 0.0562, 0.053],
                   [0.0, 0.0107, -0.2833, 0.0538, 0.0514], [0.0, 0.0174, -0.1185, 0.0593, 0.0393],
                   [0.0, -0.0391, -0.1179, 0.0528, 0.0461], [0.0, -0.0308, 0.0746, 0.0521, 0.0451],
                   [0.0, 0.0233, 0.074, 0.0573, 0.0465]]

RACK_4_RELATIVE = [[3.0, 0.1838, 0.4684, 0.1941, 0.6923], [0.0, -0.0605, -0.3426, 0.0622, 0.0572],
                   [0.0, 0.0014, -0.3453, 0.0548, 0.049], [0.0, 0.0237, -0.3619, 0.0604, 0.0435],
                   [0.0, -0.0323, -0.3629, 0.0561, 0.0498], [0.0, -0.0274, -0.2281, 0.0519, 0.0473],
                   [0.0, 0.0234, -0.2238, 0.0456, 0.0503], [0.0, -0.0405, -0.0559, 0.0525, 0.05], 
                   [0.0, 0.0086, -0.0534, 0.0493, 0.0467], [0.0, 0.036, -0.0775, 0.0459, 0.0513], 
                   [0.0, -0.0217, -0.0829, 0.0507, 0.0525], [0.0, 0.0179, 0.0959, 0.0582, 0.0452],
                   [0.0, 0.0459, 0.0537, 0.061, 0.0442], [0.0, -0.0375, 0.0922, 0.0521, 0.049],
                   [0.0, -0.0292, 0.2174, 0.0468, 0.0437], [0.0, -0.0163, 0.056, 0.046, 0.046], 
                   [0.0, 0.0275, 0.218, 0.0475, 0.0507]]



