def my_add_fun( input1 , input2):  #偷偷定義一下輸入的tpye 一定是要可被計算的 int
    input_sum = input1 + input2
    return input_sum


def my_judge(data_num, threashold):  #偷偷註記一下,data_num, threashold 是可以被比較的 int /float
    if data_num > threashold:
        summary = f'您的數字{data_num}會大於{threashold}'
    else:
        summary = f'您的數字{data_num}會小於等於{threashold}'
    return summary