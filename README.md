# Entropic Encounters UI
<em>Entropic Encounters game UI implementation</em>

## 🤝 Acknowledgments

**Entropic Encounters** was created by **Prof. Dr. Laura Bechthold**, a thought leader in inclusive design, science
fiction thinking, and innovative learning methods. Her vision is to inspire dialogue and action toward building
equitable and sustainable futures.

For more about Prof. Dr. Laura Bechthold, visit:

- 🌐 Personal Website: [laurabechthold.com](https://laurabechthold.com/)
- 💼 LinkedIn Profile: [Prof. Dr. Laura Bechthold on LinkedIn](https://www.linkedin.com/in/laurabechthold/)
- 🏫 Academic Page: [Technical University of Ingolstadt Profile](https://www.thi.de/personen/prof-dr-laura-bechthold/)

## 🚀 Game Overview

Entropic Encounters is a collaborative, immersive game designed to explore the possibilities of building inclusive,
resilient, and sustainable futures using Science Fiction Thinking. This repository includes the UI framework for the
game, which guides players through their interstellar journey to distant planets and helps them engage with diverse
societies, fostering equity, innovation, and dialogue.

## Starting a Mission
![](https://github.com/NataliaDolynska/entropic_encounters_ui/blob/master/docs/gifs/main.gif)

## Chat interaction
![](https://github.com/NataliaDolynska/entropic_encounters_ui/blob/master/docs/gifs/chat.gif)

## 🌌 Game Phases in the UI

The UI is designed to guide players through the following phases:

**1. Starting the Mission**

**2. The Encounter Begins**

**3. Selection of a Planet 🪐**

**4. Learning About the Planet**

**5. Learning About the Society**

## 🖥️ How to Run the UI

To run the **Entropic Encounters** UI on your local machine, follow these steps:

### Prerequisites

Make sure you have the following installed:

- **Python 3.10 or higher**
- **[uv](https://astral.sh/blog/uv)** (Python package manager)
- **[node-js](https://nodejs.org/en/download)**  v19

### Steps to Run the UI

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YourUsername/entropic-encounters-ui.git
   cd entropic_encounters
   ```
2. **Install python dependencies**
   ```bash
   uv venv 
   source .venv/bin/activate   
   uv sync 
   ```

3. **Install Node-js dependencies**
   ```bash
   python manage.py tailwind install
   ```

4. **Compile Tailwind, DaisyUi styles**
   ```bash
   python manage.py tailwind start
   ```
    1. This step is only during UI development or on first run, to compile styles used in project. Not needed for
       production or integration
       development phases.


5. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```
6. **Run Django server**
   ```bash 
   python manage.py runserver
   open http://localhost:8000
   ```

## 📄 License

This project is licensed under the **Apache 2.0 License**. See the LICENSE file for details.
Please note: Public deployments of this game must visibly credit the original creator, **Prof. Dr. Laura Bechthold**, on the main UI.

Any public use or deployment of this software or derivative works thereof must display the text **“Made by Natalia Dolynska”** prominently in the primary user interface or an equally prominent location. 

Additionally, in case of code modification, the names of contributors should be included on a separate page with contact data or any additional information that will be considered necessary by contributors.
