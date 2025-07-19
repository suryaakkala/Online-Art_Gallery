# 🎨 Online Art Gallery

An online platform to showcase, upload, and explore artwork. Users can sign up, log in, view artwork collections, upload their own, and add favorites to a cart-style gallery.

## 🔧 Features

- User authentication (sign up/login)
- Upload and browse artwork
- Responsive landing page and gallery UI
- Shopping cart-like collection system
- Profile view with restricted access to certain pages
- Custom admin interface

## 🛠 Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite3
- **Tools**: Django Admin, Forms, Staticfiles

## 🏁 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/suryaakkala-online-art_gallery.git
cd suryaakkala-online-art_gallery
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations and start the server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 5. Access the app

Open `http://127.0.0.1:8000/` in your browser.

---

## 📂 Project Structure (Shortened)

```
suryaakkala-online-art_gallery/
├── art_gallery/            # Main Django settings
├── gallery/                # Core app for artwork, forms, views
├── login/                  # Separate login app (optional extension)
├── static/                 # Static files (CSS/JS)
└── templates/              # HTML templates
```

---

## 👥 Team

- **Surya Akkala** (Team Lead, Backend Developer)  
  GitHub: [@suryaakkala](https://github.com/suryaakkala)

- **Sruthi Kanneti** – Frontend Developer  
  GitHub: [@Sruthi-3-0](https://github.com/Sruthi-3-0) 
- **G. Karuna Sri** – Frontend Developer  
  GitHub: [@Karunasri921](https://github.com/Karunasri921)

---

## 📄 License

This project is for academic and demonstration purposes.
