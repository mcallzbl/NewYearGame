import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime, timedelta
import json
import os
from UIUtils import UIUtils
from DataUtils import DataUtils

# 获取当前脚本的完整路径
script_path = os.path.realpath(__file__)
# 获取脚本所在目录
script_dir = os.path.dirname(script_path)

if __name__ == "__main__":
    data = DataUtils.getInstance()
    ui = UIUtils.getInstance()
    ui.showOn()
    data.closeConnection()