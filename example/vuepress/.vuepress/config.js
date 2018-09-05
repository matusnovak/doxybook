module.exports = {
    title: 'Doxybook Example Output',
    description: 'Doxybook example output converted to static website via vuepress',
    base: '/doxybook/vuepress/',
    themeConfig: {
        sidebar: 'auto',
        nav: [
            { text: 'Home', link: '/' },
            { text: 'Modules', link: '/api/modules' },
            {
                text: 'Classes',
                items: [
                    { text: 'Class List', link: '/api/annotated' },
                    { text: 'Class Index', link: '/api/classes' },
                    { text: 'Function Index', link: '/api/functions' },
                    { text: 'Variable Index', link: '/api/variables' },
                    { text: 'Enumeration Index', link: '/api/enumerations' }
                ]
            },
            { text: 'Files', link: '/api/files' },
            { text: 'Pages', link: '/api/pages' },
            { text: 'Bugs', link: '/api/bug' }
        ]
    }
}
