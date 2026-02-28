import os
import glob
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# ================= 設定區域 =================
XML_FOLDER_PATH = r'C:\Users\user\Downloads\bdd100k\Annotations' 

OUTPUT_FOLDER = r'C:\Users\user\Downloads\analyze_bbox\bbox_results'

IMG_WIDTH = 1280
IMG_HEIGHT = 720

TARGET_CLASSES = [
    'car', 'person', 'rider', 'bicycle', 
    'motorcycle', 'truck', 'train', 'bus'
]
# ===========================================

def parse_xml_and_accumulate(xml_files, heatmaps):
    """讀取 XML 並累積 Heatmap 數值"""
    print(f"開始分析 {len(xml_files)} 個 XML 檔案...")
    
    for xml_file in tqdm(xml_files):
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            for obj in root.findall('object'):
                class_name = obj.find('name').text
                
                if class_name in TARGET_CLASSES:
                    bndbox = obj.find('bndbox')
                    
                    # 讀取座標並確保數值為整數
                    xmin = int(float(bndbox.find('xmin').text))
                    ymin = int(float(bndbox.find('ymin').text))
                    xmax = int(float(bndbox.find('xmax').text))
                    ymax = int(float(bndbox.find('ymax').text))
                    
                    # 邊界檢查 (Clip)
                    xmin = max(0, min(xmin, IMG_WIDTH - 1))
                    xmax = max(0, min(xmax, IMG_WIDTH - 1))
                    ymin = max(0, min(ymin, IMG_HEIGHT - 1))
                    ymax = max(0, min(ymax, IMG_HEIGHT - 1))
                    
                    # 累積熱度
                    heatmaps[class_name][ymin:ymax, xmin:xmax] += 1
                    
        except Exception as e:
            print(f"Error parsing {xml_file}: {e}")

def plot_and_save_heatmaps(heatmaps):
    """繪製並儲存熱力圖"""
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        
    print(f"\n正在生成分析報告與圖片至 {OUTPUT_FOLDER} ...")
    
    for cls in TARGET_CLASSES:
        heatmap = heatmaps[cls]
        
        # 如果該類別完全沒有出現，跳過
        if np.max(heatmap) == 0:
            print(f"類別 [{cls}] 未偵測到任何數據。")
            continue
            
        # 1. 找出最密集的點
        y_max, x_max = np.unravel_index(np.argmax(heatmap), heatmap.shape)
        max_val = np.max(heatmap)
        
        print(f"類別: {cls:<12} | 最密集座標 (x,y): ({x_max}, {y_max}) | 最大重疊數: {int(max_val)}")
        
        # 2. 繪圖
        plt.figure(figsize=(12, 6))
        
        # 使用 'jet' 配色
        plt.imshow(heatmap, cmap='jet', interpolation='nearest', aspect='auto')
        
        # ticks=[] 代表不顯示任何數字刻度
        plt.colorbar(ticks=[])
        
        # 標記最密集點
        plt.plot(x_max, y_max, 'w+', markersize=15, markeredgewidth=2, label='Max Density Center')
        
        plt.title(f'Density Heatmap: {cls} (Size: {IMG_WIDTH}x{IMG_HEIGHT})')
        
        # 關閉主圖的座標軸 (刻度與邊框)
        plt.axis('off') 
        
        plt.legend()
        
        # 儲存圖片
        save_path = os.path.join(OUTPUT_FOLDER, f'{cls}_bdd_heatmap.png')
        plt.savefig(save_path, dpi=150, bbox_inches='tight', pad_inches=0.1)
        plt.close()

if __name__ == "__main__":
    # 1. 初始化每個類別的 Heatmap 矩陣
    class_heatmaps = {cls: np.zeros((IMG_HEIGHT, IMG_WIDTH), dtype=np.float32) for cls in TARGET_CLASSES}
    
    # 2. 獲取所有 xml 檔案路徑
    xml_files = glob.glob(os.path.join(XML_FOLDER_PATH, '*.xml'))
    
    if not xml_files:
        print(f"錯誤：在 {XML_FOLDER_PATH} 找不到任何 .xml 檔案。")
    else:
        # 3. 執行分析
        parse_xml_and_accumulate(xml_files, class_heatmaps)
        
        # 4. 輸出結果
        plot_and_save_heatmaps(class_heatmaps)
        print("\n所有分析完成！")