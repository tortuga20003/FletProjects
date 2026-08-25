import flet as ft

EMOJIS = ["😀", "😂", "🥰", "😍", "🤔"]
IDX = 0


def main(page: ft.Page):
    page.title = "EmojiApp"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input = ft.Text(value=EMOJIS[0], size=30)

    def refresh_click(e):
        global IDX
        btn = e.control

        if btn.icon == ft.Icons.ARROW_RIGHT_SHARP:
            IDX = IDX + 1
        else:
            IDX = IDX - 1

        IDX = IDX % len(EMOJIS)
        input.value = EMOJIS[IDX]

    btn_left = ft.IconButton(
        ft.Icons.ARROW_LEFT_SHARP,
        on_click=refresh_click
    )

    btn_right = ft.IconButton(
        ft.Icons.ARROW_RIGHT_SHARP,
        on_click=refresh_click
    )

    row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            btn_left,
            input,
            btn_right
        ]
    )

    page.add(row)


if __name__ == "__main__":
    ft.run(main)