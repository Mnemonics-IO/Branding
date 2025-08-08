# Tailwind CSS Portfolio Project

A modern, responsive portfolio website built with Tailwind CSS and Node.js.

## 🚀 Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean and professional design using Tailwind CSS
- **Smooth Animations**: CSS transitions and hover effects
- **Interactive Navigation**: Smooth scrolling between sections
- **Contact Form**: Ready-to-use contact form (styling only)
- **Project Showcase**: Grid layout for displaying projects
- **Skills Section**: Showcase your technical skills

## 📁 Project Structure

```
tailwind-portfolio/
├── src/
│   └── input.css          # Tailwind CSS source file
├── dist/
│   └── output.css         # Compiled CSS file
├── images/                # Image assets folder
├── index.html             # Main HTML file
├── package.json           # Node.js dependencies
├── tailwind.config.js     # Tailwind configuration
└── README.md             # This file
```

## 🛠️ Installation & Setup

1. **Navigate to the project folder:**
   ```bash
   cd tailwind-portfolio
   ```

2. **Dependencies are already installed**, but if you need to reinstall:
   ```bash
   npm install
   ```

3. **Build the CSS:**
   ```bash
   npm run build
   ```

4. **For development with auto-rebuild:**
   ```bash
   npm run build-css
   ```

5. **Open the project:**
   - Simply open `index.html` in your web browser
   - Or use a local server for better development experience

## 📝 Customization

### Changing Colors
Edit the `tailwind.config.js` file to customize the color palette:

```javascript
colors: {
  'primary': {
    // Your custom colors here
  }
}
```

### Adding Content
- **Personal Information**: Update name, title, and bio in `index.html`
- **Projects**: Replace placeholder projects with your own work
- **Skills**: Modify the skills section with your technologies
- **Contact Info**: Update email, phone, and location

### Adding Images
- Add your profile photo and project screenshots to the `images/` folder
- Update the image paths in `index.html`

## 🎨 Available Scripts

- `npm run build` - Build CSS for production
- `npm run build-css` - Build CSS with watch mode for development
- `npm run dev` - Start live server (if live-server is installed)

## 🌐 Browser Support

This portfolio works in all modern browsers:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## 📱 Mobile Responsive

The portfolio is fully responsive and includes:
- Mobile-first design approach
- Responsive navigation
- Flexible grid layouts
- Touch-friendly buttons and links

## 🚀 Deployment

You can deploy this portfolio to any static hosting service:

1. **GitHub Pages**
2. **Netlify**
3. **Vercel**
4. **Firebase Hosting**

Just upload the files and you're ready to go!

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Happy coding!** 🎉
