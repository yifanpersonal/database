import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗
from datetime import datetime
from PIL import ImageTk, Image


import tkinter as tk
from tkinter import Label, Button, font as tkFont

userid = 0

class StartPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁子界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('群聊系统')
        self.window.configure(borderwidth=2, relief='sunken', background='lightblue')  # 添加彩色边框

        # 获取屏幕宽度和高度
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # 设置窗口的宽度和高度
        window_width = 500
        window_height = 470

        # 计算居中的位置
        position_right = int((screen_width / 2) - (window_width / 2))
        position_down = int((screen_height / 2) - (window_height / 2))

        # 设置窗口的位置和大小
        self.window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

        # 加载背景图片
        background_image = Image.open("C:/Users/ROG/Desktop/主界面.jpg")  # 替换为你的背景图片路径
        # background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)
        # background_image = background_image.resize((800, 600))
        photo = ImageTk.PhotoImage(background_image)


        # 创建一个Label来放置背景图片
        background_label = tk.Label(self.window, image=photo)
        background_label.pack()  # 使用 fill='both' 和 expand=True 使背景图片填充整个窗口

        # 设置窗口的位置和大小
        # self.window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

        Button(self.window, text="管理员登录", font=tkFont.Font(size=16), command=lambda: AdminPage(self.window),
               width=25,
               height=1,
               fg='white', bg='gray', activebackground='black', activeforeground='white').place(x=115, y=235)
        Button(self.window, text="用户登录", font=tkFont.Font(size=16), command=lambda: Page(self.window),
               width=25,
               height=1, fg='white', bg='gray', activebackground='black', activeforeground='white').place(x=115, y=275)
        Button(self.window, text="注册", font=tkFont.Font(size=16), command=lambda: signup(self.window),
               width=25,
               height=1,
               fg='white', bg='gray', activebackground='black', activeforeground='white').place(x=115, y=315)
        Button(self.window, text='退出', height=1, font=tkFont.Font(size=16), width=25, command=self.window.destroy,
               fg='white', bg='gray', activebackground='black', activeforeground='white').place(x=115, y=355)

        self.window.mainloop()  # 主消息循环

# 假设 AdminPage, StudentPage, AboutPage 也是类似的类，用于创建新的窗口

