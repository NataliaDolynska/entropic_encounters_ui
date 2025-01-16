/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    daisyui: {
        themes: [
            {
                entropic: {
                    primary: "#C14242",
                    secondary: "#2C91D4",
                    accent: "#F4A261",
                    neutral: "#E0E0E0",
                    'base-100': "#111827",
                    info: "#62B6CB",
                    success: "#2BA84A",
                    warning: "#F59E0B",
                    error: "#D14343",
                },
            },
        ],
    },

    content: [
        // Templates within theme app (e.g. base.html)
        '../templates/**/*.html',
        // Templates in other apps
        '../../templates/**/*.html',
        // Ignore files in node_modules
        '!../../**/node_modules',
        // Include JavaScript files that might contain Tailwind CSS classes
        '../../**/*.js',
        // Include Python files that might contain Tailwind CSS classes
        '../../**/*.py'
    ], // Include Django's templates/static
    theme: {
        extend: {
            colors: {
                primary: '#C14242',
                secondary: '#2C91D4',
                accent: '#F4A261',
                neutral: '#E0E0E0',
                base: '#111827',
                info: '#62B6CB',
                success: '#2BA84A',
                warning: '#F59E0B',
                error: '#D14343',
            },
            fontFamily: {
                heading: ['Orbitron', 'sans-serif'],
                body: ['Roboto', 'sans-serif'],
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('daisyui'),
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
