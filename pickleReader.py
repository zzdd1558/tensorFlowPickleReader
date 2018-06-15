# -*- coding:utf-8 -*-

import numpy as np
import pickle

'''
    Method
    __init__ : class 생성자.
    read_pickle : pickleFilePath를 받아 해당 pickle데이터를 색상반전후 data return

    2018.06.15 (금) 수정
    최 윤진.
'''

class Pickle :

    def __init__(self):
        print("Pickle __init__")

    '''
        test.pickle 데이터 test.pickle 4,872개
        train.pickle 데이터 train.pickle 51,898개
        
        @:parameter 
         - pickleFilePath : 파일의 경로를 받는다.
         - readWay : 읽기 방식 저는 r+t 사용 ( 읽기와 동시에 이어쓰기 )
    '''
    def read_pickle(self, pickleFilePath , readWay):
        'r+t'
        with open(pickleFilePath , readWay) as f:
            data = pickle.load(f)

            # 이미지 이진화가 흰배경에 검정 글씨로 되있지만 MNIST 데이터는 검정바탕에 흰 글시라서 색상 반전을 위해 -1
            # -1을 하는 이유는 np.array 1,0되있을때 -1을하여 빼주면 0 , 255가 됨.
            for idx , _ in enumerate(data):
                data[idx]["features"] = np.array(abs(data[idx]["features"] - 1))

            f.close()
        return data

if __name__ == "__main__":
    print ('Pickle Class Main Success')
else :
    print('Pickle Class Import Success')