#管理员登录页面
class AdminPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员登录')
        self.window.configure(borderwidth=2, relief='sunken', background='lightblue')  # 添加彩色边框
        # self.window.configure(highlightbackground='red', highlightcolor='black', highlightthickness=2)  # 设置边框颜色

        # 获取屏幕宽度和高度
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # 设置窗口的宽度和高度
        window_width = 500
        window_height = 470

        # 计算居中的位置
        position_right = int((screen_width / 2) - (window_width / 2))
        position_down = int((screen_height / 2) - (window_height / 2))

        # 设置窗口的位置和大小
        self.window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
        self.font_art = tk.font.Font(family="华文行楷", size=14)
        self.font_art1 = tk.font.Font(family="华文行楷", size=28)

        label = tk.Label(self.window, text='管理员登录', bg='white', font=self.font_art1, width=30, height=2)
        label.pack()

        Label(self.window, text='账号', font=self.font_art).pack(pady=25)
        self.admin_username = tk.Entry(self.window, width=16, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_username.pack()

        Label(self.window, text='密码', font=self.font_art).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=16, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Button(self.window, text="登录", width=8, font=self.font_art, command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=self.font_art, command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.admin_username.get()))
        print(str(self.admin_pass.get()))
        admin_pass = None

        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM 管理员 WHERE 账号 = '%s'" % (self.admin_username.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                admin_id = row[2]
                admin_pass = row[4]
                # 打印结果
                print("admin_id=%s,admin_pass=%s" % (admin_id, admin_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '无法连接到数据库')
        db.close()  # 关闭数据库连接

        print("正在登录管理员管理界面")
        print("self", self.admin_pass)
        print("local", admin_pass)

        if self.admin_pass.get() == admin_pass:
            Adminselect(self.window)  # 进入管理员操作界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

#管理员选项界面
class Adminselect:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('选项')
        self.window.configure(borderwidth=2, relief='sunken', background='lightblue')  # 添加彩色边框
        # 获取屏幕宽度和高度
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # 设置窗口的宽度和高度
        window_width = 500
        window_height = 470

        # 计算居中的位置
        position_right = int((screen_width / 2) - (window_width / 2))
        position_down = int((screen_height / 2) - (window_height / 2))

        # 设置窗口的位置和大小
        self.window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
        self.font_art = tk.font.Font(family="华文行楷", size=16)

        label = tk.Label(self.window, text='操作选项', bg='white', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Button(self.window, text="成员信息", font=self.font_art, command=lambda: AdminManage(self.window),
               width=25,
               height=2,
               fg='black', bg='white', activebackground='black', activeforeground='white').place(x=120,y=175)
        Button(self.window, text="群聊天记录", font=self.font_art, command=lambda: ChatPage(self.window),
               width=25,
               height=2, fg='black', bg='white', activebackground='black', activeforeground='white').place(x=120,y=250)
        Button(self.window, text='返回', height=2, font=self.font_art, width=25, command=self.back,
               fg='black', bg='white', activebackground='black', activeforeground='white').place(x=120,y=325)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        AdminPage(self.window)  # 显示主窗口 销毁本窗口

# 管理员——成员信息（实现触发器，实现事务删除）
class AdminManage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = Tk()  # 初始框的声明
        self.window.title('管理员操作界面')
        self.window.configure(borderwidth=2, relief='sunken', background='lightblue')  # 添加彩色边框

        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)


        # 定义下方中心列表区域
        self.columns = ("账号", "昵称", "入群时间", "性别", "管理员")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=20, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("账号", width=100, anchor='center')  # 表示列,不显示
        self.tree.column("昵称", width=100, anchor='center')
        self.tree.column("入群时间", width=100, anchor='center')
        self.tree.column("性别", width=100, anchor='center')
        self.tree.column("管理员", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.time = []
        self.gender = []
        self.admin = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM 群成员"  # SQL 查询语句

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.time.append(row[4])
                self.gender.append(row[3])
                self.admin.append(row[5])
        except pymysql.MySQLError as e:
            messagebox.showinfo('警告！', f'数据库连接失败：{e}')
            db.close()
            return
        db.close()  # 关闭数据库连接

        # 写入数据
        for i in range(min(len(self.id), len(self.name), len(self.time), len(self.gender), len(self.admin))):
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.time[i], self.gender[i], self.admin[i]))

        # 绑定函数，使表头可排序
        for col in self.columns:
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="群成员信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明账号
        self.var_name = StringVar()  # 声明昵称
        self.var_time = StringVar()  # 声明入群时间
        self.var_gender = StringVar()  # 声明性别

        # 账号
        self.right_top_id_label = Label(self.frame_left_top, text="账号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 姓名
        self.right_top_name_label = Label(self.frame_left_top, text="昵称：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 入群时间
        self.right_top_gender_label = Label(self.frame_left_top, text="入群时间：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_time,
                                            font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 性别
        self.right_top_gender_label = Label(self.frame_left_top, text="性别：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender,
                                            font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='添加群成员', width=20, command=self.new_row)
        # self.right_top_button2 = ttk.Button(self.frame_right_top, text='管理消息', width=20,
        #                                     command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='移除群成员', width=20,
                                            command=self.del_row)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        # self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(False)
        self.frame_right_top.grid_propagate(False)
        self.frame_center.grid_propagate(False)
        self.frame_bottom.grid_propagate(False)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击

    def back(self):
        Adminselect(self.window)  # 显示主窗口 销毁本窗口

    #点击群成员信息时显示
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_time.set(self.row_info[2])
        self.var_gender.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))

        print('')

    #点击排序
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题


    #触发器控制下的添加操作
    def new_row(self):
        # print('123')
        # print(self.var_id.get())
        # print(self.id)

        # 获取当前时间
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(current_date)

        if self.var_id.get() == '':
            messagebox.showinfo('警告！', '请填写学生数据')
            return

        if int(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该用户已存在！')
            return

        db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql0 = "SELECT 账号, 昵称, 密码, 性别 FROM 全部账户 WHERE 账号 = %s"
        cursor.execute(sql0, (self.var_id.get(),))
        results = cursor.fetchall()

        if len(results) == 0:
            messagebox.showinfo('警告！', '没有找到匹配的用户！')
            db.close()
            return


        sql = "INSERT INTO 群成员(账号, 昵称, 密码, 性别,入群时间,管理员) \
               VALUES ('%s', '%s', '%s', '%s','%s', '%s')" % \
              (self.var_id.get(), results[0][1], results[0][2], results[0][3], current_date, '0')  # SQL 插入语句

        try:
            cursor.execute(sql)  # 执行sql语句
            db.commit()  # 提交到数据库执行
        except pymysql.MySQLError as e:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', f'触发器：{e}')
            db.close()
            return

        db.close()  # 关闭数据库连接

        self.id.append(int(self.var_id.get()))
        self.name.append(results[0][1])
        self.time.append(current_date)
        self.gender.append(results[0][3])
        self.admin.append('0')
        self.tree.insert('', len(self.id) - 1, values=(
            self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.time[len(self.id) - 1],
            self.gender[len(self.id) - 1], self.admin[len(self.id) - 1]))
        self.tree.update()
        messagebox.showinfo('提示！', f'{self.var_id.get()}入群成功！')

    #含有事务应用的删除操作
    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True and self.row_info[4] == '0':
            # 检查 self.row_info[0] 是否确实存在于 self.id 列表中
            print(self.id)
            print(self.row_info[0])
            intid = int(self.row_info[0])#id列表中是int型
            if intid in self.id:
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "set foreign_key_checks = 0"

                sql_delete = "DELETE 群成员,聊天记录 FROM 群成员,聊天记录 WHERE 群成员.账号=聊天记录.账号 AND 群成员.账号 = %s"

                sql_delete0 = "delete from 群成员 where 群成员.账号 = %s"
                sql1 = "set foreign_key_checks = 1"
                # 执行SQL语句
                try:
                    cursor.execute(sql)
                    cursor.execute(sql_delete, (intid,))
                    cursor.execute(sql_delete0, (intid,))
                    cursor.execute(sql1)
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '删除成功！')
                except pymysql.MySQLError as e:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', f'删除失败：{e}')
                 # 关闭数据库连接

                # 删除本地列表中的记录
                id_index = self.id.index(intid)
                del self.id[id_index]
                del self.name[id_index]
                del self.time[id_index]
                del self.gender[id_index]
                del self.admin[id_index]

                # 从树形视图中删除对应的行
                self.tree.delete(self.tree.selection()[0])
            else:
                messagebox.showinfo('警告！', '要删除的记录不存在！')

