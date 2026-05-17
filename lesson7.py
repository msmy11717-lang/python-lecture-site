import os
import shutil

# 整理したいフォルダを指定
target_folder = r"C:\Users\msmy1\OneDrive\デスクトップ\test_folder"

# 拡張子とフォルダ名の対応表（辞書）
folder_map = {
    ".pdf":  "PDF",
    ".xlsx": "Excel",
    ".csv":  "CSV",
    ".docx": "Word",
    ".png":  "画像",
    ".jpg":  "画像",
    ".mp4":  "動画",
    ".zip":  "圧縮ファイル",
}

# フォルダ内のファイルを一覧取得
files = os.listdir(target_folder)

for file in files:
    full_path = os.path.join(target_folder, file)

    # フォルダは除外してファイルだけ処理する
    if not os.path.isfile(full_path):
        continue

    # 拡張子を取得（例：.pdf）
    _, ext = os.path.splitext(file)
    ext = ext.lower()  # 大文字小文字を統一

    # 対応するフォルダ名を取得
    # 辞書にない拡張子は「その他」に入れる
    folder_name = folder_map.get(ext, "その他")

    # 移動先フォルダのパスを作成
    dest_folder = os.path.join(target_folder, folder_name)

    # フォルダがなければ作成
    os.makedirs(dest_folder, exist_ok=True)

    # ファイルを移動
    dest_path = os.path.join(dest_folder, file)
    shutil.move(full_path, dest_path)
    print(f"{file} → {folder_name}/")

print("整理完了")