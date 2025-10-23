import os
import time

# Hàm xóa màn hình (tùy hệ điều hành)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ===== Hình 1 =====
hinh1 = """
         
      *  
      * *    
      * * * 
* * * * * * * 
* * *  
* *
*
"""

# ===== Hình 2 =====
hinh2 = """
      *  
      * *    
      *   * 
* * * * * * * 
*   *  
* *
*
"""

# ===== Hình 3 =====
hinh3 = """
        * * * *
        * * *
        * *
        * 
      * *
    * * *
  * * * *
"""

# ===== Hình 4 =====
hinh4 = """
        * * * *
        *   *
        * *
        * 
      * *
    *   *
  * * * *
"""

# Danh sách các hình
cac_hinh = [hinh1, hinh2, hinh3, hinh4]

# Hiển thị từng hình cách nhau 5 giây
for hinh in cac_hinh:
    clear()
    print(hinh)
    time.sleep(5)