#管理员管理聊天记录
class ChatPage:

    def __init__(self, parent_window):

        parent_window.destroy()  # 销毁主界面

        # 创建主窗口
        self.root = tk.Tk()
        self.root.title('聊天记录')
        self.root.configure(borderwidth=2, relief='sunken', background='lightblue')  # 添加彩色边框

        # 获取屏幕宽度和高度
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # 设置窗口的宽度和高度
        window_width = 800
        window_height = 600

        # 计算居中的位置
        position_right = int((screen_width / 2) - (window_width / 2))
        position_down = int((screen_height / 2) - (window_height / 2))

        # 设置窗口的位置和大小
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

        # 加载背景图片
        # background_image = Image.open("C:/Users/ROG/Desktop/主界面.jpg")  # 替换为你的背景图片路径
        # #background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)
        # background_image = ImageTk.PhotoImage(background_image)
        #
        # # 创建一个Label来放置背景图片
        # background_label = tk.Label(root, image=background_image)
        # background_label.pack(fill='both', expand=True)

        # 聊天记录视图
        self.chat_record_view = tk.Text(self.root, state='disabled', wrap='word')
        self.chat_record_view.place(x=10, y=10)

        self.chat_record_view.config(font=('黑体', 12))

        # 连接数据库
        db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')
        cursor = db.cursor()

        # 获取聊天记录
        cursor.execute("SELECT 记录编号, 账号, 发送时间, 昵称, 内容 FROM 聊天记录")
        chat_records = cursor.fetchall()

        # 更新聊天记录视图
        for record in chat_records:
            # 组合每个属性的值
            record_str = f"编号: {record[0]}     {record[3]}     {record[1]}     {record[2]}\n\n {record[4]}\n\n"
            self.chat_record_view.config(state='normal')
            self.chat_record_view.insert(tk.END, record_str)
            self.chat_record_view.config(state='disabled')

        #删除操作按钮
        delete_button = tk.Button(self.root, text="删除记录", command=self.dele)
        delete_button.place(x=10, y=500)

        back_button = tk.Button(self.root, text="返回", command=self.back)
        back_button.place(x=150, y=500)

        self.input_entry = tk.Entry(self.root, width=30)
        self.input_entry.place(x=10, y=450)

        self.input_value = tk.StringVar()
        # 将输入框的文本绑定到变量
        self.input_entry.config(textvariable=self.input_value)

    # 在需要删除聊天记录的地方调用这个函数
    # delete_all_chat_records(self, '要删除的账号')

    def dele(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True :
            # 获取用户输入的记录编号
            id = self.input_value.get()
            print(id)
            self.chat_record_view.delete("1.0", "end")

            # 检查记录编号是否存在于聊天记录表中
            db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')
            cursor = db.cursor()
            sql = "select * from 聊天记录 where 记录编号 = %s"
            cursor.execute(sql, (id,))
            results = cursor.fetchall()

            if results is not None:
                # 删除记录
                db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql_delete = "DELETE FROM 聊天记录 WHERE 记录编号 = %s"
                try:
                    cursor.execute(sql_delete, (id,))
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '删除成功！')
                except pymysql.MySQLError as e:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', f'删除失败：{e}')
                    return
                finally:
                    db.close()  # 关闭数据库连接

                # 更新聊天记录视图
                db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')
                cursor = db.cursor()
                cursor.execute("SELECT 记录编号, 账号, 发送时间, 昵称, 内容 FROM 聊天记录")
                chat_records = cursor.fetchall()
                self.chat_record_view.config(state='normal')
                self.chat_record_view.delete('1.0', 'end')  # 清空视图中的文本

                for record in chat_records:
                    record_str = f"编号: {record[0]}     {record[3]}     {record[1]}     {record[2]}\n\n {record[4]}\n\n"
                    self.chat_record_view.config(state='normal')
                    self.chat_record_view.insert(tk.END, record_str)
                    self.chat_record_view.config(state='disabled')
            else:
                messagebox.showinfo('警告！', '没有找到匹配的记录！')
            db.close()  # 关闭数据库连接

    def back(self):
        Adminselect(self.root)  # 显示主窗口 销毁本窗口

