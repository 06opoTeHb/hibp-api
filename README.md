# hibp-api
# Educational purposes only
Permet d'utiliser l'api de HIBP gratuitement

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## 💡 Prérequis
   [Python 2/3](https://www.python.org/downloads/release/python-370/)
## 🛠️ Installation
### Avec PyPi
```pip3 install hibp-api```
### Avec le github
```bash
git clone https://github.com/megadose/hibp-api.git
cd hibp-api/
python3 setup.py install
```
## 📈 Usage
```python
from hibp import *
print(hibp.email("test@example.com"))
```
## 📚 Exemple
```bash
python3 HIBP_test.py -e test@example.com
```
## Exemple de projet : [!]Maltego HIBP()

## 📝 License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)
