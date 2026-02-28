# 物件邊界框密度熱力圖產生器

**基礎環境設置**
```
pip install numpy matplotlib tqdm
```

**選擇檔案**
+ analyze_heatmap.py為有刻度版本
+ analyze_heatmap_noscale.py為無刻度版本

**指令執行**
+ 以無刻度版本為例
```
python analyze_heatmap_noscale.py
```

**使用操作**
+ 設定路徑與參數：\
  打開所需程式碼（例如 analyze_heatmap.py），找到 ====== 設定區域 ====== 區塊，依據環境修改以下變數：
```
# 輸入：存放 XML 標註檔的資料夾路徑
XML_FOLDER_PATH = r'C:\Users\user\Downloads\Cityscapes_VOC_dataset\VOC2007\Annotations' 

# 輸出：熱力圖圖片要存到哪裡
OUTPUT_FOLDER = r'C:\Users\user\Downloads\analyze_bbox\bbox_results'

# 影像解析度 (請依照原始圖片大小設定)
IMG_WIDTH = 2048
IMG_HEIGHT = 1024

# 要分析的類別清單
TARGET_CLASSES = [
    'car', 'person', 'rider', 'bicycle', 
    'motorcycle', 'truck', 'train', 'bus'
]
```

**生成結果**
+ 有刻度版本範例
<img src="https://github.com/ccuvislab/Draw_bbox_heatmap/blob/main/Picture/motorcycle_heatmap.png" width="70%" >

+ 無刻度版本範例
<img src="https://github.com/ccuvislab/Draw_bbox_heatmap/blob/main/Picture/motorcycle_city_heatmap.png" width="70%" >

# BBox Density Heatmap Generator

**Environment Setup**
```
pip install numpy matplotlib tqdm
```

**File Selection**
+ analyze_heatmap.py：Version with axis scales.
+ analyze_heatmap_noscale.py：Version without axis scales.

**Execution**
+ Example using the non-scaled version
```
python analyze_heatmap_noscale.py
```

**Usage**
+ Set paths and parameters：\
  Open the desired script（e.g., analyze_heatmap.py），locate the ====== 設定區域 ====== block, and modify the following variables according to your environment：
```
# Input: Folder path containing the XML annotation files
XML_FOLDER_PATH = r'C:\Users\user\Downloads\Cityscapes_VOC_dataset\VOC2007\Annotations' 

# Output: Folder path to save the heatmap images
OUTPUT_FOLDER = r'C:\Users\user\Downloads\analyze_bbox\bbox_results'

# Image Resolution (Please set according to the original image size)
IMG_WIDTH = 2048
IMG_HEIGHT = 1024

# List of classes to analyze
TARGET_CLASSES = [
    'car', 'person', 'rider', 'bicycle', 
    'motorcycle', 'truck', 'train', 'bus'
]
```

**Results**
+ Example with axis scales
<img src="https://github.com/ccuvislab/Draw_bbox_heatmap/blob/main/Picture/motorcycle_heatmap.png" width="70%" >

+ Example without axis scales
<img src="https://github.com/ccuvislab/Draw_bbox_heatmap/blob/main/Picture/motorcycle_city_heatmap.png" width="70%" >
