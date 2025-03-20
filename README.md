Blog Project
![alt text](sss.jpg)
Overview

This is a Django-based blog application that allows users to create, manage, and interact with blog posts. It includes features such as authentication, likes, notifications, user profiles, and an AI chat feature.

Features

User authentication (sign up, login, logout)

Create, edit, and delete blog posts

Like system for blog posts

Comment notifications

User profiles displaying all blogs created by a user

AI chat feature for handling blog-related queries (using Gemini API)

Installation

Prerequisites

Ensure you have the following installed:

Python 3.x

Django

SQLite (or another preferred database)

Steps

Clone the repository:

Create and activate a virtual environment:

Install dependencies:

Apply migrations:

Create a superuser (admin panel access):

Run the development server:

Access the application at http://127.0.0.1:8000/.

Usage

Users can register, log in, and create blog posts.

They can like posts and receive notifications for comments.

The AI chat feature assists users with blog-related queries.

Project Structure

Applications and Functions

Blog App (blog/)

blog_list: View all blog posts

create_blog_post: Create a new blog post

edit_blog_post: Edit an existing post

delete_blog_post: Delete a blog post

like_post: Like a blog post

notifications_view: View notifications

mark_notifications_as_read: Mark notifications as read

blog_detail: View details of a blog post

Comments App (comments/)

add_comment: Add a comment to a blog post

add_reply: Add a reply to a comment

Users App (users/)

RegisterPage: User registration page

LoginPage: User login page

LogoutUser: User logout function

HomePage: Homepage view

ProfilePage: User profile view

Talk With AI App (talk_with_ai/)

AI chat functionality (Currently no defined functions in views.py)

API Keys

For the AI chat feature, add your Gemini API key in the environment variables or settings file: