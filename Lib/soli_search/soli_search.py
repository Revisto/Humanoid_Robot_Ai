import pandas as pd
from random import choice
def soli_search(inp,path):
    def sim_word(word_1,word_2):
        def phrase_builder(index_1,index_2,word):
            s=""
            for i in range(index_1,index_2+1):
                s+=word[i]
            return s
        best=0
        for index_1 in range(len(word_1)):
            for index_2 in range(index_1,len(word_1)):
                phrase_1=phrase_builder(index_1,index_2,word_1)
                for j1 in range(len(word_2)):
                    for j2 in range(j1,len(word_2)):
                        phrase_2=phrase_builder(j1,j2,word_2)
                        if phrase_1==phrase_2 and len(phrase_1)>best:
                            best=len(phrase_1)
        return best*2*100//(len(word_1)+len(word_2))
    def similarity(inp,in2):
        inp=inp.split(" ")
        in2=in2.split(" ")
        total=0
        for i in inp:
            for j in in2:
                if sim_word(i,j)>65:
                    total+=1
        if total==0:
            return 0
        return total*100//len(in2)
    df=pd.read_json(path)
    l_inp=df["input"]
    l_out=df["output"]
    #l_tag=df["tag"]
    best=None
    best_score=0
    for i in range(len(l_inp)):
        if similarity(inp,l_inp[i])>65 and similarity(inp,l_inp[i])>best_score:
            best=i
            best_score=similarity(inp,l_inp[i])
    if best==None:
        return False
    else:
        print(best_score)
        return choice(l_out[best])








while True:
    print(soli_search(input('input: '),"/home/parsa/Pyrust/soli_search/extra_data_1.json"))