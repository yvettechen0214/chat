#讀取檔案
def read_file(file_name):
    chat = []
    with open(file_name, "r", encoding = "utf-8-sig") as f:
        for line in f:
            content = line.strip()
            chat.append(content)
    return chat


def convert(content):
    person = None #為了防止資料第一行不是人名，而導致當掉
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in content:
        s = line.split(" ")  #切割完會變清單
        time = s[0]
        name = s[1]
        if name == "Allen":
            if s[2] == "貼圖":
                allen_sticker_count += 1
            elif s[2] == "圖片":
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == "Viki":
            if s[2] == "貼圖":
                viki_sticker_count += 1
            elif s[2] == "圖片":
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print("allen說了", allen_word_count,"傳了", allen_sticker_count,"貼圖", allen_image_count, "圖片")
    print("viki說了", viki_word_count,"傳了", viki_sticker_count,"貼圖", viki_image_count, "圖片")
        #print(s)
    

#寫入
def write_file(file_name, pre_output):
    with open(file_name, "w", encoding = "utf-8-sig") as f:
        for p in pre_output:
            f.write(p + "\n")


#main function
def main():
    file_name = "LINE-Viki.txt"
    content = read_file(file_name)
    #print(content)
    pre_output = convert(content)
    #write_file("output_new.txt", pre_output)

main()