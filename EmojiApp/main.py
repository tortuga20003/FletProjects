import flet as ft

# lista de emojis que irão aparecer no app
# essa lista pode ser ampliada, o aplicativo irá lidar com isso
EMOJIS = ["😀", "😂", "😍", "😎", "🤔", "😢", "😡", "👍", "👎", "🎉"]

# IDX controla o índice da lista de emojis. Sempre estará
# atualizado com o índice do emoji que está sendo exibido
# na tela.
IDX = 0


# a função main recebe o objeto página, que carrega todos
# os elementos gráficos (controls).
# Page é criado pelo framework flet durante a execução.
def main(page: ft.Page):

    # ---- configurações da página
    # editar a título da janela/aba do navegador/nome do app
    page.title = "EmojiApp"

    # alinha verticalmente o elemento (control) que foi inserido na página
    # ft.MainAxisAlignment.CENTER -> centraliza o conteúdo verticalmente
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    # ---- meus elementos (controls)
    # ft.Text -> Elemento textual
    # parametro value deste objeto contém o valor mostrado na tela
    input = ft.Text(value=EMOJIS[0])


    # ---- função aninhada na main
    # Esta é a função que é executada ao clicar em "btn".
    # A função é aninhada à main para que ela consiga acessar as variáveis
    # declaradas na função main (ex. variável input).
    # A função acresce o valor de IDX para mostrar o próximo emoji da lista
    # O parâmetro "e" da função carrega informações sobre o evento executado,
    # é possível acessar a partir de "e" o elemento que sofreu o evento.
    def refresh_click(e):
        global IDX

        # Incremento circular:
        #   * Acresce IDX em 1
        #   * Se IDX > tamanho de EMOJIS
        #       * IDX volta para 0
        # OBS: IDX nunca passa do maior índice da lista
        # IDX = 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, ...
        IDX = (IDX + 1) % len(EMOJIS)

        # altera o elemento textual para o emoji da posição IDX
        input.value = EMOJIS[IDX]


    # Elemento botão com ícone de "atualizar" (REFRESH)
    # ft.Icons.REFRESH -> fornece o ícone de "atualizar"
    # on_click -> corresponde ao apontamento da função "refresh_click",
    # que será executada toda vez que o botão "btn" for clicado.
    btn = ft.IconButton(ft.Icons.REFRESH, on_click=refresh_click)


    # Elemento de layout
    # ft.Row -> constrói uma linha no aplicativo.
    # Cada linha item inserido em "controls" irá ser posicionado em
    # coluna desta linha.
    # "input" e "btn" ficarão lado a lado.
    # alignment -> alinha os elementos ao centro da linha.
    row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            input,
            btn
        ]
    )


    # adicionando elementos na página
    # como "row" contém "input" e "btn", basta inserir "row"
    # para ver todos os elementos criados.
    page.add(row)


if __name__ == "__main__":
    # ft.app -> dá início a execução do aplicativo
    # target -> aponta para a função que irá manipular a página
    # do app.
    ft.app(target=main)