def get_non_empty_lines(lines):
    """
        returns non empty lines from a list of lines
    """
    clean_lines = []
    for line in lines:
        str_line = line.strip()
        if str_line:
            clean_lines.append(str_line)            
    return clean_lines

def get_txt_lines(data_dir):
    """
        Read text lines from gutenberg tests
        returns (text_ls,fname_ls) where 
        text_ls = input_text_lines and fname_ls = list of file names
    """
    text_ls = []
    fname_ls = []
    for fn in os.listdir(data_dir):
        full_fn = os.path.join(data_dir,fn)
        with open(full_fn,encoding="utf-8",errors="ignore") as f:
            content = f.readlines()
            content = get_non_empty_lines(content)
            text_ls += content
            ### dont add .txt to the file
            fname_ls += [fn[:-4]]*len(content)
    
    return text_ls, fname_ls    

data_dir = "/home/hucc/books"
print("File Read Time:")
# %time 
txt_ls,fname_ls = get_txt_lines(data_dir)
df = cudf.DataFrame()

print("\nCUDF  Creation Time:")
# %time 
df['text'] = nvstrings.to_device(txt_ls)

df['label'] = nvstrings.to_device(fname_ls)
title_label_df = df['label'].str.split('___')
df['author'] = title_label_df[0]

df['title'] = title_label_df[1]
df = df.drop(labels=['label'])

df.head(10).to_pandas()