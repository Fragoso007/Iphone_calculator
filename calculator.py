import flet as ft
from flet import colors
from decimal import Decimal

bottons = [
    {'operator':'AC', 'font': colors.BLACK, 'background': colors.BLUE_GREY_100},
    {'operator':'±', 'font': colors.BLACK, 'background': colors.BLUE_GREY_100},
    {'operator':'%', 'font': colors.BLACK, 'background': colors.BLUE_GREY_100},
    {'operator':'/', 'font': colors.WHITE, 'background': colors.ORANGE},
    {'operator':'7', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator':'8', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator':'9', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator':'*', 'font': colors.WHITE, 'background': colors.ORANGE},
    {'operator':'4', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator':'5', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator':'6', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator':'-', 'font': colors.WHITE, 'background': colors.ORANGE},
    {'operator':'1', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator':'2', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator':'3', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator':'+', 'font': colors.WHITE, 'background': colors.ORANGE},
    {'operator':'0', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator':'.', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator':'=', 'font': colors.WHITE, 'background': colors.ORANGE},
    ]

def main(page: ft.Page):
    page.bgcolor='#000'
    page.window_resizable = False
    page.window_width = 270
    page.window_height = 380
    page.title = "Calculator"
    page.window_always_on_top = True

    result = ft.Text(value ="0", color = colors.WHITE, size = 20)

    def calculate(operator, value_at):
        try:
            value = eval(value_at)

            if operator == '%':
                value /=100
            elif operator == '±':
                value = -value
            
        except:
            return 'Error'
        digits = min(abs(Decimal(value).as_tuple().exponent), 5)
            
        return format(value, f'.{digits}f')

    def select(e):
        value_at = result.value if result.value not in ('0', 'Error') else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in ('/', '*', '-', '+', '.'):
                value_at = value_at[:-1]

            value = value_at + value

            if value[-1] in ('=', '%', '±'):
                value = calculate(operator=value[-1], value_at=value_at)
        result.value = value
        result.update()

    display = ft.Row(
        width= 250, 
        controls= [result],
        alignment= 'end'
    )

    btn = [ft.Container(
        content=ft.Text(value=btn['operator'],color=btn['font']),
        width=50,
        height=50,
        bgcolor=btn['background'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click = select
        ) for btn in bottons]
    
    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btn,
        alignment='end'
    )

    page.add(display, keyboard)





ft.app(target = main)