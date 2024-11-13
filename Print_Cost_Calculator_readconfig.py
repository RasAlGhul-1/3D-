import tkinter as tk
import os
import json


# 文件路径
file_path = 'config.json'  # 替换成你的 JSON 配置文件路径

# 示例数据
test_data = """{
    "program_explanation_json": {
      "value": "\\n本程序仅用于计算3D打印时所产生的费用。包括：机器折旧费用、电费、人工成本、耗材成本。\\n其中：机器购买价格以拓竹P1SC为准即5500元，寿命为3D打印机的平均寿命1500小时，功率按照800瓦计算，电费默认按照0.5元每度计算，人工处理时间默认为0（可根据需要调整），每克耗材利润也为0（可根据需要调整），特殊值为修正值（会直接加在最终费用里）\\tn所有数值均可在config.json内进行配置，经常改动的数值（如：打印当前模型所需要的耗材）可以留空，基本不变的数值（如：我只有一台P1S，打印机费用是固定的）可以直接写死，避免每次重复输入",
      "remark": "程序最下方的红色说明"
    },
    "machine_cost_json": {
      "value": "5500",
      "remark": "机器购买价格（元），默认值为5500元"
    },
    "machine_lifespan_json": {
      "value": "1500",
      "remark": "机器寿命（小时），默认值为1500小时"
    },
    "machine_power_json": {
      "value": "800",
      "remark": "机器功率（瓦特），默认值为800瓦"
    },
    "electricity_cost_json": {
      "value": "0.5",
      "remark": "电费（元/度），默认值为0.5元每度"
    },
    "adjust_time_json": {
      "value": "0",
      "remark": "调整模型时间（小时），默认为0小时"
    },
    "slicing_time_json": {
      "value": "0",
      "remark": "切片时间（小时），默认为0小时"
    },
    "post_process_time_json": {
      "value": "0",
      "remark": "后期处理时间（小时），默认为0小时"
    },
    "material_price_json": {
      "value": "",
      "remark": "耗材价格（元/千克），默认为空"
    },
    "material_weight_json": {
      "value": "",
      "remark": "耗材重量（千克），默认为空"
    },
    "model_material_weight_json": {
      "value": "",
      "remark": "模型耗材重量（克），默认为空"
    },
    "profit_per_gram_json": {
      "value": "0",
      "remark": "每克耗材利润（元），默认值为0"
    },
    "print_time_json": {
      "value": "",
      "remark": "打印时间（小时），默认为空"
    },
    "operator_wage_json": {
      "value": "",
      "remark": "操作人员时薪（元）"
    },
    "special_value_json": {
      "value": "0",
      "remark": "特殊值（元），默认值为0"
    }
  }"""

# 检查文件是否存在
if not os.path.exists(file_path):
    # 如果文件不存在，创建并写入测试数据
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(test_data)
    print(f"{file_path} 不存在，已经创建并写入示例数据")
else:
    print(f"{file_path} 文件已存在")


def read_config_json(file_path, key):
    with open(file_path, 'r', encoding='utf-8') as file:
        config_data = json.load(file)  # 解析 JSON 数据
    # 获取特定键对应的值（如果存在）
    if key in config_data:
        value_data = config_data[key]['value']
        return value_data
    else:
        return None  # 如果键不存在，返回 None

