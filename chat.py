from ctransformers import AutoModelForCausalLM
llm = AutoModelForCausalLM.from_pretrained("chat.gguf")

import customtkinter

root = customtkinter.CTk()
root.title("chatGPT")
root.columnconfigure([0,1,2,3], minsize=200)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)

i = customtkinter.CTkEntry(root)
o = customtkinter.CTkTextbox(root)

def submit(i):
    root.title("Processing...")
    answer = llm(str(i.get()))
    print(str(i.get()), answer)
    o.insert("0.0", str(i.get())+answer+"\n\n")
    i.delete(0,len(str(i.get())))
    root.title("chatGPT")

btn = customtkinter.CTkButton(root, text = "Submit", command = lambda: submit(i))
o.grid(row=1, columnspan=4, sticky="nsew")
i.grid(row=2, columnspan=3, sticky="nsew")
btn.grid(row=2, column=3, sticky="nsew")

def theme():
    if light_var.get()=="on":customtkinter.set_appearance_mode("light")
    else:customtkinter.set_appearance_mode("dark")

light_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(root,text="Theme",command=theme,variable=light_var,onvalue="on",offvalue="off")
switch.grid(row=0, column=3)

root.mainloop()
