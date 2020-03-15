def count_words(sentence):
    c = dict()
   
    sep = sentence.replace(',',' ').replace('\n','').replace(':','').replace('@','').replace('_',' ').replace('.','').replace('!','').replace('&','').replace('^','').replace('$','').replace('%','').split()

    for word in sep:

        if word.count("'") == 2:
            new = word.replace("'","")
            if new.lower() in c:
                c[new.lower()] +=1
            else:
                c[new.lower()] = 1
            continue
    
        else:    
            if word.lower() in c:
                c[word.lower()] += 1

            else:
                c[word.lower()] = 1

    return c
