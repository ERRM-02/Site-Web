@echo off
echo Lancement de la mise a jour du site...

echo ====================================
echo 1. Telechargement des dernieres modifications (git pull)
echo ====================================
git pull

echo ====================================
echo 2. Execution du script Python
echo ====================================
python "mise_a_jour_site.py"

echo ====================================
echo 3. Sauvegarde des modifications (git add et commit)
echo ====================================
git add .
git commit -m "Mise a jour automatique du site (ajouts de photos ou autres)"

echo ====================================
echo 4. Envoi vers le serveur (git push)
echo ====================================
git push

echo.
echo ====================================
echo MISE A JOUR TERMINEE AVEC SUCCES !
echo ====================================
pause
