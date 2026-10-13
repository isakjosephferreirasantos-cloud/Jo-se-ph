import math
import tkinter as tk


DECLARACOES_DE_AMOR = (
    ("Português", "Eu te amo"),
    ("Inglês", "I love you"),
    ("Espanhol", "Te amo"),
    ("Francês", "Je t'aime"),
    ("Italiano", "Ti amo"),
    ("Alemão", "Ich liebe dich"),
    ("Holandês", "Ik hou van jou"),
    ("Africâner", "Ek is lief vir jou"),
    ("Sueco", "Jag älskar dig"),
    ("Norueguês", "Jeg elsker deg"),
    ("Dinamarquês", "Jeg elsker dig"),
    ("Islandês", "Ég elska þig"),
    ("Finlandês", "Rakastan sinua"),
    ("Estoniano", "Ma armastan sind"),
    ("Letão", "Es tevi mīlu"),
    ("Lituano", "Aš tave myliu"),
    ("Polonês", "Kocham cię"),
    ("Tcheco", "Miluji tě"),
    ("Eslovaco", "Ľúbim ťa"),
    ("Esloveno", "Ljubim te"),
    ("Croata", "Volim te"),
    ("Sérvio", "Волим те"),
    ("Bósnio", "Volim te"),
    ("Macedônio", "Те сакам"),
    ("Búlgaro", "Обичам те"),
    ("Russo", "Я тебя люблю"),
    ("Ucraniano", "Я тебе кохаю"),
    ("Bielorrusso", "Я цябе кахаю"),
    ("Grego", "Σ' αγαπώ"),
    ("Albanês", "Të dua"),
    ("Romeno", "Te iubesc"),
    ("Húngaro", "Szeretlek"),
    ("Turco", "Seni seviyorum"),
    ("Azerbaijano", "Mən səni sevirəm"),
    ("Georgiano", "მიყვარხარ"),
    ("Armênio", "Ես քեզ սիրում եմ"),
    ("Árabe", "أحبك"),
    ("Hebraico", "אני אוהב אותך"),
    ("Persa", "دوستت دارم"),
    ("Curdo", "Ez ji te hez dikim"),
    ("Pashto", "زه تا سره مینه لرم"),
    ("Urdu", "میں تم سے محبت کرتا ہوں"),
    ("Hindi", "मैं तुमसे प्यार करता हूँ"),
    ("Bengali", "আমি তোমাকে ভালোবাসি"),
    ("Punjabi", "ਮੈਂ ਤੈਨੂੰ ਪਿਆਰ ਕਰਦਾ ਹਾਂ"),
    ("Gujarati", "હું તને પ્રેમ કરું છું"),
    ("Marathi", "मी तुझ्यावर प्रेम करतो"),
    ("Nepalês", "म तिमीलाई माया गर्छु"),
    ("Cingalês", "මම ඔයාට ආදරෙයි"),
    ("Tâmil", "நான் உன்னை காதலிக்கிறேன்"),
    ("Telugu", "నేను నిన్ను ప్రేమిస్తున్నాను"),
    ("Canarês", "ನಾನು ನಿನ್ನನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ"),
    ("Malaiala", "ഞാൻ നിന്നെ സ്നേഹിക്കുന്നു"),
    ("Odia", "ମୁଁ ତୁମକୁ ଭଲ ପାଏ"),
    ("Assamês", "মই তোমাক ভাল পাওঁ"),
    ("Chinês mandarim", "我爱你"),
    ("Cantonês", "我愛你"),
    ("Japonês", "愛してる"),
    ("Coreano", "사랑해"),
    ("Mongol", "Би чамд хайртай"),
    ("Tibetano", "ང་ཁྱེད་རང་ལ་དགའ།"),
    ("Vietnamita", "Tôi yêu bạn"),
    ("Tailandês", "ฉันรักคุณ"),
    ("Laosiano", "ຂ້ອຍຮັກເຈົ້າ"),
    ("Khmer", "ខ្ញុំស្រឡាញ់អ្នក"),
    ("Birmanês", "မင်းကိုချစ်တယ်"),
    ("Indonésio", "Aku cinta kamu"),
    ("Malaio", "Saya cinta padamu"),
    ("Filipino", "Mahal kita"),
    ("Javanês", "Aku tresna karo kowe"),
    ("Sundanês", "Abdi bogoh ka anjeun"),
    ("Suaíli", "Nakupenda"),
    ("Zulu", "Ngiyakuthanda"),
    ("Xhosa", "Ndiyakuthanda"),
    ("Iorubá", "Mo nifẹ rẹ"),
    ("Igbo", "A hụrụ m gị n'anya"),
    ("Hauçá", "Ina son ka"),
    ("Amárico", "እወድሃለሁ"),
    ("Somali", "Waan ku jeclahay"),
    ("Oromo", "Sin jaalladha"),
    ("Kinyarwanda", "Ndagukunda"),
    ("Malgaxe", "Tiako ianao"),
    ("Shona", "Ndinokuda"),
    ("Sesoto", "Kea u rata"),
    ("Setswana", "Ke a go rata"),
    ("Lingala", "Nalingi yo"),
    ("Wolof", "Dama la bëgg"),
    ("Irlandês", "Tá grá agam duit"),
    ("Gaélico escocês", "Tha gaol agam ort"),
    ("Galês", "Rwy'n dy garu di"),
    ("Bretão", "Me az kar"),
    ("Basco", "Maite zaitut"),
    ("Catalão", "T'estimo"),
    ("Galego", "Quérote"),
    ("Maltês", "Inħobbok"),
    ("Luxemburguês", "Ech hunn dech gär"),
    ("Iídiche", "איך האָב דיך ליב"),
    ("Latim", "Te amo"),
    ("Esperanto", "Mi amas vin"),
    ("Crioulo haitiano", "Mwen renmen ou"),
)


