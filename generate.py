import time
import random
from scipy.stats import expon

random.seed(1)

def log(*args):
    with open('simulated_data.csv', 'a') as outfile:
        outfile.write(','.join([str(x) for x in args]))
        outfile.write('\n')

first_pattern_c4 = [0, 2, 2, 4, 3, 6, 6, 6, 6, 6, 6, 6, 6, 14, 7, 7, 17, 16, 19, 8, 8, 22, 21, 24, 9, 9, 27, 26, 29, 10, 10, 31, 30, 32, 11, 11, 34, 33, 35, 12, 12, 38, 37, 39, 39, 41, 40]
second_pattern_c4 = first_pattern_c4 + [26, 29, 30, 10, 10, 32, 31, 33, 11, 11, 35, 34, 36, 12, 12, 39, 38, 40, 40, 42, 41, 41, 43]

first_pattern_c5 = [1, 0, 3, 5, 4, 2, 7, 8, 9, 10, 11, 12, 13, 15, 14, 16, 18, 17, 20, 19, 21, 23, 22, 25, 24, 26, 28, 27, 28, 29, 30, 1, 31, 28, 32, 33, 15, 34, 36, 35, 37, 25, 38, 6, 40, -1, 41]
second_pattern_c5 = first_pattern_c4 + [29, 28, 28, 30, 31, 1, 32, 28, 33, 34, 15, 35, 37, 36, 38, 25, 39, 6, 41, 5, 42, 43, -1]
c5_cycle = [5, 8, 23]

type0_sizes = {  # key: group index
    0: 10,
    1: 10, 
    2: 5, 
    3: 33, 
    4: 33, 
    5: 17, 
    6: 33, 
    7: 33, 
    8: 17,
    9: 5,
    10: 5,
    11: 5
}

type0_gap_stats = {  # key: number of type0 rows
    5: 0.01369,
    10: 0.0412,
    17: 0.1094,
    33: 0.3347,
}

type0_pattern1_cycle = [3, 4, 0, 5, 1]           # when col4=0 (5,10,17)
type0_pattern2_cycle = [4, -1, 3, 5]             # when col4=1 (5,10,17)
type0_pattern3_cycle = [4, 4, 0, 5, 5, 1]        # when col7=1 (17)
type0_pattern4_cycle = [4, 4, 4, 0, 5, 5, 5, 1]  # when col7=2 (17)
type0_pattern5_cycle = [4, -1, 3, 4, 4, 0, 4, 5, 5, 5, 1, 5]    # when col7=1 (33)
type0_pattern6_cycle = [4, -1, 3, 4, 4, 0, 5, 5, 1, 5]          # when col4=1 & col6!=2 & col7!=2
type0_pattern7_cycle = [4, 4, -1, 3, 4, 4, 0, 5 ,5, 5, 5, 1]    # when col4=2 & col6!=2 & col7==1
type0_pattern8_cycle = [4, 4, -1, 3, 5, 5]                      # when col4=2 & col6!=2 & col7!=2

type1_gap_stats = { # key: number of type0 rows
    5: 0.1105,
    10: 0.3790,
    17: 0.8979,
    33: 3.2570,
}

type1_results = {  # key: number of type0 rows
    5: 0, 
    10: 1,
    17: 0,
    33: 1
}

