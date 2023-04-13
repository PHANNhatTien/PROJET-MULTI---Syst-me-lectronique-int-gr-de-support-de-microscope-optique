# PROJET-MULTI---Systeme-lectronique-integre-de-support-de-microscope-optique
# Système Intégré de Support de Microscope Électronique au LNCMI

Ce projet multidisciplinaire réalisé au LNCMI consiste en la conception et l'installation d'un modèle de support de microscope électronique intégré. Ce système est équipé de diverses fonctionnalités permettant un positionnement précis et efficace de l'échantillon, ainsi qu'un contrôle de la température. Le système comprend un mécanisme de translation à 3 axes et un système de rotation à 3 axes pour un ajustement précis de la position de l'échantillon. De plus, un contrôleur automatique de température pour l'échantillon est intégré au système, garantissant une température stable pendant l'observation. L'ensemble du système est contrôlé par un puissant processeur Raspberry Pi Pico, capable d'exécuter des instructions complexes et de fournir des retours en temps réel.

## Configuration

### Prérequis

- Raspberry Pi Pico
- Matériel de support de microscope électronique
- Contrôleur de température automatique
- Câbles et connecteurs nécessaires

### Installation

1. Clonez ce dépôt GitHub sur votre ordinateur local ou votre Raspberry Pi.
2. Installez les dépendances requises en exécutant la commande suivante dans le répertoire du projet :
   ```
   pip install -r requirements.txt
   ```
3. Connectez le Raspberry Pi Pico au système de support de microscope électronique et au contrôleur de température automatique.
4. Chargez le code du projet sur le Raspberry Pi Pico en suivant les instructions officielles de la [documentation Raspberry Pi Pico](https://www.raspberrypi.org/documentation/pico/getting-started/).

## Utilisation

1. Mettez sous tension le Raspberry Pi Pico et le système de support de microscope électronique.
2. Exécutez le script principal pour démarrer le contrôle du système :
   ```
   python main.py
   ```
3. Utilisez les commandes fournies par l'interface utilisateur pour ajuster la position de l'échantillon et la température.
4. Suivez les instructions à l'écran pour effectuer des réglages supplémentaires, tels que le choix de la méthode de contrôle de la température.

## Support

Si vous rencontrez des problèmes lors de l'installation ou de l'utilisation du système, veuillez ouvrir une issue sur ce dépôt GitHub. Nous nous efforcerons de vous fournir une assistance dans les plus brefs délais.

## Licence

Ce projet est distribué sous la licence [MIT](LICENSE).
