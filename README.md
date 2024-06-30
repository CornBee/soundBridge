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
   git clone https://github.com/yourusername/soundBridge.git
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
│   │   └── versions/
│   │       └── b58e74009c38_initial_migration.py
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── ai_music_generator.py  # New file for AI music generation logic
│   ├── collaboration_service.py  # New file for collaboration features
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   │   ├── favicon.ico
│   │   └── index.html
│   ├── src/
│   │   ├── assets/
│   │   │   └── logo.png
│   │   ├── components/
│   │   │   ├── RadialMindMap.vue  # New component for mind map interface
│   │   │   └── AudioEditor.vue  # New component for audio editing
│   │   ├── views/
│   │   ├── store/
│   │   │   └── index.js
│   │   ├── views/
│   │   │   ├── AboutView.vue
│   │   │   └── HomeView.vue
│   │   ├── App.vue
│   │   └── main.js
│   ├── .editorconfig
│   ├── babel.config.js
│   ├── jsconfig.json
│   ├── package-lock.json
│   ├── package.json
│   └── vue.config.js
│
├── .devcontainer/
│
├── .github/
│   └── workflows/
│       ├── ci.yml  # Continuous Integration workflow
│       └── cd.yml  # Continuous Deployment workflow
│
├── tests/
│   ├── backend/
│   │   ├── Dockerfile
│   │   └── devcontainer.json
│   ├── frontend/
│   │   ├── Dockerfile
│   │   └── devcontainer.json
│   └── docker-compose.yml
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

## CI/CD
We use GitHub Actions for continuous integration and deployment:
- **CI**: Automatically runs tests, linting, and builds on every push and pull request.
- **CD**: Deploys to staging environment on merges to the develop branch, and to production on merges to the main branch.

## Contributing
This project is currently personal. For future collaboration possibilities, please contact cornbee80014@gmail.com.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework.
- [Vue.js](https://vuejs.org/) for the frontend framework.
- [Google OAuth2](https://developers.google.com/identity/protocols/oauth2) for secure authentication.