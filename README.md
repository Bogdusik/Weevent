# Weevent

A dynamic platform that transforms how users discover local events and points of interest. Features an interactive map interface, event interaction tools, and AI-powered recommendations. Designed to connect communities and make exploring nearby happenings effortless.

## Demo

![Interactive Map](screenshots/map.png)
![Event Discovery](screenshots/events.png)
![Event Details](screenshots/event-details.png)

## Why It's Cool

- **Interactive Map Interface**: Discover events on a dynamic map with detailed information, navigation options, and location-based filtering
- **Event Engagement**: Follow, like, and share events to enhance community engagement and event discovery
- **Event Advertising**: Platform for organizers to promote events to a wider audience
- **AI-Powered Recommendations**: Personalized event suggestions powered by Llama 3.2 AI assistant (coming soon)
- **Cross-Platform**: Responsive design accessible on both desktop and mobile devices
- **Favorites System**: Save events for future reference with easy-to-use favorite functionality

## Tech Stack

- **Frontend**: HTML5, JavaScript, CSS
- **Backend**: MySQL, Python (framework under selection)
- **AI**: Llama 3.2 (planned)
- **APIs**: Various location and event APIs

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Bogdusik/Weevent.git
   cd Weevent
   ```

2. **Set up backend:**
   ```bash
   cd backend/weevents_backend
   # Follow backend setup instructions
   ```

3. **Set up frontend:**
   ```bash
   cd frontend
   # Open index.html or use a local server
   python -m http.server 8000
   ```

4. **Configure database:**
   - Set up MySQL database
   - Configure connection in backend settings

> **Note**: Backend framework is under selection. Check project structure for current implementation.

## Project Structure

```
Weevent/
├── frontend/                   # Frontend Application
│   ├── [HTML/CSS/JS files]    # Frontend code
│   └── styles/                 # CSS styles
│
├── backend/                    # Backend Application
│   └── weevents_backend/       # Backend code
│
├── scripts/                    # Utility Scripts
│   └── [script files]
│
├── images/                     # Static Assets
│   └── [image files]
│
└── [config files]             # Configuration files
    └── README.md
```

## What I Learned

- **Interactive Maps**: Integrated map functionality for location-based event discovery and visualization
- **Event Management Systems**: Designed data models and workflows for event creation, discovery, and interaction
- **Community Features**: Implemented social features like following, liking, and sharing events
- **Responsive Design**: Built cross-platform interface optimized for both desktop and mobile experiences
- **Database Design**: Structured MySQL database schema for events, users, and interactions
- **AI Integration Planning**: Designed architecture for AI-powered event recommendations and conversational assistance

Fork it, use it, improve it - open to PRs!
