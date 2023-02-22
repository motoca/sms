with open('todosSMS.csv', 'r') as file1, open('enviados.txt', 'r') as file2, open('diff.txt', 'w') as diff_file:
    file1_lines = set(file1.readlines())
    print(f"TODOS SMS = {len(file1_lines)}")
    file2_lines = set(file2.readlines())
    print(f"ENVIADOS = {len(file2_lines)}")
    diff_lines = file1_lines - file2_lines
    print("ANALISANDO DISFERENÇAS DO ARQUIVO...")
    print(f"DIFF = {len(diff_lines)}")
    
    print("ESCREVENDO...}")
    cont = 0
    for line in diff_lines:
        cont+=1
        diff_file.write(line)
        print("\033[K", f"LINHA: {line} - TOTAL: {cont}", end="\r")