def calculate_price():
    try:
        # 检查是否有空的输入框
        missing_fields = []
        
        # 获取输入框的值
        machine_cost = entry_machine_cost.get()
        machine_lifespan = entry_machine_lifespan.get()
        machine_power = entry_machine_power.get()
        electricity_cost = entry_electricity_cost.get()
        adjust_time = entry_adjust_time.get()
        slicing_time = entry_slicing_time.get()
        post_process_time = entry_post_process_time.get()
        material_price = entry_material_price.get()
        material_weight = entry_material_weight.get()
        model_material_weight = entry_model_material_weight.get()
        profit_per_gram = entry_profit_per_gram.get()
        print_time = entry_print_time.get()
        operator_hourly_wage = entry_operator_wage.get()
        special_value = entry_special_value.get()

        # 检查每个字段是否为空
        if not machine_cost:
            missing_fields.append("机器购买价格")
        if not machine_lifespan:
            missing_fields.append("机器寿命")
        if not machine_power:
            missing_fields.append("机器功率")
        if not electricity_cost:
            missing_fields.append("电费")
        if not adjust_time:
            missing_fields.append("调整模型时间")
        if not slicing_time:
            missing_fields.append("切片时间")
        if not post_process_time:
            missing_fields.append("后期处理时间")
        if not material_price:
            missing_fields.append("耗材价格")
        if not material_weight:
            missing_fields.append("耗材重量")
        if not model_material_weight:
            missing_fields.append("模型耗材重量")
        if not profit_per_gram:
            missing_fields.append("每g耗材利润")
        if not print_time:
            missing_fields.append("打印时间")
        if not operator_hourly_wage:
            missing_fields.append("操作人员时薪")
        if not special_value:
            missing_fields.append("特殊值")
        
        # 如果有必填字段为空，提示用户
        if missing_fields:
            output_box.config(state=tk.NORMAL)
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, f"以下字段不能为空： {', '.join(missing_fields)}")
            output_box.config(state=tk.DISABLED)
            output_box.tag_config("error", foreground="red")  # 红色提示
            output_box.tag_add("error", "1.0", "end")  # 应用红色提示到整个文本
            return
        
        # 如果没有空字段，继续进行计算
        machine_cost = float(machine_cost)
        machine_lifespan = float(machine_lifespan)
        machine_power = float(machine_power)
        electricity_cost = float(electricity_cost)
        adjust_time = parse_time(adjust_time)
        slicing_time = parse_time(slicing_time)
        post_process_time = parse_time(post_process_time)
        material_price = float(material_price)
        material_weight = float(material_weight) * 1000  # 将千克转换为克
        model_material_weight = float(model_material_weight)
        profit_per_gram = float(profit_per_gram)
        print_time = parse_time(print_time)
        operator_hourly_wage = float(operator_hourly_wage)
        special_value = float(special_value)

        machine_hourly_cost = machine_cost / machine_lifespan
        electricity_cost_per_hour = machine_power / 1000 * electricity_cost
        
        # 计算机器折旧和电费
        machine_depreciation_cost = machine_hourly_cost * print_time
        electricity_cost_total = electricity_cost_per_hour * print_time
        
        # 计算人工费用（不包括打印时间）
        labor_cost = (adjust_time + slicing_time + post_process_time) * operator_hourly_wage
        
        # 计算材料费用
        material_cost = (model_material_weight / material_weight) * material_price
        
        # 计算利润
        profit = model_material_weight * profit_per_gram

        # 计算总费用
        total_cost = (
            machine_depreciation_cost + 
            electricity_cost_total + 
            labor_cost + 
            material_cost + 
            profit + 
            special_value
        )
        output_box.tag_config("bold", font=("宋体", 10, "bold")) 
        output_text = (
            f"机器购买价格: {machine_cost}, 机器寿命: {machine_lifespan}, 机器功率: {machine_power}, 电费: {electricity_cost}, "
            f"调整模型时间: {adjust_time}h, 切片时间: {slicing_time}h, 后期处理时间: {post_process_time}h, "
            f"耗材价格: {material_price}, 耗材重量: {material_weight}g, 模型耗材重量: {model_material_weight}g, "
            f"每g耗材利润: {profit_per_gram}, 打印时间: {print_time}h, 操作人员时薪: {operator_hourly_wage}, 特殊值: {special_value}\n"
            #f"计算机器折旧: {machine_depreciation_cost}元, 电费: {electricity_cost_total}元, 人工费用: {labor_cost}元, 材料费用: {material_cost}元, 利润：{profit}元, 特殊值{special_value}元\n"
            f"总费用: {total_cost:.2f} 元"
        )

        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output_text)
        output_box.tag_add("bold", "1.0", "end")  # 将加粗标签应用到整个输出
        output_box.config(state=tk.DISABLED)
        output_box.tag_config("success", foreground="green")  # 绿色提示
        output_box.tag_add("success", "1.0", "end")  # 应用绿色提示到整个文本
    except ValueError:
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "输入无效，请检查所有字段。")
        output_box.config(state=tk.DISABLED)
        output_box.tag_config("error", foreground="red")  # 红色提示
        output_box.tag_add("error", "1.0", "end")  # 应用红色提示到整个文本