first_group10 = True
first_group17 = True
first_group33 = True
timestamp = time.time()
for group in range(12):  # for each group
    first_pattern_c5[-2] = c5_cycle[group%3]
    second_pattern_c5[-1] = c5_cycle[group%3]
    
    # Generate -1 rows first
    if group < 3:
        num_rows = 47
        for j in range(num_rows):
            log(timestamp, -1, group, first_pattern_c4[j], first_pattern_c5[j])
    else:
        num_rows = 51
        for j in range(num_rows):
            log(timestamp, -1, group, second_pattern_c4[j], second_pattern_c5[j])


    # Generate 0 rows
    num_type0 = type0_sizes[group]
    column4_10 = [0]*5 + [1]*5
    column4_17 = [0]*5 + [1]*12
    column4_33 = [0]*5 + [1]*14 + [2]*14
    column6_17 = [0]*4 + [1]*7 + [2]*1
    column7_17 = [0]*6 + [1]*6
    column6_33 = [0]*8 + [1]*18 + [2]*2
    column7_33 = [0]*11 + [1]*9 + [2]*8
    
    random.shuffle(type0_pattern1_cycle)
    random.shuffle(type0_pattern2_cycle)
    random.shuffle(type0_pattern3_cycle)
    random.shuffle(type0_pattern4_cycle)
    random.shuffle(type0_pattern5_cycle)
    random.shuffle(type0_pattern6_cycle)
    random.shuffle(type0_pattern7_cycle)
    random.shuffle(type0_pattern8_cycle)
    
    if first_group10:
        random.shuffle(column4_10)
    else:
        first_group10 = False
    if first_group17:
        random.shuffle(column4_17)
    else:
        first_group17 = False
    if first_group33:
        random.shuffle(column4_33)
    else:
        first_group33 = False
        
    m, n, o, p, q, r, s, t = 0, 0, 0, 0, 0, 0, 0, 0
    first, first1, first2, first3 = True, True, True, True

    for k in range(num_type0):  # generate the rows
        sleep = expon.rvs(type0_gap_stats[num_type0])
        timestamp += sleep
        
        if num_type0 == 5:  # trivial case
            log(timestamp, 0, group, 0, type0_pattern1_cycle[k], 0)
        elif num_type0 == 10:
            col4_val = column4_10[k]  # check column4 first
            if col4_val == 0:
                log(timestamp, 0, group, col4_val, type0_pattern1_cycle[m], 0, 0)
                m += 1
            else:  # col4 = 1
                random.shuffle(type0_pattern2_cycle)
                if first:
                    log(timestamp, 0, group, col4_val, random.randint(0, 1), 1, 0)
                    first = False
                else:
                    log(timestamp, 0, group, col4_val, type0_pattern2_cycle[n], 1, 0)
                    n += 1
            if first_group10:
                first_group10 = False
        elif num_type0 == 17:
            col4_val = column4_17[k]
            if col4_val == 0:
                log(timestamp, 0, group, col4_val, type0_pattern1_cycle[m], 0, 0)
                m += 1
            else:
                col6_val = random.sample(column6_17, 1)[0]
                column6_17.remove(col6_val)
                if col6_val == 2:
                    log(timestamp, 0, group, col4_val, 3, col6_val, 0)
                else:
                    col7_val = random.sample(column7_17, 1)[0]
                    column7_17.remove(col7_val)
                    if col7_val == 1:
                        log(timestamp, 0, group, col4_val, type0_pattern3_cycle[o], col6_val, col7_val)
                        o += 1
                    else:
                        if first:
                            log(timestamp, 0, group, col4_val, random.randint(0, 1), col6_val, col7_val)
                            first = False
                        else:
                            log(timestamp, 0, group, col4_val, type0_pattern2_cycle[n], col6_val, col7_val)
                            n += 1
            if first_group17:
                first_group17 = False
        else:  # num_type0 = 33
            col4_val = column4_33[k]
            if col4_val == 0:
                log(timestamp, group, 0, col4_val, type0_pattern1_cycle[m], 0, 0)
                m += 1
            elif col4_val == 1:
                col6_val = random.sample(column6_33, 1)[0]
                column6_33.remove(col6_val)
                if col6_val == 2:
                    log(timestamp, 0, group, col4_val, 3, col6_val, 0)
                else:
                    col7_val = random.sample(column7_33, 1)[0]
                    column7_33.remove(col7_val)
                    if col7_val == 2:
                        log(timestamp, 0, group, col4_val, type0_pattern4_cycle[p], col6_val, col7_val)
                        p += 1
                    elif col7_val == 1:
                        log(timestamp, 0, group, col4_val, type0_pattern5_cycle[q], col6_val, col7_val)
                        q += 1
                    else: # col7_val = 0
                        if first1:
                            log(timestamp, 0, group, col4_val, random.randint(0, 1), col6_val, col7_val)
                            first1 = False
                        else:
                            log(timestamp, 0, group, col4_val, type0_pattern6_cycle[r], col6_val, col7_val)
                            r += 1
            else:  # col4_val = 2
                col6_val = random.sample(column6_33, 1)[0]
                column6_33.remove(col6_val)
                if col6_val == 2:
                    log(timestamp, 0, group, col4_val, 3, col6_val, 0)
                else:
                    col7_val = random.sample(column7_33, 1)[0]
                    column7_33.remove(col7_val)
                    if col7_val == 2:
                        log(timestamp, 0, group, col4_val, type0_pattern4_cycle[p], col6_val, col7_val)
                        p += 1
                    elif col7_val == 1:
                        if first2:
                            log(timestamp, 0, group, col4_val, random.randint(0, 1), col6_val, col7_val)
                            first2 = False
                        else:
                            log(timestamp, 0, group, col4_val, type0_pattern7_cycle[s], col6_val, col7_val)
                            s += 1
                    else: # col7_val = 0
                        if first3:
                            log(timestamp, 0, group, col4_val, random.randint(0, 1), col6_val, col7_val)
                            first_group33 = False
                        else:
                            log(timestamp, 0, group, col4_val, type0_pattern8_cycle[t], col6_val, col7_val)
                            t += 1
            if first_group33:
                first_group33 = False

    # Generate 1 rows
    sleep = expon.rvs(type1_gap_stats[num_type0])
    timestamp += sleep
    log(timestamp, 1, group, type1_results[num_type0])
    timestamp += 0.0005