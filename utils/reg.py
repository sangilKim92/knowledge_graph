def tokenize(text):
    import re
    
    URL_PATTERN = re.compile('((http|https|ftp):\/\/)?(www.)?[a-zA-Z0-9-_]+\.[a-zA-Z]+(\/[a-zA-Z0-9-_.=&/가-힣]+)?')
    MULTIPLE_CHAR = re.compile(r'(.)\1+')
    
    text = (re.sub(URL_PATTERN, 'url',text))
    text = re.sub(MULTIPLE_CHAR,r'\1\1',text)
    return text
    
def read_korquad():
    with open(glob.glob(PATH)[0],'r',encoding='utf-8') as f, open('/home/data/data/KorQuAD/process/process_korquad_train.txt','w',encoding='utf-8') as f2:
    dataset_json = json.loads(f.read())
    dataset = dataset_json['data']
    
    for article in dataset:
        w_line = []
        #for paragraph in article['paragraphs']:
        w_lines.append(article['context'])
         
        for qa in article['qas']:   
            q_text = qa['question']
            a_text = qa['answer']['text']
            w_lines.append(q_text+ " "+ a_text)
        for line in w_lines:
            f2.writelines(line + "\n")