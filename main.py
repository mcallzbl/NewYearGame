from UIUtils import UIUtils
from DataUtils import DataUtils

if __name__ == "__main__":
    data = DataUtils.getInstance()
    ui = UIUtils.getInstance()
    ui.showOn()
    data.closeConnection()