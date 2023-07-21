#How to read and write a normal file
with open("Pnewfile.txt",mode="r",encoding="utf-8") as s_file:
    
    words_all=[]
    
    for line in s_file.readlines():
        print(line)
        words=line.strip().split(" ")
        words_all+=words
        uniq_words=set(words_all)
    print(len(words_all))
    print(len(uniq_words))
    

    with open("Puniqfile.txt",mode="w") as w_file:
        for word in sorted(uniq_words):
            w_file.write(word+"\n")
            
print("Finished")