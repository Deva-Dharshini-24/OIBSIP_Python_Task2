import customtkinter as ctk

from speak import speak
from listen import listen
from commands import execute_command
from weather import get_weather

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# -------------------------
# ASSISTANT FUNCTION
# -------------------------

def start_assistant():

    status_label.configure(
        text="🔴 Listening..."
    )

    app.update()

    command = listen()

    if command:

        history_box.insert(
            "end",
            f"\n🧑 You: {command}\n"
        )

        history_box.see("end")

        execute_command(command, speak)

    status_label.configure(
        text="🟢 Online"
    )


#buttons workings

def show_assistant():

    history_box.delete("1.0", "end")

    history_box.insert(
        "end",
        "🤖 Jarvis AI Ready...\n"
    )


def show_notes():

    history_box.delete("1.0", "end")

    try:

        with open("notes.txt", "r") as file:

            notes = file.read()

            history_box.insert(
                "end",
                "📝 SAVED NOTES\n\n"
            )

            history_box.insert(
                "end",
                notes
            )

    except:

        history_box.insert(
            "end",
            "No notes found."
        )


def show_history():

    history_box.delete("1.0", "end")

    try:

        with open("history.txt", "r") as file:

            history = file.read()

            history_box.insert(
                "end",
                "📜 COMMAND HISTORY\n\n"
            )

            history_box.insert(
                "end",
                history
            )

    except:

        history_box.insert(
            "end",
            "No history found."
        )




def show_weather():

    history_box.delete("1.0", "end")

    weather = get_weather("Chennai")

    history_box.insert(
        "end",
        "🌤 CURRENT WEATHER\n\n"
    )

    history_box.insert(
        "end",
        weather
    )


# -------------------------
# MAIN WINDOW
# -------------------------

app = ctk.CTk()

app.geometry("1200x700")

app.title("JARVIS AI")


# -------------------------
# SIDEBAR
# -------------------------

sidebar = ctk.CTkFrame(
    app,
    width=220,
    corner_radius=0
)

sidebar.pack(
    side="left",
    fill="y"
)

logo = ctk.CTkLabel(
    sidebar,
    text="🤖 JARVIS",
    font=("Segoe UI", 24, "bold")
)

logo.pack(
    pady=(30, 20)
)

menu1 = ctk.CTkButton(
    sidebar,
    text="🎤 Assistant",
    command=show_assistant
)

menu1.pack(
    pady=10,
    padx=20,
    fill="x"
)

menu2 = ctk.CTkButton(
    sidebar,
    text="🌤 Weather",
    command=show_weather
)

menu2.pack(
    pady=10,
    padx=20,
    fill="x"
)

menu3 = ctk.CTkButton(
    sidebar,
    text="📝 Notes",
    command=show_notes
)

menu3.pack(
    pady=10,
    padx=20,
    fill="x"
)

menu4 = ctk.CTkButton(
    sidebar,
    text="📜 History",
    command=show_history
)

menu4.pack(
    pady=10,
    padx=20,
    fill="x"
)


# -------------------------
# MAIN AREA
# -------------------------

main_frame = ctk.CTkFrame(
    app,
    corner_radius=15
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)


title = ctk.CTkLabel(
    main_frame,
    text="JARVIS AI",
    font=("Segoe UI", 38, "bold")
)

title.pack(
    pady=(20, 10)
)


status_label = ctk.CTkLabel(
    main_frame,
    text="🟢 Online",
    font=("Segoe UI", 18)
)

status_label.pack(
    pady=(0, 20)
)


listen_button = ctk.CTkButton(
    main_frame,
    text="🎙 TAP TO SPEAK",
    command=start_assistant,
    width=320,
    height=70,
    font=("Segoe UI", 18, "bold"),
    corner_radius=20
)

listen_button.pack(
    pady=20
)


# -------------------------
# HISTORY BOX
# -------------------------

history_box = ctk.CTkTextbox(
    main_frame,
    width=800,
    height=350
)

history_box.pack(
    pady=20,
    padx=20
)

history_box.insert(
    "end",
    "🤖 Jarvis AI Ready...\n"
)


# -------------------------
# BOTTOM INFO
# -------------------------

bottom_frame = ctk.CTkFrame(
    main_frame
)

bottom_frame.pack(
    fill="x",
    padx=20,
    pady=3
)

commands_card = ctk.CTkLabel(
    bottom_frame,
    text="⚡ Commands Active",
    font=("Segoe UI", 14)
)

commands_card.pack(
    side="left",
    padx=20
)

notes_card = ctk.CTkLabel(
    bottom_frame,
    text="📝 Notes Enabled",
    font=("Segoe UI", 14)
)

notes_card.pack(
    side="left",
    padx=20
)

weather_card = ctk.CTkLabel(
    bottom_frame,
    text="🌤 Weather Ready",
    font=("Segoe UI", 14)
)

weather_card.pack(
    side="left",
    padx=20
)


app.mainloop()