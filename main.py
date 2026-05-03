import tkinter as tk

BG_COLOR = "#0d1117"
SECONDARY_BG = "#161b22"
ACCENT_COLOR = "#2ea043"
TEXT_COLOR = "#e6edf3"
SUBTEXT_COLOR = "#8b949e"
BORDER_COLOR = "#30363d"

FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_NORMAL = ("Segoe UI", 12)
FONT_SMALL = ("Segoe UI", 10)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700


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

    return root


def main():
    root = build_window()
    root.mainloop()


if __name__ == "__main__":
    main()