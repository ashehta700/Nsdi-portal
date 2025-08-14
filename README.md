# 🌍 NSDI GEO Portal

An **Enterprise National Spatial Data Infrastructure (NSDI) Web Portal** designed for secure geospatial data management, sharing, and collaboration.  
Built with advanced authentication, role-based access control, and integrated GIS capabilities, the portal provides **WMS, WMTS, and WFS services** powered by **OpenLayers** and a custom backend.

---

## 📖 Overview

The NSDI GEO Portal enables government agencies, organizations, and the public to access and interact with geospatial datasets securely.  
It supports **real-time map visualization**, **feature querying**, **user collaboration**, and **file management**, all controlled through **granular permissions**.

This portal is deployed on **Windows Server 2016 IIS** with full support for **HTTP/HTTPS** on standard ports.

---

## ✨ Key Features

### 🔐 Authentication & Security
- **Login attempt limit** – 3 incorrect attempts block the user’s **public IP** for 15 minutes.
- **Secure user authentication** with password encryption.
- **Role-based access control** for different user levels:
  - **Super Admin**
  - **Admin**
  - **Sub Admin**
  - **Regular User**
- **Session management** to prevent unauthorized access.

### 👤 User Management
- **Registration page** with detailed profile creation.
- **Custom roles and permissions** for each user.
- **Admin interface** to manage all users.

### 🗺️ GEO Portal
- **Interactive map viewer** with **OpenLayers**.
- Supports **WMS**, **WMTS**, and **WFS** services.
- **Layer management** – toggle, reorder, and view metadata.
- **Feature info retrieval**:
  - Click on a point to send **X/Y coordinates** to the backend.
  - Backend processes intersection queries and returns feature details.
- **Dynamic styling** for better visualization.

### 📰 News & Community
- **News page** – manage and publish news articles.
- **Visit tracking** – record visits per user with IP logging.
- **Community forum** – users can ask and answer questions.

### 📁 File Management
- **Upload & download** files using IIS services.
- Controlled access based on user permissions.

### 📬 Communication
- **Contact Us** form – send messages directly to admin.
- **Internal messaging system** – communicate between users and admins.

### 🛠️ Admin Panels
- **Admin Panel 1** – Dashboard with an intuitive interface for **Super Admin** to monitor all portal data.
- **Admin Panel 2** – Direct management of all database tables without server-level access.

### 📦 Deployment
- Deployed on **IIS** (Windows Server 2016).
- Running on **HTTP (Port 80)** and **HTTPS (Port 443)**.

---

## 🛠️ Technology Stack

- **Backend:** ASP.NET / C# (IIS Hosted)
- **Frontend:** HTML5, CSS3, JavaScript
- **GIS Library:** OpenLayers
- **Services:** WMS, WMTS, WFS
- **Database:** SQL Server
- **Server:** Windows Server 2016 IIS

---

## 📂 Project Structure

📦 NSDI-GEO-Portal
- 📂 wwwroot # Static files (CSS, JS, images)
- 📂 Controllers # Backend logic
- 📂 Models # Database models
- 📂 Views # Frontend pages
- 📜 web.config # IIS configuration
- 📜 README.md # Documentation

---

## 🚀 Installation & Deployment

### 1️⃣ Requirements
- Windows Server 2016 or later
- IIS installed and configured
- SQL Server (2016+)
- .NET Framework compatible with the application

### 2️⃣ Deployment Steps
1. Copy project files to IIS web root.
2. Configure IIS site bindings:
   - **HTTP:** Port 80
   - **HTTPS:** Port 443 (SSL certificate required)
3. Configure database connection in `web.config`.
4. Create required SQL Server tables and run migration scripts.
5. Start the IIS site and verify access.

---

## 🌍 GIS Capabilities in Detail

- **Layer Query by Point**: Click on the map sends **X/Y coordinates** to the backend, which:
  1. Matches the location against registered GIS layers.
  2. Returns **feature attributes** for the intersected location.
  3. Displays results with a **linked WMS image** of the area.

- **Service Integration**:
  - **WMS** – Raster map layers.
  - **WMTS** – Pre-rendered map tiles for performance.
  - **WFS** – Vector features for analysis.

---


---

## 📚 Use Cases

- National spatial data infrastructure portals.
- Government GIS data sharing platforms.
- Environmental monitoring dashboards.
- Urban planning & infrastructure management.

---

## 🖋️ Author

**Ahmed Shehta**  
🌐 Portfolio: [ahmed-shehta.netlify.app](https://ahmed-shehta.netlify.app)  
📧 Email: [ashehta700@gmail.com](mailto:ashehta700@gmail.com)   
🔗 GitHub: [ashehta700](https://github.com/ashehta700)  

---

## 📜 License

This project is proprietary. For inquiries about usage, licensing, or collaboration, please contact the author.


