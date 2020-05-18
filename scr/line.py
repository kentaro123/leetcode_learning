# 座標に変換
zahyo = []
for i in range(n):
    memo = []
    for j in range(n):
        memo.append(line[i][j])
    zahyo.append(memo)
while flag:
    flag = False
    for i in range(1,n-1):
        if 'x' in zahyo[1][1:n-1]:
            flag = True
    if flag==False:
        break
    # 反感座標の定義
    max_count = 0
    memo= 0
    final_start = 0
    final_end = 0
    # 横の最大連続長を調査
    y_memo = 0
    y_max_count = 0
    y_final_start = 0
    y_final_end = 0
    for i in range(5):
        count = 0
        m_count = 0
        start = 0
        f_start = 0
        f_end = 0
        if 'x' in zahyo[i]:
            for j in range(1,n-1):
                if zahyo[i][j]=='x':
                    if count==0:
                        start = j
                    count +=1
                    if m_count<count:
                        m_count=count
                        f_start = start
                        f_end = j
                else:
                    count = 0
            if max_count<m_count:
                y_max_count = m_count
                y_memo=i+1
                y_final_start = f_start
                y_final_end = f_end+1
    # 縦の連続長を調査
    t_memo = 0
    t_max_count = 0
    t_final_start = 0
    t_final_end = 0
    for i in range(5):
        count = 0
        m_count = 0
        start = 0
        end = 0
        f_start = 0
        f_end = 0
        if 'x' in a[i]:
            for j in range(1,n-1):
                if zahyo[j][i]=='x':
                    if count==0:
                        start = j
                    count +=1
                    if m_count<count:
                        m_count=count
                        f_start = start
                        f_end = j
                else:
                count = 0
            if max_count<m_count:
                t_max_count = m_count
                t_memo=i+1
                t_final_start = f_start
                t_final_end = f_end+1
    # 縦と横の最大値同士を比較
    if y_max_count>t_max_count:
        max_count = y_max_count
        memo= y_memo
        final_start = y_final_start
        final_end = y_final_end
    else:
        max_count = t_max_count
        memo= t_memo
        final_start = t_final_start
        final_end = t_final_end
# 変換座標の表示
print(memo, final_start)
print(memo, final_end+1)
for i in range(final_start, final_end):
    zahyo[memo-1][i] = '.'
