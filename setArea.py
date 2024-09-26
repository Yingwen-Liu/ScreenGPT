import tkinter as tk
import json


class ScreenCapture:
    def __init__(self):
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.3)    # semi-transparent
        self.root.config(cursor="cross")

        self.canvas = tk.Canvas(self.root, bg='grey', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_click(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='orange', width=3)

    def on_drag(self, event):
        cur_x, cur_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_release(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        self.root.quit()

    def get_rectangle(self):
        self.root.mainloop()
        self.root.destroy()

        # Ensure coordinates are positive and sorted (top-left, bottom-right)
        x1 = int(min(self.start_x, self.end_x))
        y1 = int(min(self.start_y, self.end_y))
        x2 = int(max(self.start_x, self.end_x))
        y2 = int(max(self.start_y, self.end_y))

        return (x1, y1, x2, y2)

def set_area():
    # Start rectangle selection UI
    selector = ScreenCapture()
    x1, y1, x2, y2 = selector.get_rectangle()
    
    with open('config.json', 'r') as file:
        config = json.load(file)    
    
    # Convert to dictionary for mss
    config['area'] = {
        'top': y1,
        'left': x1,
        'width': x2 - x1,
        'height': y2 - y1
    }
    
    with open('config.json', 'w') as file:
        json.dump(config, file, indent=4)
    
    print(f">> Area {config['area']} saved")


if __name__ == "__main__":
    set_area()
