import pandas as pd
import numpy as np
def main(lines):
    data_nom = pd.DataFrame([])
    data_hak = pd.DataFrame([])
    for i in range(1,lines[0]+1):
        line = lines[i].split(' ')
        if len(line[0])==12:
            s = pd.DataFrame({'price': [int(line[1])],
                    'stand_weight': [float(line[2])],
                    'diff': [float(line[3])]},index={line[0]})
            data_nom = pd.concat([data_nom,s])
        elif len(line[0])==5:
            s = pd.DataFrame({'100weight': [int(line[1])],
                    'pack_weitht': [float(line[2])],
                    'diff': [float(line[3])]},index={line[0]})
            data_hak = pd.concat([data_hak,s])

    start = lines[0]+2
    sum_money = 0
    for i in range(start,len(lines)-2,2):
        # 量り売り商品
        if lines[i][:2]=='02':
            # 重さの確認
            if(i!=start):
                good_weight_diff = float(lines[i+1])-float(lines[i-1])
                under_diff = weight - ok_diff
                up_diff = weight + ok_diff
                if good_weight_diff<under_diff and good_weight_diff>up_diff:
                    return 'staff call: 2'
                    # チェックナンバーの確認
            num = list(lines[i][:12])
            sum_num = [float(s) for s in num]
            if int(sum(sum_num))%10!=int(lines[i][12]):
                return 'staff call: 1 2'
            # リストにあるかの確認
            if lines[i][:12] in data_hak.index:
                return 'staff call: 1 2'
            one_data = data_hak.loc[lines[i][2:7]]
            weight = one_data['100weight']*(float(lines[i][8:12])*(1.0/100.0)) + one_data['pack_weitht']
            ok_diff = one_data['diff']
            sum_money+=int(lines[i][8:12])


            # 普通商品
        else:
            # 重さの確認
            if(i!=start):
                good_weight_diff = int(lines[i+1])-int(lines[i-1])
                under_diff = weight - ok_diff
                up_diff = weight + ok_diff
                if good_weight_diff<under_diff and good_weight_diff>up_diff:
                    return 'staff call: 2'
            num = list(lines[i][:12])
            sum_num = [float(s) for s in num]
            # チェックナンバーの確認
            if int(sum(sum_num))%10!=int(lines[i][12]):
                return 'staff call: 1 2'
                # リストにあるかの確認
            if lines[i][:12] not in data_nom.index:
                return 'staff call: 1 2'
            one_data = data_nom.loc[lines[i][:12]]
            # 重さの値を保存
            weight = one_data['stand_weight']
            ok_diff = one_data['diff']
            sum_money+=one_data['price']

    good_weight_diff = int(lines[len(lines)-1])-int(lines[len(lines)-3])
    under_diff = weight - ok_diff
    up_diff = weight + ok_diff
    if good_weight_diff<under_diff and good_weight_diff>up_diff:
        return 'staff call: 2'

    return sum_money










if __name__ == '__main__':
    lines = lines = [3,'123456789123 100 10 2','987654321234 150 15 5','54321 90 5 10',
         'start',
         '1234567891231','0',
         '0254321003459','11',
         '9876543212344','22',
         'end','30']
    """
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    """
    print(main(lines))
