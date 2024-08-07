# from subprocess import check_output as t 
# from platform import system as s
# from re import findall as f
# def wifi_names():
# # Запись вывода в переменную, с терминала, по запросу вывода всех файлов хранящих пароль от точек доступа
#     response = t('cd /etc/NetworkManager/system-connections/ && ls', shell=True)
# # Получение чистого списка имён Wi-Fi
#     wifi_names_list = response.decode().split('\n')[0:-1]
#     return wifi_names_list


# def passwords(wifi_name):
# # Запись вывода в переменную, с терминала, по запросу вывода информации о конкретной точки доступа
#     response = t(f'cd /etc/NetworkManager/system-connections/ && sudo cat {wifi_name}', shell=True)

# # Поиск пароля с помощью регулярного выражения
#     try: return f('(?:npsk=)(.*)', str(response))[0].split('\\n\\n')[0]
#     except: return None

# def main():
# # Список хронящий все имена и пароли Wi-Fi сетей
#     wifi_list = []    
# # Цикл получения спика всех имён сетей, и их пароля
#     for wifi_name in wifi_names():
#         name = wifi_name.split('.nmconnection')[0]
#         password = passwords(wifi_name)
#         wifi_list.append({'name': name, 'password': password})
#     return wifi_list

# if __name__ == '__main__':
#     print(main())

import tkinter as tk
import subprocess
def display_wifi_info():
    #nmcli general status && nmcli device wifi && nmcli connection show --active"
    command = "nmcli general status && nmcli device wifi && nmcli connection show --active"
    try:
        wifi_info = subprocess.check_output(command, shell=True).decode().strip()
    except subprocess.CalledProcessError:
        wifi_info = "Error retrieving page errors"
    
    root = tk.Tk()
    root.title("WIFI Info")
    
    
    label = tk.Label(root, text="{}".format(wifi_info))
    label.pack()
    
    root.mainloop()