class CoracaoAnimado(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coração animado em 100 idiomas")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(bg="#100816")

        self.canvas = tk.Canvas(
            self,
            width=800,
            height=600,
            bg="#100816",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.center_x = 400
        self.center_y = 290
        self.frame = 0
        self.draw_background()
        self.animate()

    def draw_background(self):
        for x, y, size in [
            (86, 84, 2), (174, 166, 1), (710, 100, 2), (640, 210, 1),
            (110, 430, 1), (700, 480, 2), (245, 500, 1), (550, 70, 1),
            (320, 100, 2), (500, 450, 1), (60, 280, 1), (750, 330, 1),
        ]:
            self.canvas.create_oval(
                x - size, y - size, x + size, y + size,
                fill="#ffd6e7", outline="",
            )

        self.canvas.create_text(
            400, 535,
            text="EU TE AMO EM 100 IDIOMAS",
            fill="#f6bed4",
            font=("Segoe UI", 13, "bold"),
        )

    def heart_points(self, scale):
        points = []
        for step in range(121):
            angle = math.tau * step / 120
            x = 16 * math.sin(angle) ** 3
            y = (
                13 * math.cos(angle)
                - 5 * math.cos(2 * angle)
                - 2 * math.cos(3 * angle)
                - math.cos(4 * angle)
            )
            points.extend((
                self.center_x + x * scale,
                self.center_y - y * scale,
            ))
        return points

    def animate(self):
        self.canvas.delete("heart")
        pulse = 1 + 0.055 * math.sin(self.frame * 0.12)
        points = self.heart_points(12 * pulse)

        self.canvas.create_polygon(
            points,
            fill="",
            outline="#ff4d8d",
            width=30,
            smooth=True,
            splinesteps=24,
            tags="heart",
        )
        self.canvas.create_polygon(
            points,
            fill="#ed246c",
            outline="#ff9cbd",
            width=3,
            smooth=True,
            splinesteps=24,
            tags="heart",
        )

        language, phrase = DECLARACOES_DE_AMOR[
            (self.frame // 50) % len(DECLARACOES_DE_AMOR)
        ]
        self.canvas.create_text(
            self.center_x,
            self.center_y - 8,
            text=phrase,
            fill="#ffffff",
            font=("Segoe UI", 18, "bold"),
            width=340,
            tags="heart",
        )
        self.canvas.create_text(
            self.center_x,
            self.center_y + 28,
            text=language,
            fill="#ffe1ec",
            font=("Segoe UI", 11),
            tags="heart",
        )

        self.frame += 1
        self.after(30, self.animate)


if __name__ == "__main__":
    app = CoracaoAnimado()
    app.mainloop()
