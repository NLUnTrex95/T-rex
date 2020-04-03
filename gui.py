from tkinter import *
test_dict = {}
totals_dict = []
entries = []
stats_tracking_list =[
    "Cost:",
    "Salvage Value:",
    "Useful Life (Years):",
    "Month:",
    "Day:",
    "Method:",
]
type_of_accounting_selected =["Straight Line", "DDB", "SOYD", "ABC","MACRS",]
bg_color = "SlateBlue"; bg_color2 = "SlateBlue1"; bg_color3 = "RoyalBlue1"


def gui_run():    
    root = Tk()  # main box 
    root.title("Depreciation of Fixed Assets")
    root.geometry('523x310')
    root.grid_rowconfigure(index=0, weight=1, )
    root.grid_columnconfigure(index=0, weight=1,)

    # First frame
    base_frame = Frame(root, bg=bg_color,)
    base_frame.grid_rowconfigure(index=1, weight=1, )
    base_frame.grid_columnconfigure(index=1, weight=1, )
    base_frame.grid(sticky="n,s,e,w", )
    # Second frame.
    top_frame = Frame(base_frame, bg=bg_color, relief="raised", borderwidth=10, width=800)
    top_frame.grid(row=1, column=1, sticky="")
    # Frame for check box.
    check_box_frame = Frame(top_frame, bg=bg_color ,relief="raised", borderwidth=3, )
    check_box_frame.grid(row=(len(stats_tracking_list) + 1), column=0, padx=1, columnspan=4,)
    #Spacer row,0 column,1
    spacer_frame = Frame(top_frame, bg=bg_color, relief="raised", borderwidth=10, width=10)
    spacer_frame.grid(row=0, column=1, rowspan=6,)
    # Widgets
    
    
    k = ""
    def labels_made(i):
        k = stats_tracking_list
        k = Label(top_frame, text=stats_tracking_list[i], pady=1, bg=bg_color3, font="Helvetica 18 ",relief="raised", borderwidth=3)
        k.grid(row=i + 1, column=0, sticky="e")
        return(i)
        
    def entries_made(i):
        k = Entry(top_frame, width=10, relief="raised", borderwidth=2, font="Helvetica 18 ")
        k.grid(row=i + 1, column=2, sticky="w", )
        entries.append(k)
        return(i)

    def mode_made(i):
        k = stats_tracking_list
        k = Label(top_frame, text=stats_tracking_list[i], pady=1, bg=bg_color3, font="Helvetica 18 ",relief="raised", borderwidth=3)
        k.grid(row=i + 1, column=0, sticky="e")
        k = Spinbox(top_frame, value=(type_of_accounting_selected), width=10, font="ariel, 16",relief="raised", borderwidth=3, )
        k.grid(row=i + 1, column=2, sticky="w")
        entries.append(k)
    
    def spin_box_made(i):
        if i == 4:
            k = "sp_box" + str(i)
            k = Spinbox(top_frame, from_=1, to=31, width=3, font="ariel, 16",relief="raised", borderwidth=3, )
            k.grid(row=i + 1, column=2, sticky="w")
            entries.append(k)
        else:
            k = "sp_box" + str(i)
            k = Spinbox(top_frame, from_=1, to=12, width=3, font="ariel, 16",relief="raised", borderwidth=3, )
            k.grid(row=i + 1, column=2, sticky="w")
            entries.append(k)
            
            return(i)

    for i, value in enumerate(stats_tracking_list):
        i = labels_made(i)        
        if i <= 2: #this is for 3 lines of Entries.
            i = entries_made(i)
        elif i == 5:
            i = mode_made(i)
        elif i == 3 or 4:
            i = spin_box_made(i)    

    def fra_clear():
        top_frame.destroy()
        screen_two()

    def entries_get():
        for i, entry in enumerate(entries): 
            test_dict[stats_tracking_list[i]] = entry.get()
        print(test_dict)
        screen_two()
        

    k = Button(top_frame,text="NEXT !", bg=bg_color2, command=fra_clear, font=14, width=6, )
    k.grid(row=(len(stats_tracking_list) + len(type_of_accounting_selected) + 2), column=2, sticky="w", padx=0, columnspan=2,)

    k = Button(top_frame,text="Calculate!", bg=bg_color2, command=entries_get, font=14, width=8,)
    k.grid(row=(len(stats_tracking_list) + len(type_of_accounting_selected) + 2), column=2, sticky="e", padx=0,)


    def screen_two():
        screen_two = Frame(base_frame, bg="gray", relief="raised", borderwidth=10, width=800,)
        screen_two.grid(row=1, column=1, sticky="")
        # Frame for check box.
        check_box_frame2 = Frame(screen_two, bg="blue" ,relief="raised", borderwidth=3, )
        check_box_frame2.grid(row=(len(stats_tracking_list) + 1), column=0, padx=1, columnspan=4,)
        #Spacer row,0 column,1
        spacer_frame2 = Frame(screen_two, bg="green", relief="raised", borderwidth=10, width=10)
        spacer_frame2.grid(row=0, column=1, rowspan=6,)
        
        
        


    root.mainloop()
    return test_dict
