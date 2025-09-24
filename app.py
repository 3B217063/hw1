import os
import shutil

# 專案目錄為當前腳本所在目錄
project_root = os.path.dirname(os.path.abspath(__file__))

# 指定已存在的 Downloads 資料夾路徑
downloads_folder = os.path.join(project_root, 'Downloads')

# 定義分類副檔名
categories = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Others': []  # 不符合以上副檔名的，會歸到這裡
}

# 建立子資料夾（如果尚未存在）
for category in categories:
    category_path = os.path.join(downloads_folder, category)
    os.makedirs(category_path, exist_ok=True)

# 開始分類 Downloads 資料夾中的檔案
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    # 跳過分類資料夾本身
    if os.path.isdir(file_path):
        continue

    # 取得副檔名並轉為小寫
    file_ext = os.path.splitext(filename)[1].lower()
    moved = False

    # 嘗試分類到相對應的資料夾
    for category, extensions in categories.items():
        if file_ext in extensions:
            target_path = os.path.join(downloads_folder, category, filename)
            shutil.move(file_path, target_path)
            print(f"✅ Moved '{filename}' to '{category}/'")
            moved = True
            break

    # 如果沒找到對應類別，移到 Others
    if not moved:
        target_path = os.path.join(downloads_folder, 'Others', filename)
        shutil.move(file_path, target_path)
        print(f"📦 Moved '{filename}' to 'Others/'")

print("\n📁 檔案分類完成！")
