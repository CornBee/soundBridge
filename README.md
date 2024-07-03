# SoundBridge

SoundBridge is an innovative AI-powered music creation and collaboration platform. It combines advanced AI tools with a user-friendly interface, allowing both seasoned musicians and beginners to create, modify, and collaborate on music projects effortlessly.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Testing](#testing)
- [Code Quality](#code-quality)
- [CI/CD](#cicd)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- **AI-Powered Music Creation**: Utilize cutting-edge AI tools to create and modify music based on user preferences.
- **Interactive Mind Map Interface**: Visualize and edit music structure using an intuitive radial mind map.
- **Collaborative Platform**: Search for and collaborate with other musicians in real-time.
- **Version Control for Music**: Track changes and revert to previous versions of your musical compositions.
- **Adaptive AI Learning**: AI model that learns and adapts to individual user preferences over time.
- **Multi-instrument Support**: Create and edit tracks for various instruments within the same project.
- **Real-time Audio Processing**: Instantly hear changes as you modify your music.
- **Export and Share**: Easy options to export your creations in various formats and share them on popular platforms.

## Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/) (v14.x or later)
- [Python](https://www.python.org/) (v3.8 or later)
- [Docker](https://www.docker.com/) (optional, for containerized development)
- [Git](https://git-scm.com/)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/CornBee/soundBridge.git
   cd soundBridge
   ```

2. **Backend Setup:**
   - Navigate to the backend directory:
     ```sh
     cd backend
     ```
   - Set up a virtual environment:
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install the dependencies:
     ```sh
     pip install -r requirements.txt
     ```

3. **Frontend Setup:**
   - Navigate to the frontend directory:
     ```sh
     cd ../frontend
     ```
   - Install the dependencies:
     ```sh
     npm install
     ```

### Running the Application

1. **Backend:**
   - Apply database migrations:
     ```sh
     cd backend
     alembic upgrade head
     ```
   - Start the backend server:
     ```sh
     uvicorn main:app --reload
     ```

2. **Frontend:**
   - Start the frontend development server:
     ```sh
     cd frontend
     npm run serve
     ```

3. **Using Docker (optional):**
   - Ensure Docker is running.
   - Navigate to the `.devcontainer` directory and run Docker Compose:
     ```sh
     cd .devcontainer
     docker-compose up --build
     ```

## Usage
Once the application is running, you can access it via your web browser. The frontend will be available at `http://localhost:8080`, and the backend API can be accessed at `http://localhost:8000`.

### Authentication
- Visit `http://localhost:8000/login` for Google OAuth2 authentication.

### AI-Powered Music Creation
1. **Create**: Start a new project or choose a template.
2. **Visualize**: Use the radial mind map interface to view and edit your music structure.
3. **Modify**: Adjust parameters, add/remove elements, and hear real-time changes.
4. **Collaborate**: Invite others to contribute to your project.
5. **Version**: Save versions of your work and revert if needed.
6. **Export**: Download your creation in various formats.

### Collaboration
- Search for other musicians on the platform and collaborate on music projects.
- Use built-in tools to communicate and share work seamlessly.

## Project Structure

```plaintext
soundBridge/
│
├── backend/
│   ├── alembic/
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── ai_music_generator.py
│   ├── collaboration_service.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── RadialMindMap.vue
│   │   │   └── AudioEditor.vue
│   │   ├── views/
│   │   ├── store/
│   │   ├── App.vue
│   │   └── main.js
│   └── package.json
│
├── .devcontainer/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
│
├── tests/
│
├── .dockerignore
├── .gitignore
└── README.md
```

## Development Workflow
1. Create a new branch for each feature or bug fix.
2. Write tests before implementing features (Test-Driven Development).
3. Use the GitHub Projects board to track tasks and progress.
4. Submit pull requests for code reviews before merging into the main branch.
5. Regularly update the project board and documentation.

## Testing
We use Jest for automated testing of our JavaScript code. To run the tests:

1. Ensure you have all dependencies installed:
   ```
   npm install
   ```
2. Run the tests:
   ```
   npm test
   ```
3. To run tests with coverage report:
   ```
   npm run test:coverage
   ```

Our CI pipeline automatically runs these tests on every push and pull request.

## Code Quality
We use SonarCloud for continuous code quality inspection. You can view our project's current status and issues here:

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=CornBee_soundBridge&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=CornBee_soundBridge)

[SonarCloud Issues](https://sonarcloud.io/project/issues?impactSoftwareQualities=MAINTAINABILITY&resolved=false&id=CornBee_soundBridge&open=AZB2oZiyJxGXGwmBKkpI)

We strive to maintain high code quality and address issues promptly. Contributors are encouraged to check SonarCloud before submitting pull requests.

## CI/CD
We use GitHub Actions for continuous integration and deployment:
- **CI**: Automatically runs tests, linting, and builds on every push and pull request. This includes running our Jest tests and submitting results to SonarCloud for analysis.
- **CD**: Deploys to staging environment on merges to the develop branch, and to production on merges to the main branch.

## Contributing
We welcome contributions to SoundBridge! If you're interested in helping out, here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the code quality standards enforced by SonarCloud.

For major changes, please open an issue first to discuss what you would like to change. Please ensure to update tests and documentation as appropriate.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [Vue.js](https://vuejs.org/) for the frontend framework
- [Google OAuth2](https://developers.google.com/identity/protocols/oauth2) for secure authentication
- [Jest](https://jestjs.io/) for JavaScript testing
- [SonarCloud](https://sonarcloud.io/) for code quality analysis
- [GitHub Actions](https://github.com/features/actions) for CI/CD
- [Docker](https://www.docker.com/) for containerization
- [Alembic](https://alembic.sqlalchemy.org/) for database migrations
- [D3.js](https://d3js.org/) for data visualization (if used for the mind map interface)