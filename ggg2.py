import os

def convert_crlf_to_lf(file_path):
    """ 将 TXT 文件中的 CRLF 换行符转换为 LF """
    if not os.path.exists(file_path):
        print(f'File {file_path} does not exist.')
        return
    
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        content = file.read()
    
    # 替换 CRLF（\r\n）为 LF（\n）
    content = content.replace('\r\n', '\n')
    
    # 将转换后的内容写回到文件
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        file.write(content)
    
    print(f'Converted CRLF to LF in {file_path}')

def main():
    """ 处理当前目录下的所有 .txt 文件 """
    for filename in os.listdir('.'):
        if filename.endswith('.txt'):
            convert_crlf_to_lf(filename)

if __name__ == '__main__':
    main()
