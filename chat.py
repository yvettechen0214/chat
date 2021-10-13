#讀取檔案
def read_file(file_name):
    chat = []
    with open(file_name, "r", encoding = "utf-8-sig") as f:
        for line in f:
            content = line.strip()
            chat.append(content)
    return chat

def convert(content):
    new = []
    person = None #為了防止資料第一行不是人名，而導致當掉
    for line in content:
        if "Allen" in line:
            person = "Allen"
            continue 
        elif "Tom" in line:
            person = "Tom"
            continue

        if person: #可以解讀成，若person有值，才做下一行動作
            new.append(person + ":" + line)
    return new

#寫入
def write_file(file_name, pre_output):
    with open(file_name, "w", encoding = "utf-8-sig") as f:
        for p in pre_output:
            f.write(p + "\n")

#main function
def main():
    file_name = "input.txt"
    content = read_file(file_name)
    #print(content)
    pre_output = convert(content)
    write_file("output_new.txt", pre_output)

main()