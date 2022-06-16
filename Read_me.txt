bash path :
/mnt/c/projetf/projet_6_f/

sur python 3 tourner le code en parallèle :

for ((i=1; i<=15; i++))
do
    python3 Code_final_single.py $i &
done

python :

for ((i=1; i<=10; i++))
do
    python Code_final.py $i &
done

windows :

installer WSL et faire tourner sur wsl
