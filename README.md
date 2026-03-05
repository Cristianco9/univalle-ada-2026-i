**Autor:** Cristian Camilo Cortes Ortiz

**Código:** 202478542

**Universidad del Valle**  

**Programa:** Tecnología en Desarrollo de Software

**Asignatura:** Análisis y Diseño de Algoritmos

**Profesor:** Daniel Quintero Capera  

**Fecha:** 04 Marzo 2026

---

# Análisis y Diseño de Algoritmos
# Taller de Complejidad Algorítmica (Big O y Big Ω)

## Objetivo

El objetivo de este proyecto es desarrollar una aplicación full-stack que permita
cargar, validar y procesar archivos CSV/TXT de usuarios, ordenando su información
desde el backend y devolviendo automáticamente un nuevo archivo listo para descargar.

---

# 📦 CSV User Processing System

A full-stack application that allows users to upload a CSV/TXT file, process and
 sort user data on the backend, and download the processed file automatically.

Built with:

- **Frontend:** Next.js 14 + TypeScript + TailwindCSS + Framer Motion
- **Backend:** Node.js + Express
- **File Handling:** Multer + Native File System APIs

---

# 🚀 Features

- Drag & drop file upload
- CSV/TXT validation
- Backend file parsing
- Sorting users (worst-case scenario supported)
- Automatic download of processed file
- Animated modern UI
- Error & success handling

---

# ⚙️ Requirements

Make sure you have installed:

- Node.js (v18+ recommended)
- npm (comes with Node)
- Git

Check versions:

```bash
node -v
npm -v
```

---

# 🔧 BACKEND SETUP

## 1️⃣ Navigate to backend

```bash
cd backend
```

## 2️⃣ Install dependencies

```bash
npm install
```

## 3️⃣ Run backend server

```bash
npm run dev
```

> **Backend will run on:**

```bash
http://localhost:4000
```

---

# 💻 FRONTEND SETUP

## 1️⃣ Navigate to frontend

```bash
cd frontend
```

## 2️⃣ Install dependencies

```bash
npm install
```

> **If not already installed:**

```bash
npm install framer-motion lucide-react
```

## 3️⃣ Run development server

```bash
npm run dev
```

> **Frontend will run on:**

```bash
http://localhost:3000
```

---

# 🔄 How the System Works

1. User selects or drags a CSV/TXT file.

2. Frontend sends file to:

    ```bash
    POST http://localhost:4000/api/files/upload
    ```

3. Backend:

    - Validates file

    - Parses CSV

    - Sorts users

    - Generates new CSV file

4. Backend returns processed file as a Blob.

5. Frontend automatically triggers download:

    ```bash
    sorted_users.csv
    ```

---

# 📁 Expected CSV Format

```bash
apellido1,nombre,apellido2,nombre2,NumCelular,correo,cedula
```

Example:

```bash
Gomez,Carlos,Lopez,Andres,3001234567,carlos@email.com,12345678
```

---

# 🧪 Testing With Postman

1. Open Postman

2. Create new request:

    - Method: POST

    - URL: http://localhost:4000/api/files/upload

3. Go to Body → form-data

4. Add key:

    - Key: file

    - Type: File

    - Select CSV file

5. Send request

> You should receive a processed CSV file.

---

# 🎨 Frontend UI Stack

- TailwindCSS (utility styling)

- Framer Motion (animations)

- Lucide React (icons)

- Glassmorphism design

- Gradient buttons

- Drag & drop animations

---

# 👨‍💻 Author

Cristian Camilo
Full-Stack Software Developer

---

# 📜 License

MIT License