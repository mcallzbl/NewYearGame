import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime, timedelta
import json
import os
from UIUtils import UIUtils
from DataUtils import DataUtils

if __name__ == "__main__":
    data = DataUtils.getInstance()
    ui = UIUtils.getInstance()
    ui.showOn()
    data.closeConnection()