#用户登录页面
class Page:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('用户登录')
        self.window.configure(borderwidth=2, relief='sunken', background='lightblue')  # 添加彩色边框

        # 获取屏幕宽度和高度
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # 设置窗口的宽度和高度
        window_width = 500
        window_height = 470

        # 计算居中的位置
        position_right = int((screen_width / 2) - (window_width / 2))
        position_down = int((screen_height / 2) - (window_height / 2))

        # 设置窗口的位置和大小
        self.window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
        self.font_art1 = tk.font.Font(family="华文行楷", size=28)

        label = tk.Label(self.window, text='用户登录', bg='white', font=self.font_art1, width=30, height=2)
        label.pack()
        self.font_art = tk.font.Font(family="华文行楷", size=14)

        Label(self.window, text='账号：', font=self.font_art).pack(pady=25)
        self.username = tk.Entry(self.window, width=16, font=self.font_art, bg='Ivory')
        self.username.pack()

        Label(self.window, text='密码：', font=self.font_art).pack(pady=25)
        self.password = tk.Entry(self.window, width=16, font=self.font_art, bg='Ivory', show='*')
        self.password.pack()

        Button(self.window, text="登录", width=8, font=self.font_art, command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=self.font_art, command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.username.get()))
        print(str(self.password.get()))
        intid=int(self.username.get())
        pw = None

        # 数据库操作 查询全部成员表
        db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT 账号,密码 FROM 全部账户 WHERE 账号 = '%s'" % \
              intid  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            if results is None:
                messagebox.showinfo('警告！', '用户名或密码不正确！')
                return
            else:
                if self.password.get() == results[0][1]:
                    global userid
                    userid = intid
                    userselect(self.window)  # 进用户操作界面
                else:
                    messagebox.showinfo('警告！', '用户名或密码不正确！')
                    return

        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登录用户界面")
        # print("self", intid)
        # print("local", pw)

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

#注册界面
class signup:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('新用户注册')
        self.window.configure(borderwidth=2, relief='sunken', background='lightblue')  # 添加彩色边框
        # 获取屏幕宽度和高度
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # 设置窗口的宽度和高度
        window_width = 500
        window_height = 470

        # 计算居中的位置
        position_right = int((screen_width / 2) - (window_width / 2))
        position_down = int((screen_height / 2) - (window_height / 2))

        # 设置窗口的位置和大小
        self.window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
        self.font_art0 = tk.font.Font(family="华文行楷", size=28)

        label = tk.Label(self.window, text='新用户注册', bg='white', font=self.font_art0, width=30, height=2)
        label.pack()
        self.font_art = tk.font.Font(family="华文行楷", size=14)

        Label(self.window, text='账号：', font=self.font_art).pack(pady=10)
        self.username = tk.Entry(self.window, width=16, font=self.font_art, bg='Ivory')
        self.username.pack()

        Label(self.window, text='昵称：', font=self.font_art).pack(pady=10)
        self.name = tk.Entry(self.window, width=16, font=self.font_art, bg='Ivory')
        self.name.pack()

        Label(self.window, text='密码：', font=self.font_art).pack(pady=10)
        self.password = tk.Entry(self.window, width=16, font=self.font_art, bg='Ivory', show='*')
        self.password.pack()

        Label(self.window, text='性别：', font=self.font_art).pack(pady=10)
        self.gender = tk.Entry(self.window, width=16, font=self.font_art, bg='Ivory')
        self.gender.pack()

        Button(self.window, text="注册", width=8, font=self.font_art, command=self.find).pack(pady=20)
        Button(self.window, text="返回首页", width=8, font=self.font_art, command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环


    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

    def find(self):
        print(str(self.username.get()))
        # print(str(self.password.get()))
        username = int(self.username.get())

        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT 账号 FROM 全部账户 WHERE 账号 = %s"  # 使用参数化查询以避免SQL注入
        try:
            # 执行SQL语句
            cursor.execute(sql, username)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            if (username,) in results :
                print("Error: name already exists！")
                messagebox.showinfo('警告！', '用户名已存在！')

            else:
                self.change()

        except pymysql.MySQLError as e:
            print(f"MySQL错误：{e}")
            messagebox.showinfo('警告！', '数据库连接失败！')
        except Exception as e:
            print(f"其他错误：{e}")
            messagebox.showinfo('警告！', '错误！')
        finally:
            db.close()  # 关闭数据库连接

    def change(self):
        print(str(self.username.get()))
        print(str(self.name.get()))
        print(str(self.password.get()))
        print(str(self.gender.get()))
        username = int(self.username.get())

        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "INSERT INTO 全部账户(账号, 昵称 ,密码,性别) VALUES ('%s', '%s','%s', '%s')" % \
              (username, self.name.get(), self.password.get(),self.gender.get())  # SQL 查询语句
        try:
            cursor.execute(sql)  # 执行sql语句
            db.commit()  # 提交到数据库执行
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '数据库连接失败！')
            return

        db.close()  # 关闭数据库连接

        messagebox.showinfo('提示', '创建成功')

#用户选项
class userselect:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('选项')
        self.window.configure(borderwidth=2, relief='sunken', background='lightblue')  # 添加彩色边框
        # 获取屏幕宽度和高度
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # 设置窗口的宽度和高度
        window_width = 500
        window_height = 470

        # 计算居中的位置
        position_right = int((screen_width / 2) - (window_width / 2))
        position_down = int((screen_height / 2) - (window_height / 2))

        # 设置窗口的位置和大小
        self.window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
        self.font_art0 = tk.font.Font(family="华文行楷", size=28)

        label = tk.Label(self.window, text='选项', bg='white', font=self.font_art0, width=30, height=2)
        label.pack()
        self.font_art = tk.font.Font(family="华文行楷", size=16)

        Button(self.window, text="修改账号", font=self.font_art, command=lambda: update_id(self.window),
               width=25,
               height=2,
               fg='black', bg='white', activebackground='black', activeforeground='white').place(x=120,y=175)
        Button(self.window, text="聊天", font=self.font_art, command=lambda: Chat(self.window),
               width=25,
               height=2, fg='black', bg='white', activebackground='black', activeforeground='white').place(x=120,y=250)
        Button(self.window, text='返回', height=2, font=self.font_art, width=25, command=self.back,
               fg='black', bg='white', activebackground='black', activeforeground='white').place(x=120,y=325)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        Page(self.window)  # 显示主窗口 销毁本窗口