def parse_time(time_str):
    if not time_str:
        return 0
    hours, minutes = 0, 0
    if 'h' in time_str:
        hours = int(time_str.split('h')[0])
        if 'm' in time_str:
            minutes = int(time_str.split('h')[1].replace('m', ''))
    elif 'm' in time_str:
        minutes = int(time_str.replace('m', ''))
    return hours + minutes / 60

def on_entry_change(entry, default_value):
    current_value = entry.get()
    if current_value == str(default_value) or current_value == "":
        entry.config(fg='red')
    else:
        entry.config(fg='green')

window = tk.Tk()
window.title("3D 打印价格计算器")
window.geometry("650x550")  # 将窗口尺寸改为 700x500

# 设置 grid 配置，确保窗口内容居中
window.grid_rowconfigure(0, weight=1)  # 配置第一行占满
window.grid_columnconfigure(0, weight=1)  # 配置第一列占满
window.grid_rowconfigure(1, weight=1)  # 配置第二行占满
window.grid_columnconfigure(1, weight=1)  # 配置第二列占满

# 标签和输入框宽度调整
labels = [
    "机器购买价格（元）：", "机器寿命（h）：", "机器功率（w）：", "电费（元/度）：",
    "调整模型时间 (xhym）：", "切片时间 (xhym)：", "后期处理时间（xhym）：",
    "耗材价格（元/卷）：", "耗材重量（g/卷）:", "模型耗材重量（g）：", 
    "每g耗材利润（元）：", "打印时间 (xhym)：", "操作员时薪（元）：", "特殊值（元）："
]

# 计算最长标签长度
max_label_length = max(len(label) for label in labels)

# 创建输入框和标签的函数
def create_row(parent, label_text, default_value, row):
    frame = tk.Frame(parent)
    frame.grid(row=row, column=0, padx=10, pady=5, sticky='w')

    label = tk.Label(frame, text=label_text, width=max_label_length + 9, anchor='e', font=("宋体", 10, "bold"))  # 加粗标签文字
    label.pack(side='left', padx=10)

    # 这里调整输入框的宽度, 例如设置为 10
    entry = tk.Entry(frame, fg='red', width=10)  # 调整宽度为 10
    entry.insert(0, default_value)
    entry.pack(side='left', padx=5)
    entry.bind("<KeyRelease>", lambda event, e=entry, dv=default_value: on_entry_change(e, dv))
    return entry

# 创建左右两列
left_frame = tk.Frame(window)
left_frame.grid(row=0, column=0, padx=0, pady=5, sticky="nsew")  # 缩小了 pady 的值
right_frame = tk.Frame(window)
right_frame.grid(row=0, column=1, padx=0, pady=5, sticky="nsew")

