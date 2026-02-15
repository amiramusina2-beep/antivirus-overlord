<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Amir OS - JavaScript Edition</title>
    <style>
        /* Весь внешний вид (CSS) */
        body { margin: 0; font-family: 'Segoe UI', Tahoma, sans-serif; overflow: hidden; background: #008080; }

        /* Рабочий стол */
        #desktop { width: 100vw; height: 100vh; position: relative; }

        .icon {
            width: 80px; color: white; text-align: center;
            padding: 20px; cursor: pointer; user-select: none;
        }
        .icon:hover { background: rgba(255,255,255,0.1); }

        /* Окно */
        .window {
            position: absolute; top: 100px; left: 100px;
            width: 350px; background: #f0f0f0;
            border: 1px solid #000; box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
            display: none; flex-direction: column;
        }

        .window-header {
            background: linear-gradient(90deg, #000080, #1084d0);
            color: white; padding: 5px 10px;
            display: flex; justify-content: space-between;
            cursor: move; /* Курсор перемещения */
            user-select: none;
        }

        .close-btn { background: #c0c0c0; border: 1px solid black; cursor: pointer; font-weight: bold; width: 20px; text-align: center; }
        .close-btn:hover { background: #ff5f5f; }

        .window-content { padding: 20px; color: #333; height: 150px; }

        /* Панель задач */
        .taskbar {
            position: absolute; bottom: 0; width: 100%; height: 40px;
            background: #d4d4d4; border-top: 2px solid white;
            display: flex; align-items: center; padding: 0 10px; box-sizing: border-box;
        }

        .start-btn { font-weight: bold; padding: 2px 10px; background: #c0c0c0; border: 2px outset white; cursor: pointer; }
        .start-btn:active { border-style: inset; }

        .clock { margin-left: auto; font-size: 14px; border-left: 1px solid #888; padding-left: 10px; }
        
        #weapon-status { margin-top: 15px; padding: 5px; border: 1px dashed #888; font-weight: bold; }
    </style>
</head>
<body>

<div id="desktop">
    <div class="icon" ondblclick="toggleWindow('win-inv')">
        <img src="https://cdn-icons-png.flaticon.com/512/1065/1065535.png" width="40" draggable="false">
        <div>Инвентарь</div>
    </div>

    <div id="win-inv" class="window">
        <div class="window-header" id="win-inv-header">
            <span>Оружейная</span>
            <div class="close-btn" onclick="toggleWindow('win-inv')">x</div>
        </div>
        <div class="window-content">
            <p>Выберите снаряжение:</p>
            <button onclick="pickWeapon('🔥 Огненный меч')">Меч</button>
            <button onclick="pickWeapon('🏹 Длинный лук')">Лук</button>
            <button onclick="pickWeapon('🛡️ Тяжелый щит')">Щит</button>
            
            <div id="weapon-status">Оружие не выбрано</div>
        </div>
    </div>

    <div class="taskbar">
        <div class="start-btn">Пуск</div>
        <div class="clock" id="clock">00:00:00</div>
    </div>
</div>

<script>
    // 1. Логика выбора оружия (исправляем твою проблему)
    function pickWeapon(name) {
        const status = document.getElementById('weapon-status');
        status.innerText = "Экипировано: " + name;
        status.style.color = "blue";
        console.log("Amir: выбрано оружие - " + name);
    }

    // 2. Открытие/Закрытие окон
    function toggleWindow(id) {
        const win = document.getElementById(id);
        win.style.display = (win.style.display === 'none' || win.style.display === '') ? 'flex' : 'none';
    }

    // 3. Часы
    function updateTime() {
        document.getElementById('clock').innerText = new Date().toLocaleTimeString();
    }
    setInterval(updateTime, 1000);
    updateTime();

    // 4. СКРИПТ ПЕРЕТАСКИВАНИЯ (Drag and Drop)
    dragElement(document.getElementById("win-inv"));

    function dragElement(elmnt) {
        var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
        const header = document.getElementById(elmnt.id + "-header");
        
        if (header) {
            header.onmousedown = dragMouseDown;
        }

        function dragMouseDown(e) {
            e.preventDefault();
            pos3 = e.clientX;
            pos4 = e.clientY;
            document.onmouseup = closeDragElement;
            document.onmousemove = elementDrag;
        }

        function elementDrag(e) {
            e.preventDefault();
            pos1 = pos3 - e.clientX;
            pos2 = pos4 - e.clientY;
            pos3 = e.clientX;
            pos4 = e.clientY;
            elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
            elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
        }

        function closeDragElement() {
            document.onmouseup = null;
            document.onmousemove = null;
        }
    }
</script>

</body>
</html>