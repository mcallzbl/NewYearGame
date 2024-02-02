import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime, timedelta
import json
import os


# 获取当前脚本的完整路径
script_path = os.path.realpath(__file__)
# 获取脚本所在目录
script_dir = os.path.dirname(script_path)

class StoryApp:
    def __init__(self, master, story_data):
        self.master = master
        self.story_data = story_data
        self.current_scene_id = 'scene1'
        self.current_date = datetime.strptime(story_data['start_date'], "%Y-%m-%d")
        self.current_location = story_data['start_location']
        self.current_money = story_data['initial_money']
        self.current_time = datetime.fromisoformat(story_data['initial_time'])
        self.initialize_gui()
        self.display_scene()

    def initialize_gui(self):
        self.master.title("No game no life")
        
        self.story_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=50, height=10)
        self.story_text.pack(pady=10)
        
        self.options_frame = tk.Frame(self.master)
        self.options_frame.pack(pady=5)

        self.date_label = tk.Label(self.master, text="当前时间: " + self.current_time.strftime("%Y-%m-%d %H:%M"))
        self.date_label.pack()
        
        
        self.location_label = tk.Label(self.master, text="位置: " + self.current_location)
        self.location_label.pack()

        self.money_label = tk.Label(self.master, text="金钱: ￥" + str(self.current_money))
        self.money_label.pack()

    def display_scene(self):
        print(self.current_scene_id)
        scene = next((scene for scene in self.story_data['scenes'] if scene['id'] == self.current_scene_id), None)
        if scene is None:
            self.story_text.insert(tk.END, "Scene not found.\n")
            return

        self.story_text.delete(1.0, tk.END)
        self.story_text.insert(tk.END, scene['description'] + "\n\n")
        
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        for idx, option in enumerate(scene['options']):
            btn = tk.Button(self.options_frame, text=option['text'], command=lambda option=option: self.handle_option(option))
            btn.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

    def handle_option(self, option):
    # 检查option是否为字典并且含有'text'字段
        if isinstance(option, dict) and "text" in option:
            self.story_text.insert(tk.END, option['text'] + "\n")
            # 如果还有金钱变化，更新金钱显示
            result = option['result']
            if "money_change" in result:
                self.current_money += result['money_change']
                self.money_label.config(text="金钱: ￥" + str(self.current_money))
            # 如果有场景变化，更新场景
            
            if "scene" in result:
                self.current_scene_id = result['scene']
                self.display_scene()

            if "time_change" in result:
                self.current_time += timedelta(hours=result['time_change'])
                # 更新GUI中的时间显示，假设有一个显示时间的标签
                self.date_label.config(text="当前时间: " + self.current_time.strftime("%Y-%m-%d %H:%M"))

            if "location" in result:
                self.current_location = result['location']
                # 更新GUI中的位置显示，假设有一个显示位置的标签
                self.location_label.config(text="位置: " + self.current_location)

        # 如果option是字符串，直接处理
        elif isinstance(option, str):
            self.story_text.insert(tk.END, option + "\n")
        else:
            # 如果选项不是预期类型，可以在这里处理错误或者记录日志
            print("Unexpected option type")

        

def load_story(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == "__main__":
    story_path = script_dir+'\\story.json'  # 更改为你的JSON文件路径
    root = tk.Tk()
    story_data = load_story(story_path)
    app = StoryApp(root, story_data)
    root.mainloop()
