# Django Blog Project

## Project Overview

This is a simple Django blog project that allows users to create, read, update, and delete (CRUD) blog posts. Authenticated users can manage their posts, while all visitors can view posts.

## Features

- List all blog posts (accessible to everyone)
- View individual blog posts in detail
- Authenticated users can create new posts
- Authors can edit or delete their own posts
- Permissions ensure that only authors can modify or delete their posts
- Templates and static files (CSS/JS) for a clean user interface

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd django_blog
```

## Tags & Search

- Tags: Authors can add comma-separated tags when creating or editing a post. Click on a tag to view all posts with that tag.
- Search: Use the search box on the posts page to find posts by title, content, or tag names. Search URL: /search/?q=keyword