# 读取config中的数据
machine_cost_json_value = read_config_json(file_path, "machine_cost_json")  #机器购买价格（元）
machine_lifespan_json_value = read_config_json(file_path, "machine_lifespan_json")  #机器寿命（小时）
machine_power_json_value = read_config_json(file_path, "machine_power_json")  #机器功率（瓦特）
electricity_cost_json_value = read_config_json(file_path, "electricity_cost_json")  #电费（元/度）
adjust_time_json_value = read_config_json(file_path, "adjust_time_json")  #调整模型时间（小时）
slicing_time_json_value = read_config_json(file_path, "slicing_time_json")  #切片时间（小时）
post_process_time_json_value = read_config_json(file_path, "post_process_time_json")  #后期处理时间（小时）
material_price_json_value = read_config_json(file_path, "material_price_json")  #耗材价格（元/千克）
material_weight_json_value = read_config_json(file_path, "material_weight_json")  #耗材重量（千克）
model_material_weight_json_value = read_config_json(file_path, "model_material_weight_json")  #模型耗材重量（克）
profit_per_gram_json_value = read_config_json(file_path, "profit_per_gram_json")  #每克耗材利润（元）
print_time_json_value = read_config_json(file_path, "print_time_json")  #打印时间（小时）
operator_wage_json_value = read_config_json(file_path, "operator_wage_json")  #操作人员时薪（元）
special_value_json_value = read_config_json(file_path, "special_value_json")  #特殊值（元）


# 创建输入框
entry_machine_cost = create_row(left_frame, "机器购买价格（元）：", machine_cost_json_value, 0)
entry_machine_lifespan = create_row(left_frame, "机器寿命（h）：", machine_lifespan_json_value, 1)
entry_machine_power = create_row(left_frame, "机器功率（w）：", machine_power_json_value, 2)
entry_electricity_cost = create_row(left_frame, "电费（元/度）：", electricity_cost_json_value, 3)
entry_adjust_time = create_row(left_frame, "调整模型时间 (xhym)：", adjust_time_json_value, 4)
entry_slicing_time = create_row(left_frame, "切片时间 (xhym)：", slicing_time_json_value, 5)
entry_post_process_time = create_row(left_frame, "后期处理时间 (xhym)：", post_process_time_json_value, 6)

entry_material_price = create_row(right_frame, "耗材价格（元/卷）：", material_price_json_value, 0)
entry_material_weight = create_row(right_frame, "耗材重量（kg/卷）：", material_weight_json_value, 1)
entry_model_material_weight = create_row(right_frame, "模型耗材重量（g）：", model_material_weight_json_value, 2)
entry_profit_per_gram = create_row(right_frame, "每g耗材利润（元）：", profit_per_gram_json_value, 3)
entry_print_time = create_row(right_frame, "打印时间 (xhym)：", print_time_json_value, 4)
entry_operator_wage = create_row(right_frame, "操作员时薪（元）：", operator_wage_json_value, 5)
entry_special_value = create_row(right_frame, "特殊值（元）：", special_value_json_value, 6)

# 计算按钮
calculate_button = tk.Button(window, text="计算", command=calculate_price, width=15, height=1, font=("宋体", 10, "bold"))
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

# 输出框
output_box = tk.Text(window, height=7, bg="black", fg="green", state=tk.DISABLED, width=90)  # 设置输出框宽度和高度
output_box.grid(row=2, column=0, columnspan=2, pady=10)


# 说明框 - 设置背景为白色，字体为宋体加粗，调整行间距
explanation_box = tk.Text(window, height=12, width=90, wrap=tk.WORD, bg="white", fg="red", state=tk.DISABLED, font=("宋体", 10, "bold"))
explanation_box.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# 从config.json中读取说明
program_explanation_json_value = read_config_json(file_path, "program_explanation_json")  #程序说明

# 设置行间距
explanation_box.tag_configure("spacing", spacing1=5, spacing2=5)  # 设置段落前后间距
explanation_box.config(state=tk.NORMAL)
explanation_box.insert(tk.END, program_explanation_json_value)  # 默认显示内容

# 应用tag来调整段落间距
explanation_box.tag_add("spacing", "1.0", "end")

# 重新设置为 DISABLED，确保文本不可编辑
explanation_box.config(state=tk.DISABLED)

window.mainloop()