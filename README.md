# fincare

“Finance” + “Healthcare” -> healthcare finance / financial care

A Django-based web application to manage and streamline financial operations in healthcare institutions.

> [!Note] Where am I? What to do next?
> I want to strat over the app development. Because I have tried once using AI tools to develop the app on demand, but the result is not satisfactory. I saw basic conflicts with authentication functions. Anyone can access the entry page without login. I also found a better way to restructure the project folder. So I decide to scrap the previous work and start over again. Furthermore, I want to create prompts files (e.g. `.github/prompts/new-a-django-proj.prompt.md`) to guide the development process step by step. This will help me to keep track of the requirements and ensure that all necessary features are implemented correctly.
> 
> I am on the `dev-prompts` branch. 

## Features

- [ ] Mobile friendly.
- [ ] Per-user login
- [ ] Log income or spending by category/date
- [ ] Admin views for reporting
- [ ] User authentication and role-based access control
- [ ] Database models for financial records
- [ ] Logging of financial transactions (income, expenses, payments)
- [ ] Dashboard for financial overview and reports
- [ ] Security measures to protect sensitive financial data
- [ ] Ready for deployment with Railway
- [ ] Multi-language support (i18n) (English and Traditional Chinese)

## Author

This application was created and developed by [wudaudau](https://github.com/wudaudau/fincare/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Installation

(placeholder for installation instructions)

## Usage Examples

(placeholder for usage examples)

## Project Structure

The project structure is as follows:
fincare/
├── manage.py
├── core/                       # Django project settings
│   ├── __init__.py
│   ├── settings.py             # Django settings
│   ├── asgi.py         # ASGI configuration
│   ├── urls.py                 # URL routing
│   └── wsgi.py                # WSGI configuration
├── apps/
│   ├── finance/        # Finance app
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── authentication/       # User authentication and profile management app
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── dashboard/            # Dashboard and reporting app
│   │   ├── __init__.py
│   │   ├── views.py
│   │   └── urls.py
│   └── static/               # Static files (CSS, JS, images)
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/               # Templates used to render HTML pages
│   │   ├── includes/        # HTML chunks and components
│   │   ├── finance/        # Finance app templates
│   │   ├── authentication/       # Authentication app templates
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── profile.html
│   │   └── dashboard/            # Dashboard app templates
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
