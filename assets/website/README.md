# Comics Factory - Web App Demo

This is the demo web application for Comics Factory, an AI-powered tool that generates consistent 10+ page comic books from a single photo and a prompt.

## Features

-   **AI Story Generation**: Generates complete stories based on a plot description.
-   **Consistent Characters**: Uses a user-uploaded photo to maintain protagonist consistency across all panels.
-   **Multi-Page Output**: Produces professional PDF storybooks.
-   **One-Click Experience**: Simple interface for generating complex content.
-   **Waitlist Integration**: Collects email subscriptions via Firebase Firestore.

## Tech Stack

-   **Backend**: Python (Flask)
-   **Frontend**: HTML, CSS, JavaScript (Vanilla)
-   **Database**: Firebase Firestore (for waitlist)
-   **Storage**: Firebase Storage (for serving generated PDFs)
-   **PDF Rendering**: PDF.js

## Setup & Running

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Firebase Setup**:
    -   Ensure you have `serviceAccountKey.json` in the root directory for local development, or use Application Default Credentials in production.

3.  **Run the Application**:
    ```bash
    flask --app main run
    ```

## Recent Updates (UI/UX)

-   **Inline PDF Preview**: Resulting comic books are displayed directly on the landing page.
-   **Compact Design**: Optimized layout to show the demo result "above the fold".
-   **Enhanced UX**: Added helper text, button-based genre selector, and clear value propositions.
-   **Contact**: Added support contact information.

## Project Structure

-   `main.py`: Flask application entry point.
-   `src/`: Contains HTML templates (`index.html`, `result.html`).
-   `public/`: Static assets (images, icons).