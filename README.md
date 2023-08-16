<p align="center">
  <img src="src/assets/trust.jpg" alt="Trust Transact's Logo"/>
</p>

<br/>

<p align="center">
  <a href="https://docflex.notion.site/docflex/TrustTransact-The-Payment-Gateway-e289fbe82b1f4c8ea3a944b4e94065e5">
        <img src="https://img.shields.io/badge/DevLog%20HERE-NOTION-blue?style=for-the-badge&logo=notion" alt="Notion DevLog">
  </a>
  <a href="https://in.linkedin.com/in/r0m" target="_blank">
    <img alt="made-by-rehber" src="https://img.shields.io/badge/MADE%20BY-Rehber-blue?style=for-the-badge" />
  </a>
  <a href="https://choosealicense.com/licenses/mit/" target="_blank">
    <img alt="license" src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" />
  </a>

</p>

## 📋 Project Overview
🌐 Introducing TrustTransact: A Cutting-Edge Payment Gateway Revolution 🚀

In a world where digital transactions are ubiquitous, TrustTransact emerges as a beacon of innovation. Created to enhance the user experience for both customers and businesses, it streamlines payment procedures with finesse. 💳💼 Our primary objective is to make payment transactions as simple as possible while upholding the highest standards of security and dependability. 🔒📈 It is also prepared to be Dockerized. 🐳

Step into the future of payments with TrustTransact! Join us on this transformative journey. 🚀🔍
## 🔑 Key Features

* 🔌 Customizable Integration: TrustTransact provides well-documented APIs for simple integration with e-commerce platforms since it is designed for easy connection. 💻🌐

* 🕒 Real-time Payment Status: Real-time information on payment statuses is provided, enabling merchants to keep track of transactions and giving customers rapid confirmation. 🚀💰

* 🔔 Callback Notifications: TrustTransact enables automated callback notifications, decreasing the need for manual status checks by informing merchants of successful or unsuccessful payments. 📲📊

## 🔌 Technology Stack
* Django: The dependable and adaptable Django framework, renowned for creating web applications, powers this backend. 🐍🌐


* RESTful API: Now, easy connection between TrustTransact and other systems is made possible by a skillfully structured RESTful API architecture. This system guarantees efficient, uniform data interchange, supporting interoperability. 🌐🔌


* Database Management: By using a strong relational database system, data integrity and scalability are both rigorously maintained. 🗃️🔒📈


* Celery: Utilizing the Celery library enables effective management of asynchronous processes, including notifications and status verifications. 🌱🔧🚀


<h2 align="center"><b>🛠️ Technologies Used</b></h2>

<br>
    <p align="center">
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&amp;logo=python&amp;logoColor=ffdd54" alt="Python">
        <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&amp;logo=django&amp;logoColor=white" alt="Django">
        <img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&amp;logo=django&amp;logoColor=white&amp;color=ff1709&amp;labelColor=gray" alt="DjangoREST">
        <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&amp;logo=sqlite&amp;logoColor=white" alt="SQLite">
        <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&amp;logo=docker&amp;logoColor=white" alt="Docker">
    </p>
<br/>

## 🏃‍♂️Running The Project

Feel free to dive into the world of the TrustTransact Project DevLog! 🚀 Experience the journey of crafting an innovative payment gateway solution, from concept to reality. Join us as we discuss the highs, lows, and turning points that characterize human development. Explore the DevLog right away to avoid missing out, and check back for interesting developments! 📖🌟 [DevLog for Trust Transact](https://docflex.notion.site/docflex/TrustTransact-The-Payment-Gateway-e289fbe82b1f4c8ea3a944b4e94065e5)


### Step 1: Cloning the Repository 📥 

```
git clone https://github.com/docflex/trust-transact.git
```

### Step 2: Creating a Virtual Environment 🌐 

The reason why we do this is explained in the DevLog Mentioned Above. Please Check it out for a Deeper Dive into this Project.

```
python3 -m venv venv
```

Next, You will be needing to switch to the Virtual Environment. To do so, Run:
```
source venv/bin/activate
```

### Step 3: Installing the Dependencies 📦

```
pip install -r backend/requirements.txt
```

### Step 4: Fixing Environment Variables 🔧

```
cp env.template .env
```

### Step 5: Make Migrations 🗂️

```
cd backend

python3 manage.py makemigrations

python3 manage.py migrate
```

### Step 6: Run Server 🚀

```
python3 manage.py runserver     
```

### Step 7: Test Endpoints 🧪

Testing the createPayment Endpoint:
```
curl -X POST -H "Content-type: application/json" -d '{"order_id": "1000", "order_amount": 100}' 'http://127.0.0.1:8000/createPayment/'
```

Testing the getPaymentStatus Endpoint:
```
curl -X POST -H "Content-type: application/json" -d '{"order_id": "1000"}' 'http://127.0.0.1:8000/getPaymentStatus/'   
```

### Step 8: Checking Database 🗃️


Open the Shell to Interact with the Database
```
python3 manage.py shell
```

To query all the data in the database run:
```
from paymentProcessor.models import Order

orders = Order.objects.all()
for order in orders:
    print(order.order_id, order.order_amount, order.order_meta)
```