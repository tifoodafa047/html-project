import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy import VideoFileClip

def cut_video(input_path, output_path, start_time, end_time):
    try:
        with VideoFileClip(input_path) as video:
            cut_clip = video.subclipped(start_time, end_time)
            cut_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Failed to cut video: {e}")
        return False

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select video file",
        filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
    )
    return file_path

def parse_time(timestr):
    """Parse mm:ss string to seconds."""
    try:
        parts = timestr.strip().split(":")
        if len(parts) == 2:
            minutes = int(parts[0])
            seconds = int(parts[1])
            return minutes * 60 + seconds
        elif len(parts) == 1:
            return int(parts[0])
        else:
            raise ValueError
    except Exception:
        raise ValueError("Time format must be mm:ss or m")

def start_cut():
    input_path = entry_file.get()
    output_path = entry_output.get()
    try:
        start_time = parse_time(entry_start.get())
        end_time = parse_time(entry_end.get())
    except ValueError:
        messagebox.showerror("Error", "Start and End times must be in mm:ss format.")
        return

    if not input_path or not output_path:
        messagebox.showerror("Error", "Please select a video file and specify output path.")
        return

    if start_time >= end_time:
        messagebox.showerror("Error", "End time must be greater than start time.")
        return

    success = cut_video(input_path, output_path, start_time, end_time)
    if success:
        messagebox.showinfo("Success", "Video cut successfully!")

def select_file():
    file_path = browse_file()
    if file_path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, file_path)

def main():
    global entry_file, entry_output, entry_start, entry_end

    root = tk.Tk()
    root.title("Video Cutter")

    tk.Label(root, text="Video File:").grid(row=0, column=0, sticky="e")
    entry_file = tk.Entry(root, width=40)
    entry_file.grid(row=0, column=1)
    tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2)

    tk.Label(root, text="Output File:").grid(row=1, column=0, sticky="e")
    entry_output = tk.Entry(root, width=40)
    entry_output.grid(row=1, column=1)
    entry_output.insert(0, "output.mp4")

    tk.Label(root, text="Start Time (mm:ss):").grid(row=2, column=0, sticky="e")
    entry_start = tk.Entry(root, width=10)
    entry_start.grid(row=2, column=1, sticky="w")
    entry_start.insert(0, "00:00")

    tk.Label(root, text="End Time (mm:ss):").grid(row=3, column=0, sticky="e")
    entry_end = tk.Entry(root, width=10)
    entry_end.grid(row=3, column=1, sticky="w")
    entry_end.insert(0, "00:10")

    tk.Button(root, text="Cut Video", command=start_cut).grid(row=4, column=1, pady=10)
    tk.Button(root, text="Quit", command=root.quit).grid(row=4, column=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()