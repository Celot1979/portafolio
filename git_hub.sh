#!/bin/bash

echo "¿Qué acción quieres realizar?"
echo "1) Trabajar y hacer commit en la rama experimental"
echo "2) Volver a la rama segura 'blog'"
echo "3) Borrar la rama experimental local y en GitHub"
read -p "Elige una opción (1/2/3): " opcion

case $opcion in
  1)
    read -p "Nombre de la rama experimental (por defecto: feature/experimentos): " rama
    rama=${rama:-feature/experimentos}
    # Comprobar si la rama ya existe
    if git show-ref --verify --quiet refs/heads/"$rama"; then
      echo "La rama '$rama' ya existe localmente. Cambiando a esa rama..."
      git checkout "$rama"
    else
      echo "Creando y cambiando a la rama '$rama'..."
      git checkout -b "$rama"
      git push -u origin "$rama"
    fi
    echo "Ahora estás en la rama $rama. Haz tus cambios y commits normalmente."
    ;;
  2)
    echo "Cambiando a la rama 'blog' y sincronizando con GitHub..."
    git checkout blog && git fetch origin && git reset --hard origin/blog
    echo "Has vuelto a la rama 'blog' y tu entorno local está igual que en GitHub."
    ;;
  3)
    read -p "Nombre de la rama experimental a borrar (por defecto: feature/experimentos): " rama
    rama=${rama:-feature/experimentos}
    if [ "$(git rev-parse --abbrev-ref HEAD)" = "$rama" ]; then
      echo "No puedes borrar la rama en la que estás. Cambiando a 'blog'..."
      git checkout blog
    fi
    if git show-ref --verify --quiet refs/heads/"$rama"; then
      git branch -D "$rama"
      echo "Rama local '$rama' eliminada."
    else
      echo "La rama local '$rama' no existe."
    fi
    git push origin --delete "$rama"
    echo "La rama remota '$rama' ha sido eliminada de GitHub (si existía)."
    ;;
  *)
    echo "Opción no válida."
    ;;
esac