#修改账号(实现存储过程)
class update_id:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('修改账号')
        self.window.configure(borderwidth=2, relief='sunken', background='lightblue')  # 添加彩色边框
        # 获取屏幕宽度和高度
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # 设置窗口的宽度和高度
        window_width = 500
        window_height = 470

        # 计算居中的位置
        position_right = int((screen_width / 2) - (window_width / 2))
        position_down = int((screen_height / 2) - (window_height / 2))

        # 设置窗口的位置和大小
        self.window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
        self.font_art0 = tk.font.Font(family="华文行楷", size=28)

        label = tk.Label(self.window, text='用户登录', bg='white', font=self.font_art0, width=30, height=2)
        label.pack()
        self.font_art = tk.font.Font(family="华文行楷", size=16)

        Label(self.window, text='新账号：', font=self.font_art).pack(pady=25)
        self.username = tk.Entry(self.window, width=16, font=tkFont.Font(size=14), bg='Ivory')
        self.username.pack()

        Button(self.window, text="确认修改", width=8, font=self.font_art, command=self.update).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=self.font_art, command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def update(self):
        print(str(self.username.get()))
        intid=int(self.username.get())
        if self.username.get() == "":
            messagebox.showinfo('警告！', '请输入新账号')
            return
        else:
            # 数据库操作 查询全部成员表
            db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')  # 打开数据库连接
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "CALL UpdateAccount(%s, %s)"
            try:
                cursor.execute(sql, (userid, intid))
                messagebox.showinfo('成功！', '账号更新成功')
                db.commit()

            except:
                print("Error: unable to fecth data")
                messagebox.showinfo('警告！', '账号已存在')
            db.close()  # 关闭数据库连接

            print("正在登录用户界面")
            # print("self", intid)
            # print("local", pw)

    def back(self):
        userselect(self.window)  # 显示主窗口 销毁本窗口

