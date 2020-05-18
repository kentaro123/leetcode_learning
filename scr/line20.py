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

    start = lines[0]+1
    for i in range(start,len(lines)):
        # 量り売り商品
        sum_money = 0
        line = lines[i].split(' ')
        flag=True
        if lines[i]=='start':
            sum_money = 0
            flag = True
        elif line[0]=='end':
            line_past = lines[i-1].split(' ')
            line = lines[i].split(' ')
            good_weight_diff = float(line[1])-float(line_past[1])
            under_diff = weight - ok_diff
            up_diff = weight + ok_diff
            if good_weight_diff<under_diff and good_weight_diff>up_diff:
                return 'staff call: 2'
            print(sum_money)
        elif line[0][:2]=='02':
            # 重さの確認
            if(flag!=True):
                line_past = lines[i-1].split(' ')
                good_weight_diff = int(line[1])-int(line_past[1])
                under_diff = weight - ok_diff
                up_diff = weight + ok_diff
                if good_weight_diff<under_diff and good_weight_diff>up_diff:
                    return 'staff call: 2'
            else:
                flag=False
            # チェックナンバーの確認
            num = list(line[0][:12])
            sum_num = [float(s) for s in num]
            if int(sum(sum_num))%10!=int(line[0][12]):
                return 'staff call: 1 2'
            # リストにあるかの確認
            if lines[i][:12] in data_hak.index:
                return 'staff call: 1 2'
            one_data = data_hak.loc[line[0][2:7]]
            weight = one_data['100weight']*(float(line[0][8:12])*(1.0/100.0)) + one_data['pack_weitht']
            ok_diff = one_data['diff']
            sum_money+=int(line[0][8:12])
            # 普通商品
        else:
            # 重さの確認
            if(flag!=True):
                line_past = lines[i-1].split(' ')
                good_weight_diff = int(line[1])-int(line_past[1])
                under_diff = weight - ok_diff
                up_diff = weight + ok_diff
                if good_weight_diff<under_diff and good_weight_diff>up_diff:
                    return 'staff call: 2'
            else:
                flag=False
            num = list(line[0][:12])
            sum_num = [float(s) for s in num]
            # チェックナンバーの確認
            if int(sum(sum_num))%10!=int(line[0][12]):
                return 'staff call: 1 2'
                # リストにあるかの確認
            if line[0][:12] not in data_nom.index:
                return 'staff call: 1 2'
            one_data = data_nom.loc[line[0][:12]]
            # 重さの値を保存
            weight = one_data['stand_weight']
            ok_diff = one_data['diff']
            sum_money+=one_data['price']

if __name__ == '__main__':
    lines = [3,'123456789123 100 10 2','987654321234 150 15 5','54321 90 5 10',
         'start',
         '1234567891231 0',
         '0254321003459 11',
         '9876543212344 22',
         'end 30']
    print(main(lines))
