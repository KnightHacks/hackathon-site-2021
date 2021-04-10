[![Knight Hacks](https://via.placeholder.com/1230x323)](https://knighthacks.org/)

---

<div align="center">
<img alt="GitHub tag (latest by date)" src="https://img.shields.io/github/v/tag/KnightHacks/hackathon-site-2021" />
<img alt="GitHub" src="https://img.shields.io/github/license/KnightHacks/hackathon-site-2021" />
<img alt="W3C Validation" src="https://img.shields.io/w3c-validation/html?targetUrl=https%3A%2F%2Fknighthacks.org" />
<img alt="Frontend Status" src="https://img.shields.io/website?down_message=offline&label=frontend&logo=frontend&up_message=online&url=https%3A%2F%2Fknighthacks.org" />
<img alt="Frontend Mozilla HTTP Observatory Grade" src="https://img.shields.io/mozilla-observatory/grade/knighthacks.org?label=frontend%20observatory&logo=frontend%20observatory" />
<img alt="Backend Status" src="https://img.shields.io/website?down_message=offline&label=backend&logo=backend&up_message=online&url=https%3A%2F%2Fapi.knighthacks.org%2Fapidocs" />
<img alt="Backend Mozilla HTTP Observatory Grade" src="https://img.shields.io/mozilla-observatory/grade/api.knighthacks.org?label=backend%20observatory&logo=backend%20observatory" />
</div>

---

# Knight Hacks Hackathon 2021

Hackathon site for KnightHacks '21

## Contents

- [Frontend](frontend/README.md)
- [Backend](backend/README.md)
- [Quick Start](#quick-start)
- [File Structure](#file-structure)
- [Roadmap](#roadmap)
- [Contributing](CONTRIBUTING.md)
- [Maintainer](#maintainers)
- [License](#License)


## Quick Start

1. Clone the Project

`git clone https://github.com/KnightHacks/hackathon-site-2021.git`

2. Move to `hackathon-site-2021`

`cd hackathon-site-2021`


3. Run it

If you don't want to use Docker, skip to [Without Docker](#without-docker).

### With Docker

**Requirements**

- Docker
- Docker Compose

Start the compose stack

`docker-compose -f docker-compose.yml up -d`

Stop the compose stack

`docker-compose -f docker-compose.yml up -d`

### Without Docker

**Requirements**

- Node 14.16
- Python 3.9
- MongoDB
- RabbitMQ

1. Follow the [Frontend quick start guide](frontend/README.md#without-docker)

2. Follow the [Backend quick start guide](backend/README.md#without-docker)


## File Structure

```
.
├── docs
├── manifests                      # Kubernetes Deployment Manifests
├── backend                        # Backend source code
|   ├── src
|   |   ├── api                    # Contains all api routes in blueprints
|   |   ├── common
|   |   |   ├── decorators.py      # Middleware decorators
|   |   |   ├── error_handlers.py  # Ensures HTTP errors respond with json
|   |   |   ├── json.py            # Custom JSON Encoder Class
|   |   |   └── mail.py
|   |   ├── models                 # Defines MongoEngine Models
|   |   ├── tasks                  # Celery tasks
|   |   ├── templates/emails       # Jinja templates for sending emails
|   |   ├── __init__.py            # Initializes the server
|   |   ├── __main__.py            # Handles starting the server through the cli
|   |   ├── config.py              # Defines the Flask configs
|   |   └── schemas.yml            # Defines schemas used by openapi
|   ├── tests                      # Unit tests
|   |   ├── models                 # Unit tests for MongoEngine models
|   |   ├── routes                 # Unit tests for api routes
|   |   └── base.py                # BaseTestCase Class to be used by all test cases
|   ├── README.md
|   ├── requirements-dev.txt
|   └── requirements.txt
|
|
├── frontend                       # Frontend source code
|   ├── public
|   ├── src
|   |   ├── assets
|   |   ├── components
|   |   ├── pages
|   |   ├── App.js
|   |   ├── index.css
|   |   └── index.js
|   ├── tailwind.config.js
|   ├── README.md
|   └── package.json
|
|
├── docker-compose.yml
└── README.md
```

## Roadmap
- [x] Have a cool dev team
- [ ] Group matching
- [ ] QR code stuff
- [ ] Control Panel for Knight Hacks officials
- [ ] Automated Discord features

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## Maintainers

The Knight Hacks developer team.

## License
Should be under MIT imo
