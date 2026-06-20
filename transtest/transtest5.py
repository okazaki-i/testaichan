#!/usr/bin/env python3
# https://qiita.com/magiclib/items/89447ffbf42371cd6538

import tkinter
from PIL import Image, ImageTk

class TransparentWindow():
    """透過画面"""

    FRAME_OFFSET = -2
    BG_COLOR = "white"

    def __init__(self, main, image, position=(0, 0), size=(0, 0)):
        """コンストラクタ"""

        self.main = main
        main.config(bg=self.BG_COLOR)
        self.image = image
        self.window_position = position
        self.window_size = size

        self.main.geometry(str(self.window_size[0]) + "x" +
                           str(self.window_size[1]) + "+" +
                           str(self.window_position[0]) + "+" +
                           str(self.window_position[1]))

        self.main.wm_overrideredirect(True)
        # 透過表示(くり抜き)色を指定
        self.main.wm_attributes("-transparentcolor",
                                self.BG_COLOR)
        # ウィンドウ全体が透過される
        # self.main.wm_attributes("-alpha", 0.7)

        self.init_canvas(self.main, self.image)

    def init_canvas(self, frame, image):
        """canvas初期化"""

        # canvas作成
        self.canvas = tkinter.Canvas(
            frame,
            width=image.width,
            height=image.height,
            bg=self.BG_COLOR
        )

        # 枠を消すためにマイナス値を指定
        self.canvas.place(x=self.FRAME_OFFSET,
                          y=self.FRAME_OFFSET)

        # クリックイベント
        self.canvas.bind('<Button-1>', self.click_canvas_event)

        # PIL.Image から PhotoImage 生成
        self.photo_image = ImageTk.PhotoImage(image=image)

        # # canvasに画像を表示
        self.canvas.create_image(
            self.photo_image.width() / 2,
            self.photo_image.height() / 2,
            image=self.photo_image)

    def click_canvas_event(self, event):
        """canvasクリックイベント"""

        print("click:(x:" + str(event.x) + ",y=" + str(event.y) + ")")

        self.main.quit()


if __name__ == '__main__':

    # 画像ファイルを開く
    pil_image = Image.open("./character.png")
    # サイズ調整 1/4
    pil_image = pil_image.resize(
        (int(pil_image.width / 4),
         int(pil_image.height / 4)),
        Image.HAMMING)

    # 透過画面表示
    root = tkinter.Tk()

    window_position = (root.winfo_screenwidth() - pil_image.width - 100,
                       root.winfo_screenheight() - pil_image.height - 50)

    TransparentWindow(main=root,
                      image=pil_image,
                      position=window_position,
                      size=(pil_image.width, pil_image.height))
    root.mainloop()
