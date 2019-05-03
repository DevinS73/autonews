import random
def wordtolist(file,encoding='utf-8',errors='replace'):
    list=[]
    with open(file,encoding='utf-8',errors='replace') as file:
        for line in file:
            for word in line.strip().split():
                list+=[word]
    return list
def markov_dictionary(words):
    dictionary={}
    for i in range(1,len(words)-1):
        if words[i-1]+' '+words[i] in dictionary:
            dictionary[words[i-1]+' '+words[i]]+=[words[i+1]]
        else:
            dictionary[words[i-1]+' '+words[i]]=[words[i+1]]
    return dictionary
def new_file_maker(words,dictionary,length):
    new=[words[0],words[1]]
    i=0
    string=''
    while len(new)!=length:
        if new[i]+' '+new[i+1] not in dictionary:
            break
        else:
            new+=[random.choice(dictionary[new[i]+' '+new[i+1]])]
        i+=1
    for word in new:
        string+=word+' '
    return string[:len(string)-1]
def main():
    file=input('Which file would you like to use? ')
    try:
        words=wordtolist(file)
    except Exception:
        print('Error: File not found')
        return
    dictionary=markov_dictionary(words)
    string=new_file_maker(words,dictionary,500)
    print(string)
    newfile=input('Enter the new file name: ')
    if newfile=='':
        return
    x=0
    if len(string)>80:
        if string[79]==' ':
            filestring=string[:80]+'\n'
        else:
            while string[79-x]!=' ':
                x+=1
            filestring=string[:80-x]+'\n'
        index=80-x
        end=index+80
        while True:
            if end>=len(string):
                filestring+=string[index:]
                break
            elif string[end]==' ':
                filestring+=string[index:end+1]+'\n'
                index=end+1
                end+=80
            else:
                end-=1
    with open(newfile,"w") as file:
        file.write(filestring)
        
def markov(file,newfile,length):
    words=wordtolist(file)
    dictionary=markov_dictionary(words)
    string=new_file_maker(words,dictionary,length)
    x=0
    if len(string)>80:
        if string[79]==' ':
            filestring=string[:80]+'\n'
        else:
            while string[79-x]!=' ':
                x+=1
            filestring=string[:80-x]+'\n'
        index=80-x
        end=index+80
        while True:
            if end>=len(string):
                filestring+=string[index:]
                break
            elif string[end]==' ':
                filestring+=string[index:end+1]+'\n'
                index=end+1
                end+=80
            else:
                end-=1
    with open(newfile,"w") as file:
        try:
            print(filestring+'...')
            try:
                file.write(filestring)
                if newfile!='titles1.txt':
                    pass
                else:
                    print(f'This text can be viewed in {newfile}')
            except Exception:
                pass
        except Exception:
            print(string+'...')
            try:
                file.write(string)
                if newfile!='titles1.txt':
                    pass
                else:
                    print(f'This text can be viewed in {newfile}')
            except Exception:
                pass
    return newfile