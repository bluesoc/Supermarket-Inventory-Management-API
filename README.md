<div align="center">
<h2>Supermarket Inventory Management API</h2>

![Last Commit](https://img.shields.io/github/last-commit/bluesoc/Supermarket-Inventory-Management-API/main)
[![Django CI](https://github.com/bluesoc/Supermarket-Inventory-Management-API/actions/workflows/django.yml/badge.svg)](https://github.com/bluesoc/Supermarket-Inventory-Management-API/actions/workflows/django.yml)

[![Docker Image CI](https://github.com/bluesoc/Supermarket-Inventory-Management-API/actions/workflows/docker-image.yml/badge.svg)](https://github.com/bluesoc/Supermarket-Inventory-Management-API/actions/workflows/docker-image.yml)

![Django Version](https://img.shields.io/badge/Django-4.2.11-yellowgreen)
![Repo Size](https://img.shields.io/github/repo-size/bluesoc/Supermarket-Inventory-Management-API)

</div>
<br>

**🔥 (Codebase in development)**

A backend API used to manage, update and delete internal products in a inventory system.

It uses Django Rest Framework, JSON format and caching to handle requests and responses, allowing interopability between systems.

***

### Current API endpoints
| Method   | Route          | Parameter                |
|----------|----------------|--------------------------|
| [GET]    | view/          | [optional int]           |
| [POST]   | create/        | name, category, quantity |
| [DELETE] | delete/<int>   | Int:id of product        |
| [PUT]    | update/<int>   | Int:id [extra fields]    |
| [GET]    | search?q=<str> | str=Item name            |

***

<a href="https://github.com/bluesoc/Supermarket-Inventory-Management-API/projects">IMS Software Engineering Project Page</a>
