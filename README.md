# Blockchain analytics tool using Django!

### Installation 
Download files to your project folder. Create virtual environment and use requirements to install required packages (you can use pip install -r /path/to/requirements.txt command).  Then save all the account addresses in database under Data model. Do not forget to make migrations
``` python
# the code below used to save all urls in the database

from .website.charts.models import Data

urls = "0x00000000219ab540356cbb839cbe05303d7705fa, 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, 0xda9dfa130df4de4673b89022ee50ff26f6ea73cf, ..."
# copy all top 100 accounts from accounts.txt
accounts = urls.split(", ")
j = 0
for account in accounts:
    obj = Data(address=account)
    obj.save()


```
###  Usage
Locate your command line location to folder with manage.py file and type python manage.py runserver. Now you can open web browser and connect to your local web server by typing http://127.0.0.1:8000/ in address bar. The interface is very simple just click on chart you want to see and then wait a little. It will open the required chart. All of the charts show top accounts by ETH balance.

If you want to create superuser and have access to the database from admin panel, type python manage.py createsuperuser. Now go to http://127.0.0.1:8000/admin and use your newly created account log in
### Examples
On the page below choose the chart you are interested in 
![index_page](https://user-images.githubusercontent.com/52863393/153463069-0ea6c7b0-e3f5-45f3-ba12-a6712aa51761.png)
![pie](https://user-images.githubusercontent.com/52863393/153463084-c693c0a9-23df-48cd-b48c-ce91117e32de.png)
![line](https://user-images.githubusercontent.com/52863393/153463103-ae89c1f9-f972-464b-bf22-466ad41fa315.png)
![bar](https://user-images.githubusercontent.com/52863393/153463110-515713a4-b12b-48e8-8bf3-0a40e08dec77.png)





