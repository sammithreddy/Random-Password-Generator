import random
import string
import tkinter as tk
frame=tk.Tk()
frame.geometry("300x400")
frame.title("Password Generator")
l=tk.Label(text="Enter the len of the password (Min =8 , Max=25)")
textbox1=tk.Text(frame,height=1,width=15,bg="light yellow")
pa=tk.Text(frame,height=3,width=20,bg="light cyan")
b=tk.Button(frame,height=2,text="Submit",command=lambda: generate_password(int(textbox1.get("1.0","end"))))
l.pack()
textbox1.pack()
pa.pack()
b.pack()
def generate_password(length):
    pa.delete("1.0","end")
    if length < 6:
        raise ValueError("Password length should be at least 6 to include a mix of character types.")
    l = string.ascii_lowercase
    u = string.ascii_uppercase
    d = string.digits
    s = string.punctuation
    ans = [
        random.choice(l),
        random.choice(u),
        random.choice(d),
        random.choice(s)
    ]
    all_characters = l+u+d+s
    ans += random.choices(all_characters, k=length-4)
    random.shuffle(ans)
    pa.insert(tk.END,''.join(ans))
frame.mainloop()