import os
def delete():
    # 指定したディレクトリ内のファイルを全て削除する
    dir_path = "original_receipt"
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

    dir_path = "templates/cut_out_receipt"
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)