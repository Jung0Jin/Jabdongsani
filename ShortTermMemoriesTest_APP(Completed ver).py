from tkinter import *
import random
import tkinter.messagebox
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import tkinter.ttk

class STM_test_APP():
    def __init__(self, the_window, init_term, test_count):
        self.num_size_list=[7,6,9,10,4,5,8,11]
        self.test_count=test_count
        self.cycle=[7,6,9,10,4,5,8,11]
        for _ in range(50):
            self.num_size_list+=self.cycle
        self.var_num=StringVar()
        self.var_term=StringVar()
        self.var_test_num=StringVar()
        self.var_term.set(f'{init_term}')
        self.i=0
        self.frame_setting=Frame(the_window, relief=SOLID, bd=2)
        self.frame_test=Frame(the_window, relief=SOLID, bd=2)
        self.label_changing_num=Label(self.frame_test, textvariable=self.var_num,
                                                          font="Times 40 bold", relief=SOLID, bd=2, padx=3)
        self.label_term=Label(self.frame_setting, text='time term')
        self.entry_term=Entry(self.frame_setting, textvariable=self.var_term, width=3)
        self.button_start_test=Button(self.frame_setting, text='START' ,command=self.test)
        self.label_test_num=Label(self.frame_test, textvariable=self.var_test_num)
        self.label_term.grid(row=0,column=0)
        self.entry_term.grid(row=0,column=1)
        self.button_start_test.grid(row=0,column=2)
        self.frame_setting.grid(row=0)
        self.frame_test.grid(row=1)
        self.label_changing_num.grid(row=0, column=0)
        self.entry_memory=Entry(self.frame_test)
        ########## 여기가 엔트리값을 받는 곳 (함수 : self._input & self.__input)
        self.button_input=Button(self.frame_test, text='Enter', command=self._input)
        self.entry_memory.bind('<Return>',self.__input)
        ##########
        self.entry_memory.grid(row=0,column=1)
        self.button_input.grid(row=0,column=2)
        self.label_test_num.grid(row=1,columnspan=3)
        self.result_list=[]; self.input_list=[]; self.temp_list=[]
        self.button_output=Button(the_window, text='Show Result', command=self.show)
        self.button_output.grid(row=2)
        self.label_test_num_of_times=Label(self.frame_setting, text=f'Test number of times : {self.test_count}')
        self.label_test_num_of_times.grid(row=1,columnspan=3)
        #self.temp_button=Button(the_window, text='test', command=self.temp)
        #self.temp_button.grid(row=3)
    def test(self):
        self.button_start_test['state']='disabled'
        self.button_input['state']='disabled'
        self.entry_memory.config(state='disabled')
        self.result_list=[]
        self.i=0; self.n=0; self.test_num=1
        self.var_test_num.set('test_num : {}'.format(self.test_num))
        self.term=int(self.var_term.get())*1000
        self.change_num()
    # button 클릭시 적용되는 인풋 함수
    def _input(self):
        self.input_list.append(self.entry_memory.get())
        self.entry_memory.delete(0,END)
        self.button_start_test['state']='disabled'
        self.button_input['state']='disabled'
        self.entry_memory.config(state='disabled')
        self.test_num += 1
        self.var_test_num.set('test_num : {}'.format(self.test_num))
        self.change_num()
    # enter 입력시 적용되는 인풋 함수
    def __input(self, event):
        self.input_list.append(self.entry_memory.get())
        self.entry_memory.delete(0,END)
        self.button_start_test['state']='disabled'
        self.button_input['state']='disabled'
        self.entry_memory.config(state='disabled')
        print(self.entry_memory.get())
        self.test_num += 1
        self.var_test_num.set('test_num : {}'.format(self.test_num))
        self.change_num()
    def change_num(self):
        self.result=random.randint(0,9)
        if self.temp_list != []:
            while str(self.result) == self.temp_list[-1]:
                self.result=random.randint(0,9) # protect by sequentially duplicated number 
        self.temp_list.append(str(self.result))
        self.var_num.set(f'{self.result}')
        self.num_size = self.num_size_list[self.i]
        if self.i == self.test_count:
            tkinter.messagebox.showwarning("Test count over","You already done all tests")  
        elif self.n < self.num_size:
            self.n += 1
            win.after(self.term,self.change_num)
        elif self.n == self.num_size:
            self.entry_memory.config(state='normal')
            self.button_start_test['state']='normal'
            self.button_input['state']='normal'
            self.entry_memory.focus()
            self.n=0
            self.i += 1
            self.result_list.append("".join(self.temp_list))
            self.temp_list=[]
    def create_graph(self):
        self.series_data=pd.Series({5:self.five_property,6:self.six_property,7:self.seven_property,8:self.eight_property,
                                        9:self.nine_property,10:self.ten_property,11:self.eleven_property,12:self.twelve_property})
        self.plot_data=self.series_data.plot()
        self.plot_data.set_title("Right Properties for numbers of number")
        self.plot_data.set_xlabel("Numbers of number")
        self.plot_data.set_ylabel("Right Properties")
        plt.savefig('plot.png')
        plt.close()
    def create_image(self):
        self.img=PhotoImage(file='plot.png')
        self.label_graph=Label(self.frame_graph, image=self.img)
        self.label_graph.pack()
    def show(self):
        if self.i < self.test_count:
            tkinter.messagebox.showerror("Error","You have not done your test 40")
        else:
            print(self.result_list[0])
            print(self.input_list)
            for q in self.result_list:
                print(len(q))
            self.five_num=0; self.six_num=0; self.seven_num=0; self.eight_num=0; self.nine_num=0;
            self.ten_num=0; self.eleven_num=0; self.twelve_num=0
        
            
            for i in range(self.test_count):
                if len(self.result_list[i])==5:
                    if len(self.input_list[i]) >= 5:
                        self.right=0
                        for k in range(5):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.five_num+=self.right
                    else:
                        self.right=0
                        for k in range(len(self.input_list[i])):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.five_num+=self.right
                
                if len(self.result_list[i])==6:
                    if len(self.input_list[i]) >= 6:
                        self.right=0
                        for k in range(6):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.six_num+=self.right
                    else:
                        self.right=0
                        for k in range(len(self.input_list[i])):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.six_num+=self.right
                        
                if len(self.result_list[i])==7:
                    if len(self.input_list[i]) >= 7:
                        self.right=0
                        for k in range(7):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.seven_num+=self.right
                    else:
                        self.right=0
                        for k in range(len(self.input_list[i])):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.seven_num+=self.right
                    
                if len(self.result_list[i])==8:
                    if len(self.input_list[i]) >= 8:
                        self.right=0
                        for k in range(8):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.eight_num+=self.right
                    else:
                        self.right=0
                        for k in range(len(self.input_list[i])):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.eight_num+=self.right
                    
                if len(self.result_list[i])==9:
                    if len(self.input_list[i]) >= 9:
                        self.right=0
                        for k in range(9):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.nine_num+=self.right
                    else:
                        self.right=0
                        for k in range(len(self.input_list[i])):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.nine_num+=self.right
                    
                if len(self.result_list[i])==10:
                    if len(self.input_list[i]) >= 10:
                        self.right=0
                        for k in range(10):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.ten_num+=self.right
                    else:
                        self.right=0
                        for k in range(len(self.input_list[i])):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.ten_num+=self.right
                    
                if len(self.result_list[i])==11:
                    if len(self.input_list[i]) >= 11:
                        self.right=0
                        for k in range(11):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.eleven_num+=self.right
                    else:
                        self.right=0
                        for k in range(len(self.input_list[i])):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.eleven_num+=self.right
                    
                if len(self.result_list[i])==12:
                    if len(self.input_list[i]) >= 12:
                        self.right=0
                        for k in range(12):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.twelve_num+=self.right
                    else:
                        self.right=0
                        for k in range(len(self.input_list[i])):
                            if self.input_list[i][k]==self.result_list[i][k]:
                                self.right+=1
                        self.twelve_num+=self.right
                    
            self.five_property=self.five_num/(5*((self.test_count // 8) + 1)) if self.test_count % 8 != 0 else self.five_num/(5*(self.test_count // 8));
            self.six_property=self.six_num/(6*((self.test_count // 8) + 1)) if self.test_count % 8 != 0 else self.six_num/(6*(self.test_count // 8));
            self.seven_property=self.seven_num/(7*((self.test_count // 8) + 1)) if self.test_count % 8 != 0 else self.seven_num/(7*(self.test_count // 8));
            self.eight_property=self.eight_num/(8*((self.test_count // 8) + 1)) if self.test_count % 8 != 0 else self.eight_num/(8*(self.test_count // 8));
            self.nine_property=self.nine_num/(9*((self.test_count // 8) + 1)) if self.test_count % 8 != 0 else self.nine_num/(9*(self.test_count // 8));
            self.ten_property=self.ten_num/(10*((self.test_count // 8) + 1)) if self.test_count % 8 != 0 else self.ten_num/(10*(self.test_count // 8));
            self.eleven_property=self.eleven_num/(11*((self.test_count // 8) + 1)) if self.test_count % 8 != 0 else self.eleven_num/(11*(self.test_count // 8));
            self.twelve_property=self.twelve_num/(12*((self.test_count // 8) + 1)) if self.test_count % 8 != 0 else self.twelve_num/(12*(self.test_count // 8));
        # Sloving properties Calculating process
        
            self.ask=tkinter.messagebox.askokcancel("Show Result","You really look test result?")
            if self.ask==1:
                self.result=Toplevel()
                self.notebook=tkinter.ttk.Notebook(self.result, width=300, height=300)
                self.notebook.pack()
                self.frame_make=Frame(self.result, relief=SOLID, bd=2)
                self.notebook.add(self.frame_make, text='Graph Made first')
                self.frame_chart=Frame(self.result, relief=SOLID, bd=2)
                self.notebook.add(self.frame_chart, text='Show Chart')
                self.label_chart=Label(self.frame_chart, text=f'''
Right Property for numbers of number

Five : {self.five_property}
Six : {self.six_property}
Seven : {self.seven_property}
Eight : {self.eight_property}
Nine : {self.nine_property}
Ten : {self.ten_property}
Eleven : {self.eleven_property}
Twelve : {self.twelve_property}
''', font='맑은고딕 12', justify=LEFT)
                self.label_chart.pack()
                self.button_save=Button(self.frame_make, text='Save Graph First', command=self.create_graph)
                self.button_output=Button(self.frame_make, text='Show Graph', command=self.create_image)
                self.button_save.grid(row=0,column=0)
                self.button_output.grid(row=0,column=1)
                self.frame_graph=Frame(self.result, relief=SOLID, bd=2)
                self.notebook.add(self.frame_graph, text='Show Graph')
                self.result.mainloop()
    #def temp(self):
    #    print(self.result_list)
    #    tkinter.messagebox.showwarning("Test count over","You already done all tests")
        

        
win=Tk()
win.geometry("+500+300")
win.title("Short Term Memories TEST")
stm_test_1=STM_test_APP(win, init_term=1, test_count=3)
win.mainloop()