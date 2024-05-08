import random

def f(in_path, o_path):
    o_file = open(o_path, 'a')
    with open(in_path) as file:
        for i, _ in enumerate(file):
            txt =  1 if random.random() < 0.8 else 0 
            o_file.write(str(txt) + '\n')
    o_file.close()

f('models/2/CENET-Part2-TKGI/data/YAGO/train.txt', 'models/2/CENET-Part2-TKGI/data/YAGO/train-llm.txt')