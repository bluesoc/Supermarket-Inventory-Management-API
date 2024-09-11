#!/bin/bash
# This script will post some sample products.
# It was generated to test the API methods.

# Server IP
IP="http://127.0.0.1"

# Server Port
PORT=8000

# Fruits
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Apples","category":"Fruits","quantity":10,"price":1.50,"manufacturer":"FruitCo","description":"Crisp and juicy apples."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Bananas","category":"Fruits","quantity":6,"price":0.25,"manufacturer":"FruitCo","description":"Ripe and sweet bananas."}'

# Dairy
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Milk","category":"Dairy","quantity":20,"price":0.99,"manufacturer":"DairyBest","description":"Fresh whole milk."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Eggs","category":"Dairy","quantity":12,"price":3.00,"manufacturer":"Eggcellent","description":"Farm-fresh eggs."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Yogurt","category":"Dairy","quantity":10,"price":0.99,"manufacturer":"DairyDelight","description":"Creamy yogurt with fruit."}'

# Pantry
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Pasta","category":"Pantry","quantity":5,"price":1.75,"manufacturer":"PastaPerfect","description":"Delicious spaghetti for your favorite dishes."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Tomato Sauce","category":"Pantry","quantity":5,"price":2.00,"manufacturer":"Saucy","description":"Rich and flavorful tomato sauce."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Rice","category":"Pantry","quantity":10,"price":1.20,"manufacturer":"GrainGoodness","description":"Fluffy white rice for your meals."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Peanut Butter","category":"Pantry","quantity":5,"price":2.75,"manufacturer":"NuttyDelight","description":"Creamy peanut butter for spreading."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Spices","category":"Pantry","quantity":5,"price":1.50,"manufacturer":"FlavorMasters","description":"A variety of spices to enhance your dishes."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Canned Beans","category":"Pantry","quantity":5,"price":1.00,"manufacturer":"BeanBuddies","description":"Nutritious canned beans for quick meals."}'

# Snacks
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Chocolate Chip Cookies","category":"Snacks","quantity":5,"price":4.50,"manufacturer":"CookieMonster","description":"Delicious cookies with chocolate chips."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Granola Bars","category":"Snacks","quantity":5,"price":3.00,"manufacturer":"SnackTime","description":"Healthy granola bars for on-the-go."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Tortilla Chips","category":"Snacks","quantity":5,"price":2.50,"manufacturer":"CrunchySnacks","description":"Crispy tortilla chips for dipping."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Nut Mix","category":"Snacks","quantity":5,"price":5.00,"manufacturer":"NuttyBuddies","description":"A mix of delicious nuts for snacking."}'

# Beverages
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Orange Juice","category":"Beverages","quantity":5,"price":3.20,"manufacturer":"JuicyFresh","description":"Freshly squeezed orange juice."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Soda","category":"Beverages","quantity":5,"price":1.50,"manufacturer":"FizzCo","description":"Refreshing soda in various flavors."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Coffee","category":"Beverages","quantity":5,"price":5.00,"manufacturer":"BrewMasters","description":"Rich and aromatic coffee."}'
curl -X POST "$IP:$PORT/create/" -H "Content-Type: application/json" -d '{"name":"Tea","category":"Beverages","quantity":5,"price":3.00,"manufacturer":"TeaTime","description":"Soothing tea for relaxation."}'
