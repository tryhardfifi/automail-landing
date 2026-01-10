# Auto Mail Website

A simple, mobile-responsive static website for Auto Mail with landing page, privacy policy, and terms & conditions.

## Tech Stack

- Vite - Fast build tool
- Tailwind CSS - Utility-first CSS framework
- Firebase Hosting - Static site hosting

## Development

### Install Dependencies

```bash
npm install
```

### Run Development Server

```bash
npm run dev
```

The site will be available at `http://localhost:5173`

### Build for Production

```bash
npm run build
```

This creates an optimized build in the `dist/` directory.

### Preview Production Build

```bash
npm run preview
```

## Deployment to Firebase

### Prerequisites

Make sure you have Firebase CLI installed:

```bash
npm install -g firebase-tools
```

### Deploy

1. Build the project from the landing directory:
   ```bash
   npm run build
   ```

2. Deploy to Firebase from the firebase-functions directory:
   ```bash
   cd ../firebase-functions
   firebase deploy --only hosting
   ```

The site will be deployed to:
- https://js-code-802ec.web.app
- https://js-code-802ec.firebaseapp.com

## Project Structure

```
mail/
├── landing/              # Website files (this folder)
│   ├── index.html       # Landing page
│   ├── privacy.html     # Privacy policy page
│   ├── terms.html       # Terms & conditions page
│   ├── src/
│   │   └── style.css    # Tailwind CSS styles
│   ├── package.json     # Project dependencies
│   ├── vite.config.js   # Vite configuration
│   └── tailwind.config.js  # Tailwind configuration
├── firebase-functions/  # Firebase configuration
│   └── firebase.json    # Firebase hosting config
└── mail-ios/           # iOS app files
```

## Updating Content

### Privacy Policy

Edit the content in `privacy.html` between the section tags. The page structure and styling are already in place.

### Terms & Conditions

Edit the content in `terms.html` between the section tags. The page structure and styling are already in place.

### Landing Page

Edit `index.html` to update the hero section, features, or any other content.
