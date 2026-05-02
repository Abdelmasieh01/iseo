# ISEO Website — Phase 4: Physical Implementation
**ISOM 331 · System Analysis and Design · Spring 2026**
**Kuwait University, College of Business Administration**
**Instructor: Dr. Kamel Rouibah**

---

## Project Overview

This is the Phase 4 physical implementation of the **International Student Exchange Office (ISEO) website** — "Connect, Apply, Explore" — built using Django (Python web framework).

The system was built based on requirements gathered in Phase 3 through benchmarking (Cornell, FIU), user scenario analysis, secondary research (Google Scholar / IEEE), and heuristic evaluation.

---

## Team Members

| Name | Student ID |
|------|-----------|
| Jumanah Mourad | 2192115669 |
| Ghaneemah Alrujaib | 2211123553 |
| Sarah Almutairi | 2221175012 |
| Almaha Alajmi | 2221147629 |

---

## Setup Instructions

### Requirements
- Python 3.10 or higher
- pip

### Steps

```bash
# 1. Navigate to the project folder
cd iseo_project

# 2. Install Django
pip install django

# 3. Run migrations
python manage.py makemigrations
python manage.py migrate

# 4. Load university data
python manage.py loaddata iseo/fixtures/universities.json

# 5. Create admin account (optional but recommended)
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Open your browser to: **http://127.0.0.1:8000**

Admin panel: **http://127.0.0.1:8000/admin**

---

## Website Features (Functions Implemented)

### 1. Home Page (`/`)
- Hero section with program overview
- Statistics bar (partner count, countries, semesters)
- 4-step process guide
- Featured partner universities
- CTA (Call to Action) band

### 2. About Page (`/about/`)
- ISEO office mission and description
- Phase 3 requirements context
- Team members with student IDs
- Office contact information

### 3. Partner Universities (`/programs/`)
- Full filterable directory of all partner universities
- Filter by country via dropdown
- Shows: min GPA, language requirement, deadline, available slots

### 4. Eligibility Page (`/eligibility/`)
- Academic standing requirements
- Enrollment status criteria
- Language requirements
- Required documents list
- **Interactive GPA checker** (JavaScript tool)
- FAQ section

### 5. Application Form (`/apply/`)
- **Section 1:** Personal Information (name, student ID, email, nationality, passport)
- **Section 2:** Academic Information (GPA, program, level, language proficiency)
- **Section 3:** Exchange Preferences (1st/2nd choice university, semester, year)
- **Section 4:** Personal Statement
- Server-side form validation
- Unique reference number generated automatically on submission

### 6. Application Success (`/apply/success/<ref>/`)
- Confirmation page with reference number
- Summary of submitted application
- Next steps information

### 7. Track Application Status (`/track/`)
- Lookup by reference number + student ID
- Visual status timeline (Pending → Under Review → Decision)
- Full application summary display
- Admin notes display if set

### 8. Contact Page (`/contact/`)
- Contact form (name, email, subject, message)
- Office address, email, phone, hours
- Common questions sidebar

---

## Linkage to Phase 3 Requirements

| Phase 3 Requirement | Implementation |
|---------------------|---------------|
| Online application form with stage indicators | `/apply/` — 4 sectioned form |
| Partner university filterable directory | `/programs/` — country filter |
| Real-time application status tracking | `/track/` — by reference number |
| Unique application reference number | Auto-generated on submit (ISEO-XXXXXX) |
| Eligibility checker (GPA threshold) | `/eligibility/` — interactive tool |
| Direct contact mechanism | `/contact/` — contact form |
| Backup university selection | Second choice field on application |
| Visibility of system status (Nielsen heuristic) | Status timeline on track page |

---

## Linkage to WBS Activities

| WBS Activity | What was delivered |
|---|---|
| 1.4.1 Design system architecture | Django app/view/model architecture |
| 1.4.2 Design database schema (ERD) | `models.py` — PartnerUniversity, Application, ContactMessage |
| 1.4.3 Design UI wireframes | All 8 page templates with consistent styling |
| 1.4.4 Design application workflow | Multi-step application → reference → tracking flow |

---

## Project Structure

```
iseo_project/
├── manage.py
├── setup.sh
├── README.md
├── iseo_site/           ← Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── iseo/                ← Main application
    ├── models.py        ← Database models
    ├── views.py         ← Page logic
    ├── forms.py         ← Form definitions & validation
    ├── urls.py          ← URL routing
    ├── admin.py         ← Admin panel config
    ├── fixtures/
    │   └── universities.json  ← Seed data (8 universities)
    └── templates/iseo/
        ├── base.html
        ├── home.html
        ├── about.html
        ├── programs.html
        ├── apply.html
        ├── apply_success.html
        ├── track_status.html
        ├── contact.html
        └── eligibility.html
```

---

## Technology Stack

- **Backend:** Django 4.x (Python)
- **Database:** SQLite (development) — easily switched to PostgreSQL for production
- **Frontend:** HTML5, CSS3, JavaScript (vanilla) — no external framework needed
- **Fonts:** Playfair Display (headings) + Source Sans 3 (body) via Google Fonts
- **Admin:** Django built-in admin panel at `/admin/`

---

*ISOM 331 · Phase 4 · Group Project · Spring 2026*
