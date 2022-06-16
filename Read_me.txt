Pour faire tourner le script une seule fois il faut executer : Code_final_single.py depuis un IDE ou directement sur terminal
Attention cette version du code a pour but le débugage. Il est préférable de compiler le code en parallèle avec la méthode ci-dessous
-------------------------------------------------------------------------------------------------------------------------------------------------------

Coller l'un des deux codes bash suivant depuis le répertoire du code pour faire tourner le code en parallèle :
Une fois les scripts compilés ils enregistrent des gif dans le sous répértoire fig/gif/ et l'image final de la trace du muons directement dans fig
-------------------------------------------------------------------------------------------------------------------------------------------------------
sur python 3  :

for ((i=1; i<=15; i++))
do
    python3 Code_final.py $i &
done
-------------------------------------------------------------------------------------------------------------------------------------------------------

python :

for ((i=1; i<=10; i++))
do
    python Code_final.py $i &
done
-------------------------------------------------------------------------------------------------------------------------------------------------------

windows :

installer WSL et faire tourner sur wsl
-------------------------------------------------------------------------------------------------------------------------------------------------------

bash path :
/mnt/c/projetf/projet_6_f/
-------------------------------------------------------------------------------------------------------------------------------------------------------
