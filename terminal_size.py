import os
import shutil
import time
while(True):
# Option 1: Using os.get_terminal_size
  size = os.get_terminal_size()
  print(f"Columns: {size.columns}, Rows: {size.lines}")
  time.sleep(.5)
# # Option 2: Using shutil.get_terminal_size
# size = shutil.get_terminal_size()
# print(f"Columns: {size.columns}, Rows: {size.lines}")
