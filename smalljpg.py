from PIL import Image

def compress_image(input_path, output_path, target_size_mb=1):
    target_size_bytes = target_size_mb * 1024 * 1024  # 將 MB 換算成 Bytes
    quality = 95  # 初始壓縮品質設定
    
    # 開啟圖片
    img = Image.open(input_path)
    
    # 不斷降低圖片品質，直到檔案大小小於目標大小
    while True:
        # 儲存圖片到暫存檔案中
        img.save(output_path, format="JPEG", quality=quality)
        
        # 檢查檔案大小
        file_size = output_path.stat().st_size  # 取得當前檔案大小
        
        if file_size <= target_size_bytes or quality <= 10:
            # 如果檔案大小已符合目標，或品質低於10（避免過度壓縮），結束壓縮
            break
        
        # 否則降低品質，繼續壓縮
        quality -= 5
    
    print(f"圖片已壓縮至 {file_size / (1024 * 1024):.2f} MB")

# 範例使用
from pathlib import Path

input_path = Path("p1.jpg")  # 替換成上傳的圖片路徑
output_path = Path("p2.jpg")  # 儲存的壓縮後圖片路徑
compress_image(input_path, output_path)
