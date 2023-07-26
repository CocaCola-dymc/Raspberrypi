import json

#recv={1:30, 2:65, 3:85, 4:14, 5:98, 6:55}
recv=[{'probe':1,'value':30},{'probe':2,'value':65},{'probe':3,'value':85},
      {'probe':4,'value':14},{'probe':5,'value':98},{'probe':6,'value':55}]
if __name__ == '__main__':
    # 若传入的数据为str类型需要将它转成dict类型
    # result = json.loads(jsondata)
    print(recv)
    probe=[]
    value=[]
    
    for data in recv:
        print(data)
        probe.append(data['probe'])
        value.append(data['value'])
    print(probe)
    print(value)
    
    