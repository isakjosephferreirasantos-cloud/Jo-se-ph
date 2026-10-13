import math
import random
import tkinter as tk


class BuracoNegroApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Buraco Negro")
        self.geometry("960x720")
        self.configure(bg="#040712")
        self.resizable(False, False)

        self.canvas = tk.Canvas(
            self,
            width=960,
            height=720,
            bg="#040712",
            highlightthickness=0,
        )
        self.canvas.pack(fill="both", expand=True)

        self.cx = 480
        self.cy = 360
        self.star_field = []
        self.disk_particles = []
        self.create_star_field()
        self.create_disk_particles()
        self.draw_background()

        self.bind("<Configure>", self.on_resize)
        self.after(30, self.animate)

    def on_resize(self, event):
        self.cx = self.winfo_width() / 2
        self.cy = self.winfo_height() / 2

    def create_star_field(self):
        for _ in range(350):
            distance = random.uniform(120, 420)
            angle = random.uniform(0, math.tau)
            speed = random.uniform(0.008, 0.03)
            size = random.uniform(1, 3)
            drift = random.uniform(-0.05, 0.05)
            hue = random.choice(["#f4d35e", "#ffb703", "#f9f7f3", "#c0fdfb", "#9ad1d4"])
            self.star_field.append({
                "angle": angle,
                "distance": distance,
                "speed": speed,
                "size": size,
                "drift": drift,
                "color": hue,
                "active": True,
            })

    def create_disk_particles(self):
        colors = ["#fff1a8", "#ffd166", "#ff9f1c", "#ff6b35"]
        for _ in range(180):
            self.disk_particles.append({
                "angle": random.uniform(0, math.tau),
                "distance": random.uniform(118, 250),
                "speed": random.uniform(0.012, 0.035),
                "size": random.uniform(1.5, 3.5),
                "color": random.choice(colors),
            })

    def draw_background(self):
        self.canvas.delete("bg")
        for _ in range(200):
            x = random.randint(0, 960)
            y = random.randint(0, 720)
            radius = random.randint(1, 2)
            self.canvas.create_oval(
                x - radius,
                y - radius,
                x + radius,
                y + radius,
                fill="#e5ecff",
                outline="",
                tags="bg",
            )

    def draw_accretion_disk(self):
        self.canvas.create_oval(
            self.cx - 260,
            self.cy - 110,
            self.cx + 260,
            self.cy + 110,
            outline="#ffb703",
            width=18,
            stipple="gray50",
            tags="disk",
        )
        self.canvas.create_oval(
            self.cx - 220,
            self.cy - 90,
            self.cx + 220,
            self.cy + 90,
            outline="#ff7b00",
            width=12,
            stipple="gray25",
            tags="disk",
        )
        self.canvas.create_oval(
            self.cx - 180,
            self.cy - 70,
            self.cx + 180,
            self.cy + 70,
            outline="#ff4d00",
            width=10,
            stipple="gray12",
            tags="disk",
        )

    def draw_disk_particles(self):
        for particle in self.disk_particles:
            particle["angle"] += particle["speed"]
            x = self.cx + math.cos(particle["angle"]) * particle["distance"]
            y = self.cy + math.sin(particle["angle"]) * particle["distance"] * 0.42
            glow = particle["size"] * 2.2

            self.canvas.create_oval(
                x - glow,
                y - glow * 0.42,
                x + glow,
                y + glow * 0.42,
                fill=particle["color"],
                outline="",
                stipple="gray50",
                tags="disk",
            )
            self.canvas.create_oval(
                x - particle["size"],
                y - particle["size"] * 0.42,
                x + particle["size"],
                y + particle["size"] * 0.42,
                fill="#fff8d6",
                outline="",
                tags="disk",
            )

    def animate(self):
        self.canvas.delete("stars")
        self.canvas.delete("disk")
        self.canvas.delete("blackhole")
        self.draw_accretion_disk()
        self.draw_disk_particles()

        for star in self.star_field:
            star["angle"] += star["speed"]
            star["distance"] -= 0.8 + star["speed"] * 18
            star["angle"] += star["drift"]

            if star["distance"] < 24:
                star["distance"] = random.uniform(250, 420)
                star["angle"] = random.uniform(0, math.tau)

            x = self.cx + math.cos(star["angle"]) * star["distance"]
            y = self.cy + math.sin(star["angle"]) * star["distance"] * 0.52

            glow = star["size"] * 2.8
            self.canvas.create_oval(
                x - glow,
                y - glow,
                x + glow,
                y + glow,
                fill=star["color"],
                outline="",
                tags="stars",
            )

            line_end_x = self.cx + math.cos(star["angle"]) * (star["distance"] * 0.4)
            line_end_y = self.cy + math.sin(star["angle"]) * (star["distance"] * 0.4) * 0.52
            self.canvas.create_line(
                x,
                y,
                line_end_x,
                line_end_y,
                fill=star["color"],
                width=max(1, star["size"]),
                tags="stars",
            )

        self.canvas.create_oval(
            self.cx - 86,
            self.cy - 86,
            self.cx + 86,
            self.cy + 86,
            fill="#000000",
            outline="#040712",
            width=2,
            tags="blackhole",
        )
        self.canvas.create_oval(
            self.cx - 112,
            self.cy - 112,
            self.cx + 112,
            self.cy + 112,
            outline="#000000",
            width=45,
            stipple="gray25",
            tags="blackhole",
        )

        self.after(20, self.animate)


if __name__ == "__main__":
    app = BuracoNegroApp()
    app.mainloop()