#用户聊天(实现视图)
class Chat:

    def __init__(self, parent_window):

        parent_window.destroy()  # 销毁主界面
        self.name = ""

        db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')
        cursor = db.cursor()
        sql0 = "select * from 群成员 where 账号 = %s " % userid
        # 执行SQL语句
        cursor.execute(sql0)
        # 获取所有记录列表
        results = cursor.fetchall()
        print(results)
        db.close()
        if len(results) == 0 :
            messagebox.showinfo('警告！', '你不在群聊中')
        else:
            # 创建主窗口
            self.root = tk.Tk()
            self.root.title('聊天记录')
            self.root.configure(borderwidth=2, relief='sunken', background='lightblue')  # 添加彩色边框
            self.name = results[0][1]

            # 获取屏幕宽度和高度
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            # 设置窗口的宽度和高度
            window_width = 800
            window_height = 600

            # 计算居中的位置
            position_right = int((screen_width / 2) - (window_width / 2))
            position_down = int((screen_height / 2) - (window_height / 2))

            # 设置窗口的位置和大小
            self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

            # 加载背景图片
            # background_image = Image.open("C:/Users/ROG/Desktop/主界面.jpg")  # 替换为你的背景图片路径
            # #background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)
            # background_image = ImageTk.PhotoImage(background_image)
            #
            # # 创建一个Label来放置背景图片
            # background_label = tk.Label(root, image=background_image)
            # background_label.pack(fill='both', expand=True)

            # 聊天记录视图
            self.chat_text = tk.Text(self.root, state='disabled', wrap='word')
            self.chat_text.place(x=10, y=10)

            self.chat_text.config(font=('宋体', 12))

            # ... 其他代码 ...

            # 连接数据库
            db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')
            cursor = db.cursor()
            sql_drop = "DROP VIEW IF EXISTS chat_record"
            sql = "CREATE VIEW chat_record AS SELECT 聊天记录.账号 as 账号,聊天记录.发送时间 as 发送时间,聊天记录.昵称 as 昵称,聊天记录.内容 as 内容,群成员.管理员 as 管理员 FROM 聊天记录 INNER JOIN 群成员 ON 聊天记录.账号 = 群成员.账号;"
            sql_view = "SELECT 昵称,发送时间,管理员,内容 FROM chat_record"

            try:
                # 执行SQL语句
                cursor.execute(sql_drop)
                cursor.execute(sql)
                cursor.execute(sql_view)  # 使用参数化查询
                # 获取所有记录列表
                results = cursor.fetchall()
                if not results:
                    record_str = "无聊天记录"
                    self.chat_text.config(state='normal')
                    self.chat_text.insert(tk.END, record_str)
                else:
                    self.chat_text.config(state='normal')
                    for record in results:
                        if record[2] == 0:
                            admin=''
                        else:
                            admin='管理员'
                        record_str = f"{record[0]}     {record[1]}     {admin}\n\n{record[3]}\n\n"  # 注意索引可能与你的数据库字段对应不上
                        self.chat_text.insert(tk.END, record_str)
                    self.chat_text.config(state='disabled')

            except pymysql.MySQLError as e:
                print(f"Error: unable to fetch data - {e}")
                messagebox.showinfo('警告！', f'无法连接到数据库 - {e}')
            finally:
                db.close()  # 确保总是关闭数据库连接

            # ... 其他代码 ...

            #发送信息按钮
            send_button = tk.Button(self.root, text="发送", command=self.send)
            send_button.place(x=10, y=500)

            back_button = tk.Button(self.root, text="返回", command=self.back)
            back_button.place(x=150, y=500)

            self.input_entry = tk.Entry(self.root, width=30)
            self.input_entry.place(x=10, y=450)

            self.input_message = tk.StringVar()
            # 将输入框的文本绑定到变量
            self.input_entry.config(textvariable=self.input_message)

        # 在需要删除聊天记录的地方调用这个函数
        # delete_all_chat_records(self, '要删除的账号')

    #改成发送
    def send(self):
        res = messagebox.askyesnocancel('警告！', '是否发送？')
        if res == True :
            # 获取用户输入的文本
            message = self.input_message.get()
            # 获取当前时间
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(message)
            self.chat_text.delete("1.0", "end")
            code = ""
            number = 0

            # 检查记录编号到哪了
            db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')
            cursor = db.cursor()
            sql = "select 记录编号 from 聊天记录"
            cursor.execute(sql)
            results = cursor.fetchall()
            db.close()
            c=0
            if results is None:
                code = "REC001"
            else:
                for row in results:
                    if c<int(row[0][4:]):
                        c=int(row[0][4:])
                print(c)
                code = "REC0" + str(c+1)
                print(code)

            db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')
            cursor = db.cursor()
            sql = "INSERT INTO 聊天记录(记录编号,账号,发送时间,昵称,内容) \
                           VALUES ('%s', '%s', '%s', '%s','%s')" % \
                  (code, userid, current_date, self.name, message)  # SQL 插入语句

            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
            except pymysql.MySQLError as e:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '发送失败')
                db.close()
                return

            db.close()  # 关闭数据库连接

            # 连接数据库
            db = pymysql.connect(host='localhost', port=3306, db='群聊系统', user='root', password='zhyf040216')
            cursor = db.cursor()
            sql_view = "SELECT 昵称,发送时间,管理员,内容 FROM chat_record"
            self.chat_text.config(state='normal')
            self.chat_text.delete('1.0', 'end')  # 清空视图中的文本
            # 执行SQL语句
            cursor.execute(sql_view)  # 使用参数化查询
            # 获取所有记录列表
            results = cursor.fetchall()
            for record in results:
                if record[2] == 0:
                    admin = ''
                else:
                    admin = '管理员'
                record_str = f"{record[0]}     {record[1]}     {admin}\n\n{record[3]}\n\n"  # 注意索引可能与你的数据库字段对应不上
                self.chat_text.insert(tk.END, record_str)
            self.chat_text.config(state='disabled')
            db.close()  # 确保总是关闭数据库连接

    def back(self):
        userselect(self.root)  # 显示主窗口 销毁本窗口

if __name__ == '__main__':

    window = tk.Tk()
    StartPage(window)
