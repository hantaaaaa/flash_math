import random
import time
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font
import os

# クラスと対応する設定を辞書で定義
# (num_questions, display_time, digit_length, erase_time)
class_settings = {
    "20段": (15, 0.1, 3, 0),
    "19段": (15, 0.106666667, 3, 0),
    "18段": (15, 0.113333333, 3, 0),
    "17段": (15, 0.12, 3, 0),
    "16段": (15, 0.126666667, 3, 0),
    "15段": (15, 0.133333333, 3, 0),
    "14段": (15, 0.146666667, 3, 0),
    "13段": (15, 0.16, 3, 0),
    "12段": (15, 0.173333333, 3, 0),
    "11段": (15, 0.186666667, 3, 0),
    "10段": (15, 0.2, 3, 0),
    "9段": (15, 0.3, 3, 0),
    "8段": (15, 0.4, 3, 0),
    "7段": (15, 0.533333333, 3, 0),
    "6段": (12, 0.666666667, 3, 0),
    "5段": (10, 0.7, 3, 0),
    "4段": (8, 0.75, 3, 0),
    "3段": (6, 0.833333333, 3, 0),
    "2段": (4, 1, 3, 0),
    "初段": (15, 0.666666667, 2, 0),
    "1級": (15, 0.866666667, 2, 0),
    "2級": (12, 1, 2, 0),
    "3級": (10, 1.2, 2, 0),
    "4級": (8, 1.375, 2, 0),
    "5級": (7, 1.428571429, 2, 0),
    "6級": (6, 1.5, 2, 0),
    "7級": (5, 1.6, 2, 0),
    "8級": (4, 1.75, 2, 0),
    "9級": (3, 2, 2, 0),
    "10級": (2, 2, 2, 0),
    "11級": (15, 1, 2, 0),
    "12級": (10, 1, 2, 0),
    "13級": (20, 0.75, 1, 0),
    "14級": (15, 1, 1, 0),
    "15級": (12, 1.25, 1, 0),
    "16級": (10, 1.2, 1, 0),
    "17級": (8, 1.25, 1, 0),
    "18級": (5, 1.5, 1, 0),
    "19級": (3, 1.5, 1, 0),
    "20級": (3, 1.5, 1, 0.2),
}

def flash_mental_math():
    print("フラッシュ暗算を始めます！")
    print("画面に表示される数字を覚えて、その合計を答えてください。")
    print("準備ができたらEnterキーを押してください。")
    input()

    # クラスを選択
    selected_class = None
    while selected_class not in class_settings:
        print("クラスを選択してください:")
        for class_name in class_settings.keys():
            print(f"- {class_name}")
        selected_class = input("クラスを入力してください(例:20級) ")
        if selected_class not in class_settings:
            print("無効なクラスが選択されました。もう一度入力してください。")

    # 選択したクラスに基づいて設定を取得
    num_questions, display_time, digit_length, erase_time = class_settings[selected_class]

    for i in range(1):
        # 指定された桁数のランダムな数字を生成（連続する同じ数値を防ぐ）
        numbers = []
        for _ in range(num_questions):
            while True:
                new_number = random.randint(10**(digit_length-1), 10**digit_length - 1)
                if not numbers or new_number != numbers[-1]:  # 直前の数値と異なる場合
                    numbers.append(new_number)
                    break

        correct_answer = sum(numbers)

        print(f"桁数は{digit_length}桁です")
        print(f"口数は{num_questions}口です")
        print(f"1問の表示時間は{display_time:.2f}秒です")
        print("準備ができたらEnterキーを押してください。")
        input()

        # 3秒間の準備時間
        print("準備中...\n")
        time.sleep(3)

        #時間測定開始
        start_time = time.time()

        # 数字を順番に表示
        for num in numbers:
            print(num, end="", flush=True)  # 数字を表示
            time.sleep(display_time)       # 指定時間待機
            print("\r" + " " * len(str(num)), end="\r")  # 数字を消す
            time.sleep(erase_time)         # 消去時間を待機
 
        #時間測定終了
        end_time = time.time()

        # ユーザーの回答を取得
        user_answer = input("合計は？: ")

        # 時間差を表示
        elapsed_time = end_time - start_time
        print(f"数字の表示にかかった時間: {elapsed_time:.1f} 秒")

        # 出題した数字を再表示
        print(f"出題した数字: {', '.join(map(str, numbers))}")

        # 答え合わせ
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("正解！")

        else:
            print(f"不正解。正しい答えは {correct_answer} です。")

    print(f"\n練習終了！")

class FlashMathGUI:
    def __init__(self, master):
        self.master = master
        master.title("フラッシュ暗算 GUI")
        master.configure(bg="black")
        self.selected_class = tk.StringVar(value="20級")
        self.numbers = []
        self.current_index = 0
        self.correct_answer = 0
        self.start_time = 0
        self.display_time = 1
        self.erase_time = 0
        self.digit_length = 2
        self.num_questions = 5

        # アバカスフォント２の読み込み
        try:
            self.abacus_font_large = font.Font(family="Abacus2", size=150)
        except Exception as e:
            messagebox.showerror("フォントエラー", f"ABACUS2.ttf の読み込みに失敗しました。\n{e}")
            self.abacus_font_large = ("Arial", 150)

        # メインフレーム（横並び）
        main_frame = tk.Frame(master, bg="black")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 左側：操作部
        control_frame = tk.Frame(main_frame, bg="black")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

        tk.Label(control_frame, text="クラスを選択してください:", fg="white", bg="black", font=("Hiragino Maru Gothic Pro W2", 14)).pack(anchor=tk.W, pady=(0,10))
        class_menu = ttk.Combobox(control_frame, textvariable=self.selected_class, values=list(class_settings.keys()), width=8, font=("Hiragino Maru Gothic Pro W2", 14))
        class_menu.pack(anchor=tk.W, pady=(0,20))

        self.start_btn = tk.Button(control_frame, text="スタート", command=self.start_game, font=("Hiragino Maru Gothic Pro W2", 16), bg="#ADFF2F", fg="black")
        self.start_btn.pack(anchor=tk.W, pady=(0,30))

        answer_frame = tk.Frame(control_frame, bg="black")
        answer_frame.pack(anchor=tk.W, pady=(0,10))
        self.answer_frame = answer_frame  # 追加: answer_frameをインスタンス変数に
        tk.Label(answer_frame, text="合計は？", fg="white", bg="black", font=("Hiragino Maru Gothic Pro W2", 14)).pack(side=tk.LEFT)
        self.answer_entry = tk.Entry(answer_frame, font=("Hiragino Maru Gothic Pro W2", 18), width=10)
        self.answer_entry.pack(side=tk.LEFT, padx=10)
        self.answer_entry.bind('<Return>', lambda event: self.check_answer())
        self.answer_btn = tk.Button(answer_frame, text="答える", command=self.check_answer, font=("Hiragino Maru Gothic Pro W2", 14), state=tk.DISABLED)
        self.answer_btn.pack(side=tk.LEFT)

        self.result_label = tk.Label(control_frame, text="", font=("Hiragino Maru Gothic Pro W2", 16), fg="white", bg="black")
        self.result_label.pack(anchor=tk.W, pady=(10,0))

        # 右側：数値表示部
        display_frame = tk.Frame(main_frame, bg="black")
        display_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.number_label = tk.Label(display_frame, text="", font=self.abacus_font_large, fg="#ADFF2F", bg="black")
        self.number_label.pack(expand=True)

        # --- 追加: 回答入力の有効/無効制御 ---
        self.answer_entry_enabled = False

    def set_answer_entry_state(self, enabled):
        self.answer_entry_enabled = enabled
        self.answer_entry.config(state=tk.NORMAL)  # Entryは常に有効
        if enabled:
            self.answer_btn.config(state=tk.NORMAL)
        else:
            self.answer_btn.config(state=tk.DISABLED)

    def start_game(self):
        # answer_frameの初期化（子ウィジェット全削除→再生成）
        for widget in self.answer_frame.winfo_children():
            widget.destroy()
        tk.Label(self.answer_frame, text="合計は？", fg="white", bg="black", font=("Hiragino Maru Gothic Pro W2", 14)).pack(side=tk.LEFT)
        self.answer_entry = tk.Entry(self.answer_frame, font=("Hiragino Maru Gothic Pro W2", 18), width=10)
        self.answer_entry.pack(side=tk.LEFT, padx=10)
        self.answer_entry.bind('<Return>', lambda event: self.check_answer())
        self.answer_btn = tk.Button(self.answer_frame, text="答える", command=self.check_answer, font=("Hiragino Maru Gothic Pro W2", 14), state=tk.DISABLED)
        self.answer_btn.pack(side=tk.LEFT)

        self.result_label.config(text="")
        self.answer_entry.delete(0, tk.END)
        self.set_answer_entry_state(False)
        self.number_label.config(text="")
        self.master.update()
        class_name = self.selected_class.get()
        self.num_questions, self.display_time, self.digit_length, self.erase_time = class_settings[class_name]
        self.numbers = []
        for _ in range(self.num_questions):
            while True:
                new_number = random.randint(10**(self.digit_length-1), 10**self.digit_length - 1)
                if not self.numbers or new_number != self.numbers[-1]:
                    self.numbers.append(new_number)
                    break
        self.correct_answer = sum(self.numbers)
        self.current_index = 0
        self.start_btn.config(state=tk.DISABLED)
        self.start_time = time.time()
        # 1秒待ってから最初の数字を表示
        self.master.after(1000, self.show_number)

    def show_number(self):
        self.set_answer_entry_state(False)
        if self.current_index < len(self.numbers):
            num = self.numbers[self.current_index]
            self.number_label.config(text=str(num))
            self.master.after(int(self.display_time * 1000), self.erase_number)
        else:
            self.number_label.config(text="?")
            self.set_answer_entry_state(True)
            self.answer_entry.focus()

    def erase_number(self):
        self.number_label.config(text="")
        self.current_index += 1
        self.master.after(int(self.erase_time * 1000), self.show_number)

    def check_answer(self):
        if not self.answer_entry_enabled:
            # 数値表示中にEnter/答えるが押された場合
            self.result_label.config(text="計算しなよ、baby", fg="yellow")
            return
        user_answer = self.answer_entry.get()
        if user_answer.strip() == "":
            self.result_label.config(text="計算しなよ、baby", fg="yellow")
            self.answer_entry.focus()
            return
        elapsed = time.time() - self.start_time
        if user_answer.isdigit() and int(user_answer) == self.correct_answer:
            self.result_label.config(text=f"正解！\n数字: {', '.join(map(str, self.numbers))}\n時間: {elapsed:.1f}秒", fg="#ADFF2F")
        else:
            self.result_label.config(text=f"不正解。正しい答えは {self.correct_answer} です。\n数字: {', '.join(map(str, self.numbers))}\n時間: {elapsed:.1f}秒", fg="red")
        self.start_btn.config(state=tk.NORMAL)
        self.set_answer_entry_state(False)  # 回答後は再入力不可にする

if __name__ == "__main__":
    import sys

    # exe 化されたとき → 常に GUI
    if getattr(sys, 'frozen', False):
        root = tk.Tk()
        app = FlashMathGUI(root)
        root.mainloop()

    # --console が付いた場合のみコンソール版
    elif len(sys.argv) > 1 and sys.argv[1] == "--console":
        flash_mental_math()

    # それ以外は GUI (デフォルト)
    else:
        root = tk.Tk()
        app = FlashMathGUI(root)
        root.mainloop()
