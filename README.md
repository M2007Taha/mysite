## Django Learning Project

This repository is dedicated to learning and exploring the Django web framework. It serves as a playground to experiment with core concepts, build simple applications, and solidify understanding of Django functionalities.

### Getting Started

This project assumes you have Python and pip installed on your system.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/M2007Taha/django-learning.git
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

   This will launch the server on `http://127.0.0.1:8000/` by default. You can access the Django admin interface at `http://127.0.0.1:8000/admin/`.

### Project Structure

The project structure follows the standard Django conventions:

* `mysite`: The main Django project directory.
* `mysite/settings.py`: Global project configurations.
* `mysite/urls.py`: Defines URL patterns for the mysite.
* `mysite/wsgi.py`: Entry point for the WSGI server.
* `website` : My Django application directory.
* `website/urls.py` : Defines URL patterns for the website.
* `website/views.py` : It holds Django view functions that process user requests and generate web responses.
* `website/templates` : It stores HTML templates used by Django views to render dynamic web pages.
* `website/static` : Contains static files (CSS, JavaScript, images) served directly by the web server.

### Learning Resources

Here are some helpful resources for learning Django:

* **Official Django Documentation:** [https://docs.djangoproject.com/en/5.0/](https://docs.djangoproject.com/en/5.0/)
* **Django Girls Tutorial:** [https://tutorial.djangogirls.org/en/](https://tutorial.djangogirls.org/en/)
* **Django Tutorial (Step-by-Step):** [https://github.com/consideratecode/django-tutorial-step-by-step](https://github.com/consideratecode/django-tutorial-step-by-step)
* **Many more online tutorials and courses**

### Contributing

Feel free to experiment, create new features, and explore different Django functionalities within this project. You can also contribute by creating issues or pull requests to share your learnings and improvements.


Happy learning!
