# 3DPrint_Cost_Calculator
## 为什么会有这个程序
因为刚开始接触3D打印，不知道如何计算费用。一番查找后只找到一个网站可以在线计算：https://3dwithus.com/3d-print-cost-calculator

本程序即为参考该网站使用python3编写的，补充了电费及特殊值（补偿值）。
## 简介
本程序仅用于计算3D打印时所产生的费用。包括：机器折旧费用、电费、人工成本、耗材成本。

其中：机器购买价格以拓竹P1SC为准即5500元，寿命为3D打印机的平均寿命1500小时，功率按照800瓦计算，电费默认按照0.5元每度计算，人工处理时间默认为0（可根据需要调整），每克耗材利润也为0（可根据需要调整），特殊值为修正值（会直接加在最终费用里）

（功率我没有找到机器的平均功率数据，800是根据官方文档的最大功率和打印ABS材料时的功率估的一个大概值）
## 更改配置
程序运行后会读取当前目录下的config.json文件，如果没有，程序会自动创建并写入示例数据。所有数值均可在config.json内进行配置。
经常改动的数值（如：打印当前模型所需要的耗材）可以留空。
![image](https://github.com/user-attachments/assets/44b14b79-7f78-4676-9d2e-24e1e36f1e87)

基本不变的数值（如：我只有一台P1S，打印机费用是固定的）可以直接写死，避免每次重复输入。
![image](https://github.com/user-attachments/assets/157336bf-0d34-4dcc-97b2-9174203ed6c0)
## 运行
如果想要修改代码，或者通过代码的方式运行，你需要python3的环境，我使用的是Python 3.10.6。
由于只使用了tkinter、os、json库。所以没有tkinter的直接```pip install tkinter```即可，如果网络原因无法安装，则用国内的源```pip install tkinter -i https://pypi.douban.com/simple```

**如果你使用的设备操作系统是windows，也可以直接下载release内的文件双击运行。**

初始界面：

![image](https://github.com/user-attachments/assets/df976a9f-f77d-41f3-b20a-c2025b8c1305)

输入数据进行计算：

![image](https://github.com/user-attachments/assets/eac9be1f-f05c-4f84-896b-adada0ad56b9)

**注意：输入的所有时间，格式均为类似1h37m(1小时37分钟)**
