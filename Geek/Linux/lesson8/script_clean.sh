#!/bin/bash

# Проверяем, передан ли путь к директории
if [ -z "$1" ]
then
  echo "Ошибка: не указан путь к директории"
  exit 1
fi

# Проверяем, существует ли указанная директория
if [ ! -d "$1" ]
then
  echo "Ошибка: директория не существует"
  exit 1
fi

# Удаляем все файлы с расширениями .bak, .tmp, .backup
find "$1" -type f \( -name "*.bak" -o -name "*.tmp" -o -name "*.backup" \) -delete

echo "Директория $1 очищена от файлов с расширениями .bak, .tmp, .backup"