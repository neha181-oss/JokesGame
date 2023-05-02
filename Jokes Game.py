#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import pyjokes
root=tk.Tk()
root.title("Jokes game")
root.geometry("300x300")
root.configure(bg="Black")

def joke():
    global joke 
    joke=pyjokes.get_joke()
    T.insert(tk.END,joke)
def clear():
    T.delete("1.0","end")
    


T=tk.Text(root)
T.place(x=5,y=5,height=100,width=290)
b1=tk.Button(root,text="joke",bg="red",fg="black",command=joke)
b1.place(x=20,y=120,height=50,width=80)
b2=tk.Button(root,text="Clear",bg="red",fg="white",command=clear)
b2.place(x=100,y=120,height=50,width=60)


root.mainloop()


# In[21]:


import pyjokes
a=pyjokes.get_joke()


# In[24]:


print(a)


# In[ ]:




