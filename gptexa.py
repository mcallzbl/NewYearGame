import sys
import openai
from Controller import Controller
from datetime import datetime
ctrl = Controller.getInstance()
openai.api_key = "sk-lJismDvRUX1PCmbfD6Cc6cC83e654148AdE00aB0FcFa4e5f"  # 使用你的API密钥
openai.api_base = "http://211.159.163.132:3000/v1"  # 使用正确的API基础URL
ctrl = Controller.getInstance()
ctrl.setCurrentModule('scene')


def check_date():
    current_time_str = ctrl.getTime()
    try:
        current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M")
    
    target_time = datetime(current_time.year, 2, 6)
    return current_time < target_time
def chat_with_gpt3(user_input):
    introduction = "我是一个人工智能助手，我可以帮助你规划你的假期。请你告诉我你的假期安排，我会将你的安排拆分成多个小的事项，并逐行输出。"

    conversation_history = [
        {"role": "system", "content": introduction},
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": "这个输入是否包含不恰当或冒犯性的内容？如果是，请回答'是'。"}
    ]

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    gpt_response = chat_completion.choices[0].message["content"]
    if "是" in gpt_response:
        ctrl.addStoryText("检测到不合适的输入，请重新输入。")
        ask_for_plan()
    else:
        # 如果输入有效，格式化并输出用户的计划
        formatted_input = user_input.replace('，', '\n').replace(',', '\n').strip()
        global global_plans
        global_plans = formatted_input.split('\n')
        ctrl.appendToFile("plan.txt", formatted_input + "\n")
        ctrl.addStoryText("已保存")
        create_action_buttons(global_plans)

def generate_encouragement(plan):
    prompt = f"请为以下计划项生成一段鼓励的话：\n计划项：{plan}\n鼓励的话："
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=60
    )
    encouragement = response.choices[0].text.strip()
    ctrl.addStoryText(encouragement)
    ctrl.setImmediateOutput()
    # 检查是否所有计划都已经讨论过
    global global_plans
    global_plans.remove(plan)
    if not global_plans:
        # 如果所有计划都讨论完毕，递进到下一天
        ctrl.addTime(days=1)
        if check_date():
            # 如果还没到2月6日，再次询问计划
            ask_for_plan()
        else:
            # 如果已经到达2月6日，结束循环
            ctrl.addStoryText("我们已经完成了所有的计划，现在是2月6日。")

def create_action_buttons(plans):
    ctrl.clearPanel()
    for plan in plans:
        if plan.strip() and plan not in completed_plans:
            ctrl.addButton(plan, lambda plan=plan: on_button_click(plan))

def on_button_click(plan):
    generate_encouragement(plan)
    completed_plans.append(plan)
    update_buttons()

def update_buttons():
    ctrl.clearPanel()
    for plan in global_plans:
        if plan in completed_plans:
            ctrl.addButton(plan + " - 已完成", lambda: None)
        else:
            ctrl.addButton(plan, lambda plan=plan: on_button_click(plan))
    check_all_completed()

def check_all_completed():
    if all(plan in completed_plans for plan in global_plans):
        ctrl.addTime(days=1)
        if check_date():
            start_new_day()
        else:
            ctrl.addStoryText("我们已经完成了所有的计划，现在是2月6日。")

def start_new_day():
    global completed_plans
    completed_plans = []
    create_action_buttons(global_plans)

def ask_for_plan():
    ctrl.clearPanel()
    ctrl.addStoryText("请输入您的假期安排：")
    ctrl.addEntry(submit_callback=chat_with_gpt3, placeholder_text="请在这里输入...")

def plan():
    if check_date():
        ask_for_plan()
    else:
        ctrl.addStoryText("时间已经到达2月6日。")


