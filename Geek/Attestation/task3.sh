# Для создания директории и перемещения файла в нее можно использовать команды mkdir и mv. Например:
sudo echo "deb http://repo.mysql.com/apt/ubuntu/ bionic mysql-8.0" >> /etc/apt/sources.list

# Затем необходимо обновить список пакетов и установить выбранный пакет. Например:
sudo apt update
sudo apt install mysql-community-server