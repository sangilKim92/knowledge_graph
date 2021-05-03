def tokenize(text):
    import re
    if not texts:
        return
    
    answer = []
    for text in texts:
        if not isinstance(text,str):
            continue
        URL_PATTERN = re.compile('((http|https|ftp):\/\/)?(www.)?[a-zA-Z0-9-_]+\.[a-zA-Z]+(\/[a-zA-Z0-9-_.=&/가-힣]+)?')
        DATE_PATTERN = re.compile(r"(\d{2,4})(\.|\/|\s)(\d{1,2})(\.|\/|\s)(\d{1,2})(\.|\/|\s)?([월화수목금토일])?(요일)? ")
        TEL_PATTERN = re.compile("(\d{2,3})(-|\.| )+(\d{3,4})(-|\.| )+(\d{3,4})")
        EMAIL_PATTERN = re.compile('([a-zA-Z0-9]+)@([a-zA-Z0-9]+)\.([a-z]{2,3})')
        MULTIPLE_CHAR = re.compile(r'(.)\1+')

        text = re.sub(URL_PATTERN, 'URL',text)
        text = re.sub(DATE_PATTERN,'DATETIME',text)
        text = re.sub(TEL_PATTERN, 'TEL ', text)
        text = re.sub(EMAIL_PATTERN, 'EMAIL', text)
        text = re.sub(MULTIPLE_CHAR, r'\1\1',text)
        answer.append(text)
    return answer

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