import tkinter as tk

BG_COLOR = "#0d1117"
SECONDARY_BG = "#161b22"
ACCENT_COLOR = "#2ea043"
TEXT_COLOR = "#e6edf3"
SUBTEXT_COLOR = "#8b949e"
BORDER_COLOR = "#30363d"
INPUT_BG = "#21262d"
USER_BUBBLE = "#2ea043"
BOT_BUBBLE = "#21262d"

FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_NORMAL = ("Segoe UI", 12)
FONT_SMALL = ("Segoe UI", 10)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700


def add_message(messages_frame, canvas, text, role="user"):
    is_user = role == "user"

    outer = tk.Frame(messages_frame, bg=BG_COLOR, pady=4)
    outer.pack(fill="x", padx=10)

    bubble_color = USER_BUBBLE if is_user else BOT_BUBBLE
    text_color = "#ffffff" if is_user else TEXT_COLOR
    anchor_side = "e" if is_user else "w"
    align = "right" if is_user else "left"

    name_label = tk.Label(
        outer,
        text="You" if is_user else "🤖 Assistant",
        font=("Segoe UI", 9, "bold"),
        bg=BG_COLOR,
        fg=SUBTEXT_COLOR,
    )
    name_label.pack(anchor=anchor_side, padx=12)

    bubble_frame = tk.Frame(outer, bg=bubble_color, padx=12, pady=8)
    bubble_frame.pack(anchor=anchor_side)

    msg_label = tk.Label(
        bubble_frame,
        text=text,
        font=FONT_NORMAL,
        bg=bubble_color,
        fg=text_color,
        wraplength=480,
        justify=align,
        anchor=anchor_side,
    )
    msg_label.pack()

    messages_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.yview_moveto(1.0)

    return msg_label


def build_window():
    root = tk.Tk()
    root.title("🤖 AI Chatbot")
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.configure(bg=BG_COLOR)
    root.resizable(False, False)

    header_frame = tk.Frame(root, bg=SECONDARY_BG, pady=12)
    header_frame.pack(fill="x")

    tk.Label(
        header_frame,
        text="🤖 AI Chatbot",
        font=FONT_TITLE,
        bg=SECONDARY_BG,
        fg=ACCENT_COLOR,
    ).pack(side="left", padx=20)

    tk.Label(
        header_frame,
        text="● Online",
        font=FONT_SMALL,
        bg=SECONDARY_BG,
        fg=ACCENT_COLOR,
    ).pack(side="right", padx=20)

    chat_outer = tk.Frame(root, bg=BORDER_COLOR)
    chat_outer.pack(fill="both", expand=True, padx=15, pady=(10, 5))

    chat_frame = tk.Frame(chat_outer, bg=BG_COLOR)
    chat_frame.pack(fill="both", expand=True, padx=1, pady=1)

    canvas = tk.Canvas(chat_frame, bg=BG_COLOR, highlightthickness=0)
    scrollbar = tk.Scrollbar(chat_frame, orient="vertical", command=canvas.yview)

    messages_frame = tk.Frame(canvas, bg=BG_COLOR)
    messages_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
    )

    canvas.create_window((0, 0), window=messages_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    canvas.bind_all(
        "<MouseWheel>",
        lambda e: canvas.yview_scroll(-1 * (e.delta // 120), "units"),
    )

    add_message(messages_frame, canvas, "Hello! How can I help you today?", role="bot")

    input_outer = tk.Frame(root, bg=BORDER_COLOR)
    input_outer.pack(fill="x", padx=15, pady=(0, 15))

    input_frame = tk.Frame(input_outer, bg=INPUT_BG, pady=10, padx=10)
    input_frame.pack(fill="x", padx=1, pady=1)

    input_entry = tk.Text(
        input_frame,
        font=FONT_NORMAL,
        bg=INPUT_BG,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        relief="flat",
        height=3,
        wrap="word",
    )
    input_entry.pack(side="left", fill="both", expand=True, padx=(5, 10))
    input_entry.insert("1.0", "Type a message...")
    input_entry.config(fg=SUBTEXT_COLOR)

    def on_focus_in(event):
        if input_entry.get("1.0", tk.END).strip() == "Type a message...":
            input_entry.delete("1.0", tk.END)
            input_entry.config(fg=TEXT_COLOR)

    def on_focus_out(event):
        if input_entry.get("1.0", tk.END).strip() == "":
            input_entry.insert("1.0", "Type a message...")
            input_entry.config(fg=SUBTEXT_COLOR)

    input_entry.bind("<FocusIn>", on_focus_in)
    input_entry.bind("<FocusOut>", on_focus_out)

    def on_send():
        message = input_entry.get("1.0", tk.END).strip()
        if not message or message == "Type a message...":
            return
        input_entry.delete("1.0", tk.END)
        add_message(messages_frame, canvas, message, role="user")

    def on_enter_press(event):
        if not event.state & 0x1:
            on_send()
            return "break"

    input_entry.bind("<Return>", on_enter_press)

    send_btn = tk.Button(
        input_frame,
        text="Send ➤",
        font=FONT_NORMAL,
        bg=ACCENT_COLOR,
        fg=TEXT_COLOR,
        relief="flat",
        padx=15,
        pady=8,
        cursor="hand2",
        activebackground="#3fb950",
        activeforeground=TEXT_COLOR,
        command=on_send,
    )
    send_btn.pack(side="right")

    tk.Label(
        root,
        text="Enter to send  •  Shift+Enter for new line",
        font=FONT_SMALL,
        bg=BG_COLOR,
        fg=SUBTEXT_COLOR,
    ).pack(pady=(0, 5))

    return root


def main():
    root = build_window()
    root.mainloop()


if __name__ == "__main__":
    main()