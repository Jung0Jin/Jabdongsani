from tkinter import *
from random import randint
from datetime import datetime
import tkinter.messagebox

print('hello world!')
class SR_test_APP():
    def __init__(self, the_win):
        self.i = 0; self.miss = 0; self.count = 0
        self.win = the_win
        self.var_change = StringVar()
        self.var_entry = StringVar()
        self.var_corr = StringVar()
        self.var_miss = StringVar()
        self.frame_set = Frame(self.win, relief=SOLID, bd=2)
        self.frame_test = Frame(self.win, relief=SOLID, bd=2)
        self.label_num_test = Label(self.frame_set, text="Test 횟수 : ", font="맑은고딕 12")
        self.entry_num_test = Entry(self.frame_set, width=3)
        self.label_num_select = Label(self.frame_set, text="선택변수 개수 : ", font="맑은고딕 12")
        self.entry_num_select = Entry(self.frame_set, width=3)
        self.button_set = Button(self.frame_set, text="Set", command=self.set_condition)
        self.label_num_select.grid(row=0, column=0)
        self.entry_num_select.grid(row=0, column=1)
        self.label_num_test.grid(row=0, column=2)
        self.entry_num_test.grid(row=0, column=3)
        self.button_set.grid(row=0, column=4)
        self.frame_set.grid(row=0)
        self.label_disp = Label(self.frame_test, text="Variable : ", font="Times 20")
        self.label_change = Label(self.frame_test, textvariable=self.var_change, font="Times 30 bold")
        self.entry_input = Entry(self.frame_test, textvariable=self.var_entry, font="맑은고딕 12", state='disabled')
        self.entry_input.bind('<Key>',self.change_num)
        self.label_disp.grid(row=0, column=0)
        self.label_change.grid(row=0, column=1)
        self.entry_input.grid(row=1, columnspan=2)
        self.frame_test.grid(row=1)
        self.frame_corr_miss = Frame(self.win, relief=SOLID, bd=2)
        self.label_correct = Label(self.frame_corr_miss, textvariable=self.var_corr, font="맑은고딕 12 bold")
        self.label_miss = Label(self.frame_corr_miss, textvariable=self.var_miss, font="맑은고딕 12 bold")
    def set_condition(self):
        self.i = 0; self.miss = 0
        self.test_num = int(self.entry_num_test.get())
        self.select_num = int(self.entry_num_select.get())
        self.randombox = [str(randint(0,self.select_num-1)) for _ in range(500)]
        self.label_correct.pack(side=LEFT)
        self.label_miss.pack()
        self.frame_corr_miss.grid(row=2)
        self.var_corr.set(f"Answer : {self.i}")
        self.var_miss.set(f"Miss : {self.miss}")
        self.var_entry.set("")
        self.entry_input['state']='normal'
        tkinter.messagebox.showinfo("Setting","Test 횟수는 %d 회, 선택변수는 %d 개로 설정되었습니다."%(self.test_num, self.select_num))
        self.var_change.set(self.randombox[0])
        if self.count != 0:
            self.label_result.grid_forget();
        self.entry_input.focus();
    def change_num(self, event):
        if self.i == 0:
            self.start = datetime.now()
            if event.char == self.randombox[self.i]:
                self.i += 1
                self.var_change.set(self.randombox[self.i])
                self.var_corr.set(f"Answer : {self.i}")
                self.var_miss.set(f"Miss : {self.miss}")
            else:
                self.miss += 1
                self.var_corr.set(f"Answer : {self.i}")
                self.var_miss.set(f"Miss : {self.miss}")
        else:
            if event.char == self.randombox[self.i]:
                self.i += 1
                self.var_change.set(self.randombox[self.i])
                self.var_corr.set(f"Answer : {self.i}")
                self.var_miss.set(f"Miss : {self.miss}")
            else:
                self.miss += 1
                self.var_corr.set(f"Answer : {self.i}")
                self.var_miss.set(f"Miss : {self.miss}")
            if self.i == self.test_num:
                self.finish = datetime.now()
                self.avg_time = str((self.finish-self.start)/self.test_num)
                self.var_entry.set('ALL DONE')
                self.var_change.set('X')
                self.entry_input['state']='disabled'
                self.result = tkinter.messagebox.askyesno("All Tests Done", "All tests were done. Check your result?")
                if self.result == 1:
                    tkinter.messagebox.showinfo("Your Result", f"Test 횟수 : {self.test_num}회, 선택변수 : {self.select_num}개 일때, 당신의 평균반응시간은 {self.avg_time[6:11]} sec입니다.")
                    self.label_result = Label(self.win, text=self.avg_time[6:11]+" sec", relief = SOLID, bd=1, fg="red", font="맑은고딕 15 bold")
                    self.label_result.grid(row=3)
                else:
                    self.button_result = Button(self.frame_test, text="Show result", font="함초롱바탕 12", height=3, command=self.show_result)
                    self.button_result.grid(row=0, rowspan=2,column=2)
                    self.count += 1;
    def show_result(self):
        self.result = tkinter.messagebox.askyesno("Check your result", "Check your result?")
        if self.result == 1:
            tkinter.messagebox.showinfo("Your Result", f"Test 횟수 : {self.test_num}회, 선택변수 : {self.select_num}개 일때, 당신의 평균반응시간은 {self.avg_time[6:11]} sec 입니다.")
            self.label_result = Label(self.win, text=self.avg_time[6:11]+" sec", relief = SOLID, bd=1, fg="red", font="맑은고딕 15 bold")
            self.label_result.grid(row=3)
            self.button_result.grid_forget()

win = Tk()
win.title("SR_TEST")
win.geometry("+500+200")
SR_test_1 = SR_test_APP(win)
win.mainloop()
