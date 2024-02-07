# Date 2024-2-07-12
# version 1.0
# by mcallzbl
from UIUtils import UIUtils
from DataUtils import DataUtils

if __name__ == "__main__":
    data = DataUtils.getInstance()
    ui = UIUtils.getInstance()
    ui.showOn()
    data.closeConnection()