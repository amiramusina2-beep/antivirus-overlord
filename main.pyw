import flet as ft
import os

def main(page: ft.Page):
    # --- НАСТРОЙКИ ЭКРАНА ПОД ТЕЛЕФОН ---
    page.title = "Antivirus Overlord"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505" # Глубокий черный
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- ЭЛЕМЕНТЫ ИНТЕРФЕЙСА ---
    icon = ft.Icon(ft.icons.SHIELD_SHARP, color="red", size=100)
    
    title = ft.Text(
        "SYSTEM OVERLORD", 
        size=24, 
        weight="bold", 
        color="red",
        text_align=ft.TextAlign.CENTER
    )
    
    status = ft.Text(
        "Сканер готов к работе", 
        size=16, 
        color="white54"
    )

    progress_bar = ft.ProgressBar(width=250, color="red", visible=False)

    def start_scan(e):
        scan_btn.disabled = True
        progress_bar.visible = True
        status.value = "ПОИСК ВИРУСОВ..."
        status.color = "red"
        page.update()
        
        # Здесь могла быть логика, но пока просто имитация для красоты
        import time
        time.sleep(2) 
        
        status.value = "УГРОЗЫ НЕ ОБНАРУЖЕНЫ"
        status.color = "green"
        progress_bar.visible = False
        scan_btn.disabled = False
        page.update()

    scan_btn = ft.ElevatedButton(
        text="ЗАПУСТИТЬ",
        icon=ft.icons.PLAY_ARROW,
        style=ft.ButtonStyle(
            color="white",
            bgcolor="red",
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        width=200,
        height=50,
        on_click=start_scan
    )

    # Собираем всё в одну колонку
    layout = ft.Column(
        [
            icon,
            title,
            status,
            ft.Container(height=10), # Отступ
            progress_bar,
            ft.Container(height=10), # Отступ
            scan_btn,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    page.add(layout)

# --- ВАЖНО ДЛЯ ХОСТИНГА (Render/Koyeb) ---
if __name__ == "__main__":
    # Берем порт из настроек сервера или ставим 8080 по умолчанию
    port = int(os.getenv("PORT", 8080))
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=port, host="0.0.0.